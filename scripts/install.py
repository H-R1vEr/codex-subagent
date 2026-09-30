#!/usr/bin/env python3
"""Local, no-overwrite installer; standard library only, Python 3.10+."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def install(destination: Path, names: list[str] | None = None, dry_run: bool = False,
            root: Path = ROOT) -> list[Path]:
    root = root.resolve()
    catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    allowed = {entry['name'] for entry in catalog}
    selected = sorted(allowed if names is None else set(names))
    if not selected:
        raise ValueError('No skills selected')
    for name in selected:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name not in allowed:
            raise ValueError(f'Unknown or unsafe skill name: {name!r}')
    # Reject symlink/junction destination components before resolving paths.
    destination = Path(os.path.abspath(destination.expanduser()))
    if any(p.is_symlink() or (hasattr(p, 'is_junction') and p.is_junction())
           for p in (destination, *destination.parents)):
        raise ValueError('Destination traverses a symlink/junction; choose its explicit real path')
    if destination.exists() and not destination.is_dir():
        raise ValueError('Destination must be a directory')
    source_root = root / 'skills'
    sources = []
    targets = []
    for name in selected:
        source = source_root / name
        if not source.is_dir() or not (source / 'SKILL.md').is_file():
            raise ValueError(f'Incomplete source skill: {name}')
        for path in (source, *source.rglob('*')):
            if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
                raise ValueError(f'Source symlink/junction refused: {path}')
        if source.resolve().parent != source_root.resolve():
            raise ValueError(f'Source escapes skills directory: {name}')
        target = destination / name
        if target.exists() or target.is_symlink():
            raise FileExistsError(f'Existing skill preserved; installation aborted: {target}')
        if destination == source or destination.is_relative_to(source):
            raise ValueError('Destination overlaps a source skill')
        sources.append(source)
        targets.append(target)
    for source, target in zip(sources, targets):
        print(f'{"DRY-RUN" if dry_run else "COPY"} {source} -> {target}')
    if dry_run:
        return targets
    # Stage copies completely before touching final skill names. Reserve each
    # final directory using mkdir(exist_ok=False), never overwriting a collision.
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    with tempfile.TemporaryDirectory(prefix='.researchflow-stage-', dir=destination) as stage:
        staged = []
        for source in sources:
            p = Path(stage) / source.name
            shutil.copytree(source, p)
            staged.append(p)
        try:
            for staged_source, target in zip(staged, targets):
                target.mkdir(exist_ok=False)
                created.append(target)
                shutil.copytree(staged_source, target, dirs_exist_ok=True)
        except Exception:
            # Only roll back directories this invocation successfully reserved.
            for target in reversed(created):
                shutil.rmtree(target)
            raise
    return targets

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scope', choices=['user', 'project'], default='user')
    parser.add_argument('--project-root', type=Path)
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--skill', action='append', dest='skills')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    if args.scope == 'project':
        if args.project_root is None or not args.project_root.is_dir():
            parser.error('project scope requires an explicit existing --project-root')
    destination = args.destination or (
        args.project_root / '.agents' / 'skills' if args.scope == 'project'
        else Path.home() / '.agents' / 'skills')
    try:
        targets = install(destination, args.skills, args.dry_run)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f'{len(targets)} skills {"planned; no files changed" if args.dry_run else "installed"}.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
