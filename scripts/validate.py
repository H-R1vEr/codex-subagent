#!/usr/bin/env python3
"""Validate original skill structure, metadata, catalog and local references."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import yaml
import markdown

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
REQUIRED = ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
            'CHANGELOG.md', 'SECURITY.md', 'catalog.json', 'VERSION',
            'docs/index.html', 'scripts/install.ps1', 'scripts/install.sh',
            '.github/workflows/validate.yml', '.github/workflows/pages.yml']

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'id' in data:
            self.ids.add(data['id'])
        for attr in ('href', 'src'):
            if attr in data:
                self.links.append(data[attr])

def parse_document(path: Path) -> Links:
    text = path.read_text(encoding='utf-8')
    if path.suffix.lower() == '.md':
        text = re.sub(r'\A---\r?\n.*?\r?\n---\r?\n', '', text, flags=re.S)
        text = markdown.markdown(text, extensions=['fenced_code', 'tables', 'toc'])
    parser = Links()
    parser.feed(text)
    return parser

def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding='utf-8-sig')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z', text, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter delimiters')
    data = yaml.safe_load(match[1])
    if not isinstance(data, dict):
        raise ValueError('Frontmatter must be a mapping')
    return data, match[2]

def validate(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    errors = []
    def fail(path, message):
        errors.append(f'{path}: {message}')
    for item in REQUIRED:
        if not (root / item).is_file():
            fail(item, 'required file missing')
    skills = root / 'skills'
    found = {}
    for folder in sorted(skills.iterdir()) if skills.is_dir() else []:
        if not folder.is_dir():
            fail(folder.name, 'unexpected file in skills root')
            continue
        path = folder / 'SKILL.md'
        try:
            data, body = frontmatter(path)
        except (ValueError, OSError, yaml.YAMLError) as exc:
            fail(str(path.relative_to(root)), str(exc))
            continue
        name = data.get('name')
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) >= 64:
            fail(folder.name, 'name must be lowercase hyphenated and under 64 characters')
        if name != folder.name:
            fail(folder.name, 'folder and frontmatter name differ')
        if name in found:
            fail(folder.name, 'duplicate name')
        if isinstance(name, str):
            found[name] = folder
        desc = data.get('description')
        if not isinstance(desc, str) or not 20 <= len(desc) <= 1024:
            fail(folder.name, 'description must be 20–1024 characters')
        if len(body.strip()) < 100:
            fail(folder.name, 'workflow body is missing or too short')
        if re.search(r'\bTODO\b|\bTBD\b|\[INSERT[^\]]*\]|\[REPLACE[^\]]*\]', body):
            fail(folder.name, 'unfinished scaffold marker')
        for child in folder.iterdir():
            if child.name not in {'SKILL.md', 'agents', 'references', 'scripts', 'assets'}:
                fail(folder.name, f'unsupported skill resource: {child.name}')
        try:
            meta = yaml.safe_load((folder / 'agents/openai.yaml').read_text(encoding='utf-8'))
            interface = meta['interface']
            if not isinstance(interface.get('display_name'), str) or not interface['display_name'].strip():
                fail(folder.name, 'display_name missing')
            if not isinstance(interface.get('short_description'), str) or not 25 <= len(interface['short_description']) <= 64:
                fail(folder.name, 'UI short_description must be 25–64 chars')
            if f'${name}' not in interface.get('default_prompt', ''):
                fail(folder.name, 'default_prompt must mention skill')
            if meta.get('policy', {}).get('allow_implicit_invocation') is not True:
                fail(folder.name, 'V1 skills must allow implicit invocation')
        except (OSError, KeyError, TypeError, yaml.YAMLError) as exc:
            fail(folder.name, f'UI metadata invalid: {exc}')
    try:
        catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
        names = [x['name'] for x in catalog]
        if len(names) != len(set(names)) or set(names) != set(found):
            fail('catalog.json', 'catalog names must match skills uniquely')
        for entry in catalog:
            if entry['path'] != f"skills/{entry['name']}" or entry['layer'] not in {'Earthquake', 'Reasoning', 'Router', 'Journal'}:
                fail('catalog.json', f'invalid path/layer: {entry}')
            if entry['name'] in found:
                skill_data, _ = frontmatter(found[entry['name']] / 'SKILL.md')
                if entry.get('description') != skill_data.get('description'):
                    fail('catalog.json', f"description drift: {entry['name']}")
    except (ValueError, OSError, KeyError, TypeError) as exc:
        fail('catalog.json', str(exc))
    files = [p for p in root.rglob('*') if p.suffix.lower() in {'.md', '.html'}
             and not any(x in p.relative_to(root).parts for x in ('.git', 'site', '.agents', 'local-results', '__pycache__'))]
    docs = {}
    for path in files:
        try:
            docs[path] = parse_document(path)
        except (OSError, UnicodeError) as exc:
            fail(str(path.relative_to(root)), str(exc))
    for source, document in docs.items():
        for link in document.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target = (source.parent / unquote(parts.path)).resolve() if parts.path else source
            if not target.is_relative_to(root):
                fail(str(source.relative_to(root)), f'link escapes repository: {link}')
            elif not target.exists():
                fail(str(source.relative_to(root)), f'broken local link: {link}')
            elif parts.fragment and target in docs and unquote(parts.fragment) not in docs[target].ids:
                fail(str(source.relative_to(root)), f'broken anchor: {link}')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    count = len(list((args.root / 'skills').glob('*/SKILL.md')))
    print(f'PASS: {count} skills; frontmatter, UI, catalog, structure and local links checked')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
