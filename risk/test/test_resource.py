"""This tests the ability to read resources."""

import os
import unittest
import risk

from risk.board import Board
from risk.player import Player

RESOURCES_DIR = os.path.dirname(risk.__file__)+"/../resources/"
NAMES = ["Chris", "Filon", "Hitler"]
COLORS = ["red", "blue", "green"]

REGION_OWNINGS = [["A","B"], ["C"], ["D","E"]]

class TestResources(unittest.TestCase):
    """Test resource inpu
    """

    def setUp(self, player_names=NAMES, colors=COLORS, res_dir=RESOURCES_DIR, ownage=REGION_OWNINGS):
        """ Create a board and stuff.
        """
        players = [Player(n,c) for n,c in zip(player_names, colors)]
        self.b = Board(players, res_dir+"regions.json", res_dir+"ring.json", None)

        for i,p in enumerate(ownage):
            for r in p:
                self.b.reinforce(r, player=players[i])

    def test_region_net(self):
        """ Test region connections.
        """
        A_neighbors = sorted([self.b.get_region(i) for i in ["C", "D", "E"]])

        self.assertEquals(sorted(self.b.neighbors("A")), A_neighbors)

    def test_player(self):
        """ Test that a player actually owns what he sais he does. """
        self.assertEquals( sorted(self.b.empire(self.b.players[0]).region_list()),
                           sorted(self.b.get_region(i) for i in ["A", "B"]))
