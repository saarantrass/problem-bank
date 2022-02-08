from stanfordkarel import *


def main():

  for i in range(7):
    move()
    if beepers_present():
      pick_beeper()
    else:
      put_beeper()


if __name__ == "__main__":
    run_karel_program("flip_beepers")