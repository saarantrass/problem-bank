from stanfordkarel import *

def main():

  for i in range(63):
    move()
    if beepers_present():
      pick_beeper()
    if front_is_blocked():
      turn_left()


if __name__ == "__main__":
    run_karel_program("the_spiral_maze")