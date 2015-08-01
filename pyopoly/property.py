'''
property.py

Can haz howse?
'''

class Land(object):
    owner = None
    price = 0
    mortgaged = False
    def __init__(self, name, price, *args):
        self.name = name
        self.price = price
    def is_owned():
        return not (owner == None)
    def mortgage():
        self.mortgaged = True
        return self.price / 2
    def unmortgage():
        self.mortgaged = False
    def __str__(self):
        return "%s (%s)" % (self.name,self.owner)
    def __repr__(self):
        return str(self)

class Property(Land):
    name = ""
    owner = None
    homes = 0
    home_values = []
    def __init__(self, name, price, home_values, *args):
        super(Property, self).__init__(name, price, *args)
        self.home_values = home_values
    def set_owner(self, owner):
        self.owner = owner
    def charge_rent(self, player):
        if self.owner == player or self.mortgaged == True:
            return 0
        rent = self.home_values[self.homes]
        return rent
    def buy_home(self, count=1):
        if self.homes == 5:
            raise # TODO: Add custom "too many homes" exception
        if self.owner == None:
            raise # TODO: Add custom "no owner" exception
        self.homes += 1
    def sell_home(self, count=1):
        if self.homes == 0:
            raise # TODO: Add custom "not enough homes" exception
        if self.owner == None:
            raise # TODO: Add custom "no owner" exception
        self.homes -= 1

class Utility(Land):
    def __init__(self, name, price, *args):
        super(Utility, self).__init__(name, price, *args)

class Railroad(Land):
    def __init__(self, name, price, *args):
        super(Railroad, self).__init__(name, price, *args)

class PropertyGroup(object):
    properties = []
    name = ""
    def __init__(self, name, *args):
        self.properties = args
        self.name = name
    def all_owned(self, player):
        return len([p for p in self.properties if p.owner == player]) == len(self.properties)
    def __str__(self):
        return "%s (%s)" % (self.name, self.properties)
    def __repr__(self):
        return str(self)
# vim: ts=4:sw=4:expandtab
