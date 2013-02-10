import networkx as nx

class Region(object):
    """A region on the map.
    """

    def __init__(self, name, troops=0, owner=None, ring_roll=False):
        """Set the name.
        """
        self.name = name
        self.troops = troops
        self.owner = owner
        self.ring_roll = ring_roll

    def __str__(self):
        return self.name

class Continent(object):
    """ A continent class.
    """

    def __init__(self, name, regions=[], bonus=0, json_dic=None):
        """Create a continent which is basically an collection of regions that
        gives some bonus. Regions are region names.
        """
        self.name = name

        if json_dic is not None:
            self.regions = json_dic['regions']
            self.bonus = json_dic['bonus']
        else:
            self.regions = regions
            self.bonus = bonus


    def regions(self):
        """Return a list of tuples of each region and it's neighbors."""


class Map(object):
    """ The map of regions, agnostic to all other gameplay elements.
    """

    def __init__(self):
        """ Initialize the map.
        """
        self.regions = {}
        self.net = nx.Graph()

    def add_region(self, region, connections=[]):
        """Add a region object to the map. Given a region object and the names of
        the adjacent regions.
        """
        self.regions[region.name] = region
        self.net.add_node(region.name)
        for c in connections:
            self.add_edge(region.name, c)

    def neighbors(self, region):
        """Return a list or neighboring region names. Works with region objects or
        strings.
        """
        try:
            name = region.name
        except AttributeError:
            name = region

        return self.net.neighbors(name)
