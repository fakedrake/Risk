import json

class Board(object):
    """The board thet manages the game
    """

    def __init__(self, players, regions_file):
        """Initialize the board with a list of player objects and a file with the
        region grid.

        Arguments:
        - `players`:
        - `regions_file`:
        """
        self.players = players
        self.regions_file = regions_file
        self.continents, self.regions = self.parse_regions(regions_file)

    def parse_regions(self, regions_file):
        """Given a Regions file, parse the reguion grid.
        """
        regions = nx.Graph()
        continents = []
        with f as open(regions_file):
            data = json.loads(f.read())

            for cont_name, attrs in data.iteritems():
                continents.append( Continent(cont_name, json=attrs) )
                for region, neighbors in continents[-1].regions():
                    regions.add_region(region, neighbors)

        return continents, regions
