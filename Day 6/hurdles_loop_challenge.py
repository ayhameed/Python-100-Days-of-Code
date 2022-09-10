#from angela's 30 days of code
#my solution to the hurdles loop challenge
#For educational purposes only

def move_up():
    move()
    turn_left()
    move()
move_up()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_right()

def move_down():
    move()
    turn_right()
    move()
    
def move_down_down():
    move_down()
    turn_left()
    move_up()
    turn_right()
    move_down()
move_down_down()

def bottom_up():
    turn_left()
    move()
    turn_left()
    move()
    turn_right()
bottom_up()

move_down_down()
bottom_up()
move_down_down()