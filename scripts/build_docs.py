#!/usr/bin/env python3
"""Render a navigable static site, without CDN or JavaScript dependencies."""
import html
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit, urlunsplit
import markdown

ROOT = Path(__file__).resolve().parents[1]

def destination(path: Path, site: Path) -> Path:
    rel = path.relative_to(ROOT)
    return site / (rel.with_suffix('.html') if path.suffix == '.md' else rel)

def rewrite(content: str, source: Path, output: Path, site: Path) -> str:
    def replace(match):
        prefix, url, quote = match.groups()
        parts = urlsplit(html.unescape(url))
        if parts.scheme or parts.netloc or not parts.path:
            return match[0]
        target = (source.parent / unquote(parts.path)).resolve()
        if not target.is_relative_to(ROOT):
            raise ValueError(f'Escaping docs link: {url}')
        mapped = destination(target, site)
        rel = os.path.relpath(mapped, output.parent).replace(os.sep, '/')
        return prefix + html.escape(urlunsplit(('', '', rel, parts.query, parts.fragment)), quote=True) + quote
    return re.sub(r'((?:href|src)=")(.*?)(")', replace, content)

def build(site: Path = ROOT / 'site') -> int:
    site.mkdir(parents=True, exist_ok=True)
    # Build into a caller-controlled directory without recursive deletion.
    pages = 0
    for source in ROOT.rglob('*'):
        rel = source.relative_to(ROOT)
        if not source.is_file() or any(p in rel.parts for p in ('.git', 'site', '.agents', 'local-results', '__pycache__')):
            continue
        if source == ROOT / 'docs/index.html':
            continue
        if source.suffix not in {'.md', '.css', '.js', '.json', '.csv', '.svg', '.png', '.jpg'} and source.name not in {'LICENSE', 'VERSION'}:
            continue
        out = destination(source, site)
        out.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == '.md':
            text = source.read_text(encoding='utf-8')
            text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
            rendered = markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc'])
            rendered = rewrite(rendered, source, out, site)
            css = os.path.relpath(site / 'docs/assets/style.css', out.parent).replace(os.sep, '/')
            home = os.path.relpath(site / 'index.html', out.parent).replace(os.sep, '/')
            out.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(source.stem)} · ResearchFlow</title><link rel="stylesheet" href="{css}"></head><body><nav><a class="brand" href="{home}">RF / ResearchFlow</a></nav><main class="document">{rendered}</main></body></html>\n', encoding='utf-8')
            pages += 1
        else:
            shutil.copyfile(source, out)
    source = ROOT / 'docs/index.html'
    index = site / 'index.html'
    index.write_text(rewrite(source.read_text(encoding='utf-8'), source, index, site), encoding='utf-8')
    # Also keep docs/index.html usable when navigated to from rendered documents.
    out = site / 'docs/index.html'
    out.write_text(rewrite(source.read_text(encoding='utf-8'), source, out, site), encoding='utf-8')
    (site / '.nojekyll').write_text('', encoding='utf-8')
    print(f'Built {pages} documentation pages plus homepage in {site}')
    return pages

if __name__ == '__main__':
    build()
