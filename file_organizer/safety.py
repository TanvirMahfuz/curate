from pathlib import Path


def validate_safe_directory(root):
    home = Path.home().resolve()

    protected = [
        Path("/"),
        Path("/etc"),
        Path("/usr"),
        Path("/var"),
        Path("/boot"),
        Path("/bin"),
        Path("/sbin"),
        Path("/lib"),
        Path("/lib64"),
        Path("/opt"),
        Path("/proc"),
        Path("/sys"),
        Path("/dev"),
        Path("/run"),
        Path("/root"),
        Path("/snap"),
        Path("/srv"),
        home,
        home / ".config",
        home / ".local",
        home / ".cache",
        home / ".ssh",
        home / ".gnupg",
        home / ".docker",
    ]

    for path in protected:
        path = path.resolve()

        if root == path:
            raise ValueError(
                "Refusing to organize protected directory: " + str(root)
            )