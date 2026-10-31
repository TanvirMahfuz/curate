
def get_unique_destination(destination, reserved):
    if not destination.exists() and destination not in reserved:
        reserved.add(destination)
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while True:
        candidate = parent / (stem + "_" + str(counter) + suffix)

        if not candidate.exists() and candidate not in reserved:
            reserved.add(candidate)
            return candidate

        counter += 1
