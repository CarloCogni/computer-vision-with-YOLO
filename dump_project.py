#!/usr/bin/env python3
"""Dump all project files into a single text file for LLM context."""

import os
import sys

# Extensions to include (add/remove as needed)
TEXT_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.scss',
    '.json', '.yaml', '.yml', '.toml', '.cfg', '.ini', '.env',
    '.md', '.txt', '.rst', '.sh', '.bash', '.sql', '.xml',
    '.c', '.cpp', '.h', '.hpp', '.java', '.go', '.rs',
    '.django', '.jinja', '.jinja2',
}

# Directories to skip
SKIP_DIRS = {
    '.git', '__pycache__', 'node_modules', '.venv', 'venv', 'env',
    '.mypy_cache', '.pytest_cache', 'dist', 'build', '.egg-info',
    'migrations', '.idea', '.vscode', 'static/vendor',
}

def dump_project(root, output_file='project_dump.txt', max_file_size=50_000):
    root = os.path.abspath(root)
    with open(output_file, 'w', encoding='utf-8') as out:
        for dirpath, dirnames, filenames in os.walk(root):
            # Prune skipped dirs in-place
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            dirnames.sort()

            for fname in sorted(filenames):
                ext = os.path.splitext(fname)[1].lower()
                if ext not in TEXT_EXTENSIONS:
                    continue

                filepath = os.path.join(dirpath, fname)
                relpath = os.path.relpath(filepath, root)

                if os.path.getsize(filepath) > max_file_size:
                    out.write(f"\n{'='*60}\n")
                    out.write(f"FILE: {relpath}  [SKIPPED - too large]\n")
                    out.write(f"{'='*60}\n")
                    continue

                try:
                    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                except Exception as e:
                    content = f"[ERROR reading file: {e}]"

                out.write(f"\n{'='*60}\n")
                out.write(f"FILE: {relpath}\n")
                out.write(f"{'='*60}\n")
                out.write(content)
                out.write('\n')

    print(f"Done → {output_file}")

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    output = sys.argv[2] if len(sys.argv) > 2 else 'project_dump.txt'
    dump_project(root, output)