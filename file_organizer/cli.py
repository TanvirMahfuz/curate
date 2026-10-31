import argparse

from file_organizer.config import CATEGORIES
from file_organizer.organizer import organize_directory
from file_organizer.history import undo_last_operation


def main():
    parser = argparse.ArgumentParser(
        description="Organize files safely."
    )

    parser.add_argument(
        "directory",
        nargs="?",
        help="Directory to organize"
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files"
    )

    parser.add_argument(
        "--undo",
        action="store_true",
        help="Undo the last operation"
    )

    parser.add_argument(
        "--category",
        choices=list(CATEGORIES.keys()) + ["others"],
        help="Organize only this category"
    )

    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Exclude files matching a pattern"
    )

    args = parser.parse_args()

    if args.undo:
        if args.directory or args.apply or args.category or args.exclude:
            parser.error("--undo cannot be combined with other options")

        undo_last_operation()
        return

    if not args.directory:
        parser.error("directory is required")

    try:
        organize_directory(
            args.directory,
            apply=args.apply,
            selected_category=args.category,
            exclude_patterns=args.exclude
        )
    except (FileNotFoundError, NotADirectoryError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()