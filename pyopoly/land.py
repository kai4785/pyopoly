'''
property.py

I can haz howse?
'''

from dice import Dice

class LandException(Exception):
    pass

class Land(object):
    def __init__(self, name, price, *args):
        self.owner = None
        self.mortgaged = False
        self.landgroup = None
        self.name = name
        self.price = price
    def is_owned():
        return not (owner == None)
    def mortgage():
        self.mortgaged = True
        return self.price / 2
    def set_owner(self, owner):
        self.owner = owner
    def unmortgage():
        self.mortgaged = False
    def __str__(self):
        return "%s (%s)" % (self.name,self.owner)
    def __repr__(self):
        return str(self)

class Property(Land):
    def __init__(self, name, price, *args, **kwargs):
        super(Property, self).__init__(name, price, *args)
        self.houses = 0
        self.house_values = kwargs['house_values']
    def charge_rent(self, player):
        if self.owner == player or self.mortgaged == True:
            rent = 0
        elif self.houses == 0 and self.landgroup.all_owned(self.owner):
            rent = self.house_values[0] * 2
        else:
            rent = self.house_values[self.houses]
        return rent
    def buy_house(self, count=1):
        if self.houses + count > 5:
            raise LandException("Limit 5 houses. %d already owned, %d requested to purchase" % (self.houses, count)) # TODO: Add custom "too many houses" exception
        if self.owner is None:
            raise LandException("There is no owner, can't buy a house.") # TODO: Add custom "no owner" exception
        self.houses += count
    def sell_house(self, count=1):
        if self.houses - count < 0:
            raise LandException("Cannot sell more houses than you own. %d owned, %d requested to sell" % (self.houses, count)) # TODO: Add custom "not enough houses" exception
        if self.owner == None:
            raise LandException("There is no owner, can't sell a house.") # TODO: Add custom "no owner" exception
        self.houses -= count

class Utility(Land):
    def __init__(self, name, price, *args):
        super(Utility, self).__init__(name, price, *args)
    def charge_rent(self, player):
        rent = 0
        prop_owned = 0
        prop_owned = self.landgroup.player_owned(self.owner)
        if self.owner == player or self.mortgaged == True:
            rent = 0
        else:
            # TODO: the die should be provided some other way
            self.owner.dice.roll()
            if prop_owned == 1:
                rent = (self.owner.dice.die1 + self.owner.dice.die2) * 4 # 4 * Dice
            if prop_owned == 2:
                rent = (self.owner.dice.die1 + self.owner.dice.die2) * 10 # 10 * Dice
        return rent

class Railroad(Land):
    def __init__(self, name, price, *args):
        super(Railroad, self).__init__(name, price, *args)
    def charge_rent(self, player):
        rent = 0
        prop_owned = self.landgroup.player_owned(self.owner)
        if self.owner == player or self.mortgaged == True:
            rent = 0
        else:
            rent = 25 * ( 2**(prop_owned - 1) )
        return rent

class LandGroup(object):
    def __init__(self, name, *args):
        self.name = ""
        self.lands = []
        for arg in args:
            arg.landgroup = self
            self.lands.append(arg)
        self.name = name
    def player_owned(self, player):
        return len([p for p in self.lands if p.owner == player])
    def all_owned(self, player):
        return self.player_owned(player) == len(self.lands)
    def __str__(self):
        return "%s (%s)" % (self.name, self.lands)
    def __repr__(self):
        return str(self)
    def __iter__(self):
        return iter(self.lands)
    def __len__(self):
        return len(self.lands)
# vim: ts=4:sw=4:expandtab
