
def move(position, direction):
    if direction.lower() == "n":
        return position + 1
    elif direction.lower() == "s":
        return position - 1
    elif direction.lower() = "w":
        return position - 10
    elif direction.lower() == "e":
        return position + 10
    else:
        return position
        