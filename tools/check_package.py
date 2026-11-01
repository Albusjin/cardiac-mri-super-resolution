#!/usr/bin/env python3
"""Validate package hashes and local document links; standard library only."""
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.links.append(value)


def main():
    root = Path(__file__).resolve().parents[1]
    failures = []
    count = 0
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest, relative = line.split('  ', 1)
        target = (root / relative).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            failures.append(f'文件缺失或越界: {relative}')
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != digest:
            failures.append(f'哈希不符: {relative}')
        count += 1

    link_count = 0
    for path in sorted(root.iterdir()):
        if path.suffix not in ('.html', '.md'):
            continue
        source = path.read_text(encoding='utf-8')
        if path.suffix == '.html':
            parser = LinkParser()
            parser.feed(source)
            links = parser.links
        else:
            # Code fences are examples, not navigable document links.
            source = re.sub(r'```.*?```', '', source, flags=re.S)
            links = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', source)
        for link in links:
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            link_count += 1
            if not target.is_relative_to(root) or not target.exists():
                failures.append(f'链接无效: {path.name} -> {link}')

    if failures:
        print('\n'.join(failures))
        raise SystemExit(1)
    print(f'PASS: {count} 个文件哈希一致；{link_count} 个本地链接可达。')
    print('校验范围为本资料包；未验证远程链接、训练效果或临床结论。')


if __name__ == '__main__':
    main()
