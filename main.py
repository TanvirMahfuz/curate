import argparse
import sys

from file_organizer.organizer import organize_directory
from file_organizer.config import CATEGORIES


def main():
    parser = argparse.ArgumentParser(
        description="Organize files into categorized directories."
    )

    parser.add_argument(
        "directory",
        help="Directory to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    parser.add_argument(
        "--category",
        choices=list(CATEGORIES.keys()) + ["others"],
        help="Organize only a specific category"
    )

    args = parser.parse_args()

    try:
        organize_directory(
            args.directory,
            dry_run=args.dry_run,
            selected_category=args.category
        )
    except (OSError, ValueError) as error:
        print("Error: " + str(error), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()