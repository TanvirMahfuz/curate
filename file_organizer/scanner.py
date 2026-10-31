
def scan_directory(root):
    files = []

    for entry in root.iterdir():
        if entry.is_symlink():
            continue

        if entry.is_file():
            files.append(entry)

    return files
