'''
property.py

Can haz howse?
'''

class Property(object):
    name = ""
    owner = None
    def __init__(self, *args, **kwargs):
        self.properties = args
        self.name = kwargs['name']
    def set_owner(self, owner):
        self.owner = owner ## TODO: This should turn into a Player object, not a string
    def __str__(self):
        return "%s (%s)" % (self.name,self.owner)
    def __repr__(self):
        return self.name

class PropertyGroup(object):
    properties = []
    name = ""
    def __init__(self, *args, **kwargs):
        self.properties = args
        self.name = kwargs['name']
    def all_owned(self, player):
        return len([p for p in self.properties if p.owner == player]) == len(self.properties)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
# vim: ts=4:sw=4:expandtab
