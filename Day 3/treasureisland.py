#write a program using flowchart here : https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Would you like to go Left and Right?")
direction.lower()
if direction == "right" or direction == "":
    print("Fall into a hole.")
    print("Gamer Over.")
elif direction == "left":
    swim_or_wait = input("Would you be swiming or wait?")
    swim_or_wait.lower()
    if swim_or_wait == "swim" or swim_or_wait == "":
        print("Attacked by trout.")
        print("Game Over.")
    elif swim_or_wait == "wait":
        door = input("Which door? Red or Blue?")
        door.lower()
        if door == "blue":
            print("Eaten by beasts.")
            print("Game Over.")
        elif door == "red":
            print("Burned by Fire.")
            print("Game Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")