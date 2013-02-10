class Player(object):
    """Player object. A player is the interface with the board. From here we
    will be requesting the board for each move.
    """

    def __init__(self, name, color):
        """ Create a player given a name and a color.
        """
        self.name = name
        self.color = color
