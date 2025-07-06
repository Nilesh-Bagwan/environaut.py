import sys
from pathlib import Path

def is_in_virtualenv() -> bool:
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

def is_file_nonempty(path: Path) -> bool:
    return path.exists() and path.stat().st_size > 0
