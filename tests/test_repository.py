import contextlib
import csv
import importlib.util
import io
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from install import install
from validate import validate, parse_document
from demo_residuals import compute
from build_docs import build

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        # macOS /var points to /private/var. Supply the explicit real
        # temporary path; the separate symlink test still checks refusal.
        self.base = Path(self.tmp.name).resolve()
        self.dest = self.base / 'skills'
    def tearDown(self):
        self.tmp.cleanup()
    def run_install(self, *args, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return install(*args, **kwargs)
    def test_all_files_preserved(self):
        targets = self.run_install(self.dest)
        self.assertEqual(len(targets), 14)
        for source in (ROOT / 'skills').rglob('*'):
            if source.is_file():
                self.assertEqual(source.read_bytes(), (self.dest / source.relative_to(ROOT / 'skills')).read_bytes())
    def test_dry_run_creates_nothing(self):
        targets = self.run_install(self.dest, dry_run=True)
        self.assertEqual(len(targets), 14)
        self.assertFalse(self.dest.exists())
    def test_collision_preflight_is_whole_run(self):
        existing = self.dest / 'mixed-effects-reml'
        existing.mkdir(parents=True)
        (existing / 'keep.txt').write_text('original')
        with self.assertRaises(FileExistsError):
            self.run_install(self.dest)
        self.assertEqual(sorted(p.name for p in self.dest.iterdir()), ['mixed-effects-reml'])
        self.assertEqual((existing / 'keep.txt').read_text(), 'original')
    def test_selective_install(self):
        self.run_install(self.dest, ['evidence-chain'])
        self.assertEqual([p.name for p in self.dest.iterdir()], ['evidence-chain'])
    def test_unsafe_and_unknown_names(self):
        for name in ['../outside', '/absolute', 'UNKNOWN', 'not-a-real-skill', 'evidence-chain/../x']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.run_install(self.dest, [name])
        self.assertFalse(self.dest.exists())
    def test_destination_file(self):
        self.dest.write_text('preserved')
        with self.assertRaises(ValueError):
            self.run_install(self.dest)
        self.assertEqual(self.dest.read_text(), 'preserved')
    def test_symlink_destination(self):
        real = self.base / 'real'
        real.mkdir()
        try:
            self.dest.symlink_to(real, target_is_directory=True)
        except OSError:
            self.skipTest('OS does not permit unprivileged symlinks')
        with self.assertRaises(ValueError):
            self.run_install(self.dest)
        self.assertEqual(list(real.iterdir()), [])
    def test_cli_project_root_required(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--scope', 'project'], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
    def test_project_scope_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--scope', 'project', '--project-root', str(self.base), '--skill', 'evidence-chain'], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertTrue((self.base / '.agents/skills/evidence-chain/SKILL.md').is_file())

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'repository'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', 'site', '__pycache__', 'local-results'))
    def tearDown(self):
        self.tmp.cleanup()
    def test_repository_valid(self):
        self.assertEqual(validate(ROOT), [])
    def test_name_mismatch_caught(self):
        file = self.root / 'skills/evidence-chain/SKILL.md'
        file.write_text(file.read_text(encoding='utf-8').replace('name: evidence-chain', 'name: wrong-name'), encoding='utf-8')
        self.assertTrue(any('name differ' in e for e in validate(self.root)))
    def test_broken_link_caught(self):
        file = self.root / 'README.md'
        with file.open('a', encoding='utf-8') as stream:
            stream.write('\n[missing](docs/nonexistent.md)\n')
        self.assertTrue(any('broken local link' in e for e in validate(self.root)))
    def test_bad_yaml_caught(self):
        (self.root / 'skills/evidence-chain/SKILL.md').write_text('---\nname: [\n---\nbody', encoding='utf-8')
        self.assertTrue(validate(self.root))
    def test_broken_anchor_caught(self):
        file = self.root / 'README.md'
        with file.open('a', encoding='utf-8') as stream:
            stream.write('\n[missing anchor](CONTRIBUTING.md#no-such-anchor)\n')
        self.assertTrue(any('broken anchor' in e for e in validate(self.root)))
    def test_built_site_links_resolve(self):
        site = Path(self.tmp.name) / 'site'
        with contextlib.redirect_stdout(io.StringIO()):
            pages = build(site)
        self.assertGreaterEqual(pages, 25)
        from urllib.parse import unquote, urlsplit
        for page in site.rglob('*.html'):
            for link in parse_document(page).links:
                u = urlsplit(link)
                if not u.scheme and not u.netloc and u.path:
                    target = page.parent / unquote(u.path)
                    self.assertTrue(target.exists(), f'{page}: {link}')
    def test_fixture_known_values(self):
        result = compute(ROOT / 'examples/synthetic-residuals/records.csv')
        expected = json.loads((ROOT / 'examples/synthetic-residuals/expected.json').read_text())['residuals']
        self.assertEqual(result.keys(), expected.keys())
        for key in expected:
            self.assertAlmostEqual(result[key], expected[key], places=12)
    def test_duplicate_record_rejected(self):
        file = Path(self.tmp.name) / 'bad.csv'
        file.write_text('record_id,observed_g,predicted_g\nx,0.1,0.2\nx,0.1,0.2\n')
        with self.assertRaises(ValueError):
            compute(file)
    def test_invalid_motion_rejected(self):
        for value in ['0', '-0.1', 'nan', 'inf']:
            file = Path(self.tmp.name) / 'bad.csv'
            file.write_text(f'record_id,observed_g,predicted_g\nx,{value},0.2\n')
            with self.subTest(value=value), self.assertRaises(ValueError):
                compute(file)

if __name__ == '__main__':
    unittest.main()
