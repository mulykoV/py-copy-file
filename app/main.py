def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_name = parts[1]
    destination_name = parts[2]
    if parts[1] == parts[2]:
        return

    try:
        with open(source_name, "r") as source, \
                open(destination_name, "w") as destination:
            destination.write(source.read())
    except FileNotFoundError:
        return
