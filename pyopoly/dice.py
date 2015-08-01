#!/usr/bin/python
'''
dice.py

will have two actual dice numbers (for doubles!)

actions:
  roll

returns:
  random number, 1 through 6 for each dice
'''

import random

class Dice(object):
    die1 = 0
    die2 = 0
    snake_eyes = False
    doubles = False

    def __init__(self):
        pass

    def roll(self):
        self.die1 = random.randrange(1, 6)
        self.die2 = random.randrange(1, 6)
        if self.die1 == self.die2:
            self.doubles = True
            if self.die1 == 1:
                self.snake_eyes = True
        return

    def clear(self):
        self.die1 = 0
        self.die2 = 0
        self.snake_eyes = False
        self.doubles = False

# vim: ts=4:sw=4:expandtab
