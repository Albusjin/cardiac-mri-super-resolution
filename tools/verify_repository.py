#!/usr/bin/env python3
"""Generate or verify a portable SHA-256 inventory using only the standard library."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'REPOSITORY_MANIFEST.json'
EXCLUDED_DIRS = {'.git', '.sync-local', '__pycache__', '.venv', 'venv', 'node_modules',
                 'data', 'datasets', 'checkpoints', 'weights', 'runs', 'wandb'}
EXCLUDED_EXTENSIONS = {'.pyc', '.pem', '.key', '.pth', '.pt', '.ckpt', '.safetensors',
                       '.nii', '.h5', '.hdf5', '.zip'}


def included(path):
    rel = path.relative_to(ROOT)
    if rel.as_posix() == '.obsidian/workspace.json':
        return False  # Device-specific Obsidian UI state is not a shared artifact.
    if rel.as_posix() == 'output/pdf/Nature Skills 中文使用指南.pdf':
        return False  # Duplicate export contains a machine-specific home path.
    if path == MANIFEST or path.is_symlink() or any(x in EXCLUDED_DIRS for x in rel.parts):
        return False
    if path.name in {'.DS_Store', '.env'} or path.name.startswith(('.env.', 'credentials', 'secrets', 'id_rsa', 'id_ed25519')):
        return path.name == '.env.example'
    return path.suffix.lower() not in EXCLUDED_EXTENSIONS and not path.name.endswith('.nii.gz')


def inventory():
    result = []
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or not included(p):
            continue
        sha = hashlib.sha256()
        with p.open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                sha.update(chunk)
        result.append({'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                       'sha256': sha.hexdigest()})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='replace the inventory after checking intended changes')
    args = parser.parse_args()
    current = inventory()
    if args.write:
        MANIFEST.write_text(json.dumps({'version': 1, 'algorithm': 'sha256', 'files': current},
                                       ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'已更新文件清单：{len(current)} 个文件。清单自身不计入。')
        return
    if not MANIFEST.exists():
        sys.exit('缺少 REPOSITORY_MANIFEST.json；请先使用 --write 创建。')
    recorded = {item['path']: item for item in json.loads(MANIFEST.read_text(encoding='utf-8'))['files']}
    actual = {item['path']: item for item in current}
    missing = sorted(recorded.keys() - actual.keys())
    added = sorted(actual.keys() - recorded.keys())
    changed = sorted(p for p in recorded.keys() & actual.keys() if recorded[p] != actual[p])
    for label, paths in [('缺失', missing), ('未记录', added), ('内容变化', changed)]:
        for p in paths:
            print(f'{label}: {p}')
    if missing or added or changed:
        sys.exit(1)
    print(f'PASS: {len(current)} 个文件与 SHA-256 清单一致（清单本身不计入）。')


if __name__ == '__main__':
    main()
