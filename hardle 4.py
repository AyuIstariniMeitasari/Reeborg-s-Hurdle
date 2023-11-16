def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def lompat_dinding():
    turn_left()
    count_wall=0
    while wall_on_right():
        count_wall+=1
        move()
    turn_right()
    move()
    turn_right()
    while count_wall>0:
        move()
        count_wall-=1
    turn_left()

while not at_goal():
    if wall_in_front():
        lompat_dinding()
    elif front_is_clear():
        move()
