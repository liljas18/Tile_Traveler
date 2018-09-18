
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

def print_travel_options(Directions):
    return_str = "You can travel: "
    if "n" in Directions:
        return_str += "(N)orth"
    if "s" in Directions:
        return_str += "(S)outh"
    if "e" in Directions:
        return_str += "(E)ast"
    if "w" in Directions:
        return_str += "(W)est"
    print(return_str)

def promt_user_and_move(position, Directions):
    print_travel_options(Directions)
    direction = input("Direction: ")
    if not valid_direction(direction, Directions):
        print("Not a valid direction!")
        return position
    return move(position, direction)




