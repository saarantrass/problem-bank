from stanfordkarel import *


def main():

  for i in range(3):
    move()
    move()
    move()
    for j in range(7):
      pick_beeper()
    turn_left()

if __name__ == "__main__":
    run_karel_program("corners_of_piles")