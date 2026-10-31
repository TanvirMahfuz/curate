import json
import shutil
from pathlib import Path


HISTORY_FILE = (
    Path.home() / ".local" / "state" / "curate" / "history.json"
)


def load_history():
    if not HISTORY_FILE.exists():
        return []

    with HISTORY_FILE.open("r") as file:
        return json.load(file)


def save_history(history):
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    temporary = HISTORY_FILE.with_suffix(".tmp")

    with temporary.open("w") as file:
        json.dump(history, file, indent=4)

    temporary.replace(HISTORY_FILE)


def start_operation():
    history = load_history()
    history.append([])
    save_history(history)


def record_move(source, destination):
    history = load_history()

    if not history:
        history.append([])

    history[-1].append({
        "source": str(source),
        "destination": str(destination)
    })

    save_history(history)


def undo_last_operation():
    history = load_history()

    if not history or not history[-1]:
        print("Nothing to undo.")
        return

    answer = input(
        "Undo the last operation? [y/N]: "
    ).strip().lower()

    if answer not in ("y", "yes"):
        print("Undo cancelled.")
        return

    moves = history[-1]
    remaining = []

    for move in reversed(moves):
        source = Path(move["source"])
        destination = Path(move["destination"])

        try:
            if source.exists():
                raise FileExistsError(str(source))

            if not destination.exists():
                raise FileNotFoundError(str(destination))

            source.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(destination), str(source))

            print("[RESTORED] " + str(source))

        except OSError as error:
            print("[UNDO ERROR] " + str(error))
            remaining.append(move)

    history[-1] = list(reversed(remaining))

    if not history[-1]:
        history.pop()

    save_history(history)