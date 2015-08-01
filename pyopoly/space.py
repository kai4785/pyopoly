#!/usr/bin/python
'''
space.py

defines the space on a board

has an action - get chance card, pay rent, go to jail, etc...

Game needs an interface to talk to the Space
the space knows what MUST be done and what CAN be done with itself
action takes Player and Game

PropertySpace
CommunityChestSpace
ChanceSpace
GoSpace
JailSpace
GoToJailSpace
FreeParkingSpace

each space is going to have to tell the game what to do when a player lands on it
the game is going to start things off by rolling for player 1, move player 1 by roll
amount.  the move happens along Position which is a pre-defined and verbose setup
of each space.  it starts with GoSpace, then PropertySpace  (which happens to be mediterranean ave), 
then CommunityChestSpace, then PropertySpace (which happens to be baltic avenue), etc...

so when player1 gets moved to Space in Position, we'll need to know what to do

'''

class Space(object):
    
    def __init__(self):
        pass

    def action(self):
        pass

class PropertySpace(Space):
    prop = None

    def __init__(self, prop):
        self.prop = prop
        pass

    def getAction(self, *args, **kwargs):
        super(Space, self).__init__(args, kwargs)
        player = kwargs['player']
        game = kwargs['game']
        
        if player != prop.owner:
            if prop.is_owned:
                pass
                # Game.charge_rent(player, prop.get_rent())
            else:
                pass
                # Game.offer_property(player)


# vim: ts=4:sw=4:expandtab
