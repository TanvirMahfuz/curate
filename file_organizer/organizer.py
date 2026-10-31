from fnmatch import fnmatch

from file_organizer.validator import validate_directory, validate_category
from file_organizer.safety import validate_safe_directory
from file_organizer.scanner import scan_directory
from file_organizer.categorizer import get_category
from file_organizer.destination import get_unique_destination
from file_organizer.mover import move_file
from file_organizer.reporter import print_report
from file_organizer.history import start_operation, record_move


def is_excluded(source, patterns):
    for pattern in patterns:
        if fnmatch(source.name, pattern):
            return True

    return False


def organize_directory(directory, apply=False,
                       selected_category=None, exclude_patterns=None):
    root = validate_directory(directory)
    validate_safe_directory(root)
    validate_category(selected_category)

    patterns = exclude_patterns or []
    reserved = set()
    plan = []
    skipped = 0

    for source in scan_directory(root):
        if is_excluded(source, patterns):
            skipped += 1
            continue

        category = get_category(source)

        if selected_category and category != selected_category:
            skipped += 1
            continue

        destination = root / category / source.name
        destination = get_unique_destination(destination, reserved)
        plan.append((source, destination))

    for source, destination in plan:
        print("[PLAN] " + str(source) + " -> " + str(destination))

    print("\nFiles to organize: " + str(len(plan)))

    if not apply:
        print("Preview only. Use --apply to move files.")
        print_report(0, skipped, 0)
        return 0, skipped, 0

    if not plan:
        print("Nothing to organize.")
        return 0, skipped, 0

    answer = input("Proceed with these moves? [y/N]: ").strip().lower()

    if answer not in ("y", "yes"):
        print("Operation cancelled.")
        return 0, skipped, 0

    start_operation()

    moved = 0
    errors = 0

    for source, destination in plan:
        if move_file(source, destination):
            record_move(source, destination)
            moved += 1
        else:
            errors += 1

    print_report(moved, skipped, errors)
    return moved, skipped, errors