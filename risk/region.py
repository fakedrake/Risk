import networkx as nx

class Region(object):
    """A region on the map.
    """

    def __init__(self, name, stronghold=False, troops=0, owner=None):
        """Set the name.
        """
        self.name = name
        self.troops = troops
        self.owner = owner
        self.stronghold = stronghold

    def modifier(self, attacking):
        """Get the modifier of the highest die given wether it is
        attacking or defending."""
        ret = 0
        if self.owner.leader_in(self):
            ret += 1

        if not attacking and self.stronghold:
            ret += 1

        return ret

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


    def region_connections(self):
        """Return a list of tuples of each region object and it's
        neighbors' names."""
        ret = []
        for r in regions:
            stronghold  = False

            if r['stronghold'] == "true":
                stronghold = True

            ret.append((Region(r["name"], stronghold=stronghold), r["neighbors"]))

        return ret


class Map(object):
    """ The map of regions, agnostic to all other gameplay elements.
    """

    def __init__(self, regions={}, net=nx.Graph()):
        """ Initialize the map given a map of region names to region
        objects and a network of region names. Note that the region
        dict may have more regions that the graph but not less.
        """
        self.regions = regions
        self.net = net

    def add_region(self, region, connections=[]):
        """Add a region object to the map. Given a region object and
        the names of the adjacent regions.
        """
        self.regions[region.name] = region
        self.net.add_node(region.name)
        for c in connections:
            self.add_edge(region.name, c)

    def neighbors(self, region):
        """Return a list or neighboring region names. Works with
        region objects or strings.
        """
        try:
            name = region.name
        except AttributeError:
            name = region

        return self.net.neighbors(name)

    def empire(self, player):
        """Return a graph with a player's empire."""
        region_names = self.net.subgraph([i.name for i in player.regions()])

        return Map(region_names, self.regions)
