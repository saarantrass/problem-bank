from stanfordkarel import *

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

def move_2():
  move()
  move()

def move_3():
  move_2()
  move()

def main():
  move_2()
  turn_left()
  move()
  turn_left()
  move_2()
  pick_beeper()
  turn_around()
  move_2()
  turn_left()
  move_3()
  turn_right()
  move_3()
  pick_beeper()
  turn_around()
  move_3()
  move_2()
  pick_beeper()

if __name__ == "__main__":
  run_karel_program()