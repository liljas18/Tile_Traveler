https://github.com/liljas18/Tile_Traveler.git
position = 11

while position != 31:
    if position == 11:
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction.lower() == "n":
           position +=1
        else:
            print("Not a valid direction!")

    elif position == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
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
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction.lower() == "s":
            position -= 1
        elif direction.lower() == "e":
            position +=10
        else:
            print("Not a valid direction!")
    
    elif position == 21:
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction.lower() == "n":
            position += 1
        else:
            print("Not a valid direction!")

    elif position == 22:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction.lower() == "w":
            position -= 10
        elif direction.lower() == "s":
            position -= 1
        else: 
            ("Not a valid direction!")
    elif position == 23:
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: ")
        if direction.lower() == "w":
            position -= 10
        elif direction.lower() == "e":
            position += 10
        else:
            print("Not a valid direction!")

    elif position == 33:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction.lower() == "w":
            position -= 10
        elif direction.lower() == "s":
            position -= 1
        else:
            print("Not a valid direction!")

    elif position == 32:
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ")
        if direction.lower() == "n":
            position += 1
        elif direction.lower() == "s":
            position -= 1
        else: print("Not a valid direction!")
    
    else: 
        print("How did you do that?")
print("Victory!")
    

        
