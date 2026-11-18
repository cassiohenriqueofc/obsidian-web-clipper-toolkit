"""Shared project paths; standard library only."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {'.git', 'local-only', 'private', 'secrets', 'dist', '__pycache__', '.obsidian', 'test-results', 'playwright-report'}

def project_files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and not any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts)
                  and p.suffix != '.pyc' and p.name not in {'.DS_Store', 'Thumbs.db'})
