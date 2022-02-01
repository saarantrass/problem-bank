from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
  move()
  pick_beeper()
  move()
  turn_left()
  move()
  # --------
  # This section can be replaced by turn_right()
  turn_left()
  turn_left()
  turn_left()
  # ---------
  move()
  move()
  put_beeper()

if __name__ == "__main__":
  run_karel_program()