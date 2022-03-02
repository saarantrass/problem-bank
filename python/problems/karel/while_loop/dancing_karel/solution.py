from stanfordkarel import *

def twist_karel():
    turn_left()
    while right_is_clear():
        turn_left()


def dance_karel():
    while front_is_clear():
        move()
        twist_karel()


def main():
    dance_karel()

if __name__ == "__main__":
    run_karel_program("dancing_karel")