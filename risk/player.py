class Player(object):
    """Player object. A player is the interface with the board. From here we
    will be requesting the board for each move.
    """

    def __init__(self, name, color, board, reinforcements=0):
        """ Create a player given a name and a color.
        """
        self.name = name
        self.color = color
        self.board = board

        self.reinforcements = reinforcements

    def regions(self):
        """Return the player's regions as objects."""
        return self.board.regions(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Player object name: \"%s\" color: \"%s\">" % (self.name, self.color)
