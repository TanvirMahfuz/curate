
from pathlib import Path

from file_organizer.config import CATEGORIES


def validate_directory(directory):
    root = Path(directory).expanduser().resolve()

    if not root.exists():
        raise FileNotFoundError("Directory does not exist: " + str(root))

    if not root.is_dir():
        raise NotADirectoryError(str(root))

    return root


def validate_category(category):
    categories = set(CATEGORIES.keys()) | {"others"}

    if category and category not in categories:
        raise ValueError("Unknown category: " + category)
