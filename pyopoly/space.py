#!/usr/bin/python
'''
space.py

defines the space on a board

has an action - get chance card, pay rent, go to jail, etc...

Game offloads responsibility of what to do on each Space to Space.

Game says 'ok, space, here is everything you need to make it happen because i know everything about you.  make it happen'

'''

from polyopoly_property import Land
from game import Game

class Space(object):
    def __init__(self):
        pass

class LandSpace(Space):
    def __init__(self):
        pass

    def getAction(self, *args, **kwargs):
        game = kwargs['game']
        player = kwargs['player']
        banker = kwargs['banker']
        land = kwargs['land']
        
        if player != prop.owner:
            if land.is_owned():
                banker.charge_rent(player, land)
            else:
                game.offer_land(player, land)

class GoSpace(Space):
    def __init__(self):
        pass
    
    def getAction(self, *args, **kwargs):
        player = kwargs['player']
        game = kwargs['game']

        banker.give_money(player, 200)



class     

# vim: ts=4:sw=4:expandtab
