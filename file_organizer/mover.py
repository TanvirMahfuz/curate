
import shutil


def move_file(source, destination, dry_run=False):
    try:
        if dry_run:
            print("[DRY RUN] " + str(source) + " -> " + str(destination))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            print("[MOVED] " + str(source) + " -> " + str(destination))

        return True

    except OSError as error:
        print("[ERROR] " + str(source) + ": " + str(error))
        return False
