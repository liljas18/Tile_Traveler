
position = 11

while position != 31:
    if position == 11:
       print("You can travel: (N)orth.")
       direction = Input("Direction: ")
       if direction.lower() == "n":
           position +=1
        else 
            print("Not a valid direction!")

    elif position == 12:
        print("You can travel: (N)orth, (S)outh or (E)ast")
        direction = input("Direction: ")
        if direction.lower() == "n":
            position += 1
        elif direction.lower() == "e":
            position += 10
        elif direction.lower() == "s":
            position -= 1
        else:
            print("Not a valid direction!")

    elif position == 13:
        print("You can travel: (S)outh or (E)ast")
        direction = input("Direction: ")
        if direction.lower() == "s":
            position -= 1
        elif direction.lower() == "e":
            position +=10
        else:
            print("Not a valid direction!")
    
    elif position == 21:
        print("You can travel (N)orth")
        direction = input("Direction: ")
        if direction.lower() == "n":
            position += 1
        else:
            print("Not a valid direction!")
    
        