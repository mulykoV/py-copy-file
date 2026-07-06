import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3 or parts[0] != "cp":
        return

    if parts[1] == parts[2]:
        return
    old_file = parts[1]
    new_file = parts[2]
    if not os.path.exists(old_file):
        return

    with open(old_file, "r") as source, open(new_file, "w") as destination:
        destination.write(source.read())
