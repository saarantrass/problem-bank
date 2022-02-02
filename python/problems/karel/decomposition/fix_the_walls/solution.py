from stanfordkarel import *

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

def fix_hole():
  turn_right()
  move()
  put_beeper()
  turn_around()
  move()
  turn_right()

def move_2():
  move()
  move()

def move_3():
  move_2()
  move()

def main():

  move_2()
  fix_hole()
  move_3()
  fix_hole()
  move()

  turn_left()
  move_2()
  fix_hole()
  move_2()
  fix_hole()
  move()

  turn_left()
  move_2()
  fix_hole()
  move_2()
  fix_hole()
  move()

  turn_left()
  move_2()
  fix_hole()
  move()


if __name__ == "__main__":
  run_karel_program('fix_the_walls')
