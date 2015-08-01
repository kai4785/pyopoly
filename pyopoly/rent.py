'''
rent.py

Can haz rent plz?
'''

from property import Property

class Rent(object):
    prop = None
    def __init__(self, *args, **kwargs):
        pass

class PropertyRent(Rent):
    base = 0
    homes = []
    def __init__(self, *args, **kwargs):
        super(PropertyRent, self).__init__(args, kwargs)
        self.base = kwargs['base']
        self.prop = kwargs['property']
        self.homes = kwargs['homes']
    def charge(self):
        pass

class UtilityRent(Rent):
    def charge(self):
        # Check to see if both utilities
        pass

class RailRoadRent(Rent):
    base = 0
    def charge(self):
        pass

# vim: ts=4:sw=4:expandtab
