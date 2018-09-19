
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

def promt_user_and_move(position, directions, print_options = True):
    if print_options:
        print_travel_options(directions)
    direction = input("Direction: ")
    if not valid_direction(direction, directions):
        print("Not a valid direction!")
        return promt_user_and_move(position, directions, False)
    return move(position, direction)

position = 11 

while position != 31:
    if position == 11:
        position = promt_user_and_move(position, "n")
    elif position == 12:
        position = promt_user_and_move(position, "nes")
    elif position == 13:
        position = promt_user_and_move(position, "es")
    elif position == 21:
        position = promt_user_and_move(position, "n")
    elif position == 22:
        position = promt_user_and_move(position, "sw")
    elif position == 23:
        position = promt_user_and_move(position, "we")
    elif position == 33:
        position = promt_user_and_move(position, "sw")
    elif position == 32:
        position = promt_user_and_move(position, "ns")
    else:
        print("How did you do that?")

print ("Victory!")



