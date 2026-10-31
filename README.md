# Curate

**Curate** is a lightweight command-line file organizer built with Python. It organizes files into category-based folders according to their extensions, helping keep directories clean and manageable.

It uses Python's standard library, so no third-party runtime dependencies are required.

## Features

- **Automatic organization:** Categorizes files based on their extensions.
- **Non-recursive scanning:** Processes only files directly inside the specified directory.
- **Safe preview:** Shows planned changes without moving anything by default.
- **Explicit execution:** Requires `--apply` to perform file movements.
- **Confirmation prompt:** Asks for confirmation before moving files.
- **No overwrites:** Generates unique filenames using suffixes such as `_1`, `_2`, etc.
- **Category filtering:** Organizes only a selected category.
- **Exclude patterns:** Skips files matching specified patterns.
- **Undo support:** Keeps a history of file movements so the last operation can be reversed.
- **Protected directories:** Refuses to organize designated sensitive system and application directories.
- **No third-party dependencies:** Built using Python's standard library.

## Requirements

- Python 3.8 or later
- Linux, macOS, or Windows
- pipx (recommended for installation)

## Installation

### Install using pipx

Install pipx if you don't already have it:

```bash
sudo apt install pipx
```

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/curate.git
cd curate
```

Install Curate:

```bash
pipx install .
```

After installation, the `curate` command will be available in your terminal.

## Usage

### Preview organization

By default, Curate runs in preview mode. It displays the files that would be moved without changing anything.

```bash
curate ~/Downloads
```

### Apply changes

To actually organize files, use `--apply`:

```bash
curate ~/Downloads --apply
```

Curate displays the planned changes and asks for confirmation before moving files.

### Organize a specific category

Use `--category` to organize only files belonging to a particular category.

```bash
curate ~/Downloads --category pdfs
```

Apply the changes:

```bash
curate ~/Downloads --category pdfs --apply
```

### Exclude files

Use `--exclude` to skip files matching a pattern.

```bash
curate ~/Downloads --exclude "*.log"
```

Multiple exclusion patterns are supported:

```bash
curate ~/Downloads --exclude "*.log" --exclude "*.tmp"
```

Exclusion patterns apply only to the current execution. They are not permanently saved.

### Undo the last operation

Curate maintains a history of successful file movements.

```bash
curate --undo
```

It asks for confirmation before restoring files to their original locations.

## How File Organization Works

Curate identifies files based on their extensions and places them into corresponding category folders.

For example:

**Before:**

```text
Downloads/
├── report.pdf
├── notes.txt
├── photo.jpg
├── spreadsheet.xlsx
└── archive.zip
```

**After:**

```text
Downloads/
├── pdfs/
│   └── report.pdf
├── documents/
│   └── notes.txt
├── images/
│   └── photo.jpg
├── spreadsheets/
│   └── spreadsheet.xlsx
└── archives/
    └── archive.zip
```

The exact category names depend on the extension mappings configured in Curate.

## History Storage

Curate stores its operation history locally:

```text
~/.local/state/curate/history.json
```

The history file and its parent directories are created automatically when an operation is executed.

## Project Structure

```text
file-organizer/
├── file_organizer/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── categorizer.py
│   ├── validator.py
│   ├── scanner.py
│   ├── destination.py
│   ├── mover.py
│   ├── reporter.py
│   ├── organizer.py
│   ├── safety.py
│   └── history.py
├── tests/
│   └── test_organizer.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Development

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/curate.git
cd curate
```

Run the application during development:

```bash
python -m file_organizer ~/Downloads
```

Run tests:

```bash
python -m unittest discover -s tests
```

Reinstall the CLI after making changes:

```bash
pipx install . --force
```

## Safety Notes

- Curate does not recursively scan subdirectories.
- Directories and symbolic links are skipped.
- Files are not moved unless `--apply` is specified.
- Existing destination files are not intentionally overwritten.
- Always review the preview before applying changes.
- Undo relies on the saved movement history being available.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.