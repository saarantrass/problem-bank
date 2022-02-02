from stanfordkarel import *

def main():

  for i in range(3):
    move()
    move()
    move()
    pick_beeper()
    turn_left()

if __name__ == "__main__":
    run_karel_program("corners_of_beepers")