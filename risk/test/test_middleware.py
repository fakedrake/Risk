import os
import unittest
import risk


RESOURCES_DIR = os.path.dirname(risk.__file__)+"/../resources/"
PLAYERS = [("Chris", "Red"),
           ("Filon", "Blue"),
           ("Hitler", "Black")]

class TestPhases(unittest.TestCase):
    """ Test the phases of the game.
    """

    def setUp(self, rdir=RESOURCES_DIR, players=PLAYERSx):
        """ Setup a game.
        """
        # setup the regions and the ring but no GUI
        self.game = risk.Game(rdir+"regions.json", rdir+"ring.json", players, None)

        self.game.distribute_regions(json=rdir+"region_distribution.json")

    def test_reinforcements(self):
        """ Test the reingorcement phase.
        """
        self.assertEquals(str(self.game.current_phase().player()), "Chris")

        # Chris has the entire BB continent and also 3 regions
        self.assertEquals(self.game.current_phase().get_reinforcements(), 7)
