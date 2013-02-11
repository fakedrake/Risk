"""This tests the ability to read resources."""

import os
import unittest

from risk.board import Board
from risk.player import Player

RESOURCES_DIR = os.dirname(module.__file__)+"/resources/"
NAMES = ["Chris", "Filon", "Hitler"]
COLORS = ["red", "blue", "green"]

class TestResources(unittest.TestCase):
    """Test resource inpu
    """

    def setUp(self, player_names=NAMES, colors=COLORS, res_dir=RESOURCES_DIR):
        """ Create a board and stuff.
        """
        players = [Player(n,c) for n,c in zip(player_names, colors)]
        self.b = Board(players, res_dir+"regions.json", res_dir+"ring.json", None)
