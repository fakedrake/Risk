from .gui import Gui
from .board import Board
from .player import Player
from .region import Region

class MainGame(object):
    """Contains all that was, is and will be during a game session
    """
    
    def __init__(self):
        """Creates all the needed objects for the game to run
        """

        # Some parameters are temporary for debugging
        self.players = [
            Player("Cpt Grinias", "red")
            Player("Mihalaras Karagiozaras", "blue")
            Player("Andrear", "black")
            ]
        self.gui = Gui("./LOTR_Risk_indexed_map.jpg")
        board = Board(self.players, "./resources/regions.txt", self.gui)
        
    def game_loop(self):
        """Cycle through players and call player_turn for each one of them until
        player quits or game is over
        """

        quit = False
        while not quit:
            for player in players:
                quit = self.player_turn(player)
                if quit:
                    break

    def player_turn(self, player):
        """Plays out a single player turn and returns True if the game is over or
        False otherwise.
        """

        
