
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

def valid_direction(Input, Directions):
    return(Input.lower() in Directions)

def append_option(option, new_option):
    if len(option) > 0:
        return option + "or" + new_option
    return new_option

def print_travel_options(directions):
    return_str = "You can travel: "
    options = ""
    if "n" in directions:
        options = append_option (options, "(N)orth")
    if "s" in directions:
        options = append_option(options, "(S)outh")
    if "e" in directions:
        options = append_option(options, "(E)ast")
    if "w" in directions:
        options = append_option(options, "(W)est")
    print(f"{return_str}{options}.")

def promt_user_and_move(position, directions):
    print_travel_options(directions)
    direction = input("Direction: ")
    if not valid_direction(direction, directions):
        print("Not a valid direction!")
        return position
    return move(position, direction)

position = 11 


