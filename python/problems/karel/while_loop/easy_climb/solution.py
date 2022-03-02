from stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()


def step_up():
    put_beeper()
    turn_left()
    if front_is_clear():
        move()
        turn_right()


def put_beeper_and_climb():
    while front_is_clear():
        step_up()
        move()
    # extension
    if no_beepers_present():
        put_beeper()


def main():
    put_beeper_and_climb()

if __name__ == "__main__":
    run_karel_program("easy_climb")