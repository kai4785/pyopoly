'''
property.py

I can haz howse?
'''

class LandException(Exception):
    pass

class Land(object):
    def __init__(self, name, price, *args):
        self.owner = None
        self.mortgaged = False
        self.pgroup = None
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
    def __init__(self, name, price, house_values, *args):
        super(Property, self).__init__(name, price, *args)
        self.houses = 0
        self.house_values = []
        self.house_values = house_values
    def charge_rent(self, player):
        if self.owner == player or self.mortgaged == True:
            rent = 0
        elif self.houses == 0 and self.pgroup.all_owned(self.owner):
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

class Railroad(Land):
    def __init__(self, name, price, *args):
        super(Railroad, self).__init__(name, price, *args)
    def charge_rent(self, player):
        rent = 0
        prop_owned = 0
        if self.owner == player or self.mortgaged == True:
            rent = 0
        else:
            prop_owned = self.pgroup.player_owned(self.owner)
            rent = 25 * ( 2**(prop_owned - 1) )
        return rent

class PropertyGroup(object):
    def __init__(self, name, *args):
        self.name = ""
        self.properties = []
        for arg in args:
            arg.pgroup = self
            self.properties.append(arg)
        self.name = name
    def player_owned(self, player):
        return len([p for p in self.properties if p.owner == player])
    def all_owned(self, player):
        return self.player_owned(player) == len(self.properties)
    def __str__(self):
        return "%s (%s)" % (self.name, self.properties)
    def __repr__(self):
        return str(self)
# vim: ts=4:sw=4:expandtab
