from file_organizer.config import CATEGORIES, DEFAULT_CATEGORY


def get_category(filename):
    extension = filename.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return DEFAULT_CATEGORY