"""This tests the battles."""

import os
import unittest
import random

from mock import patch

import risk

from risk.board import Board
from risk.player import Player

RESOURCES_DIR = os.path.dirname(risk.__file__)+"/../resources/"
PLAYERS = [("Chris", "red"), ("Filon", "blue"), ("Hitler", "green")]

REGION_OWNINGS = [
    [("A",5),
     ("B",6)],
    [("C", 10)],
    [("D",2),
     ("E",4)]]

def mock_randint_defend(self, x, y):
    """Attackers roll first so defenders should win with this."""
    for i in range(1,5):
        yield i

class TestBattle(unittest.TestCase):
    """ Test battles!
    """

    def setUp(self, players=PLAYERS, res_dir=RESOURCES_DIR, ownage=REGION_OWNINGS):
        self.b = Board(players, res_dir+"regions.json", res_dir+"ring.json", None)

        for emp,(pl, col) in zip(ownage, players):
            for reg, tr in emp:
                self.b.reinforce(reg,tr, pl)

    @patch('random.randint', mock_randint_defned)
    def test_battle_defend(self):
        self.b.attack("A","C")
        self.b.battle.set_troops(4,5)
        self.b.battle.roll()
