class Game(object):
    """ This is the phase manager. It is the spearhead interfaces of the library
    """

    def __init__(self, json_regions, json_ring, players, gui):
        """Initialize the game."""
        if isinstance(players[0], Player):
            player_objects = players
        else:
            player_objects = [Player(*p) for p in players]

        self.board = Board(player_object, json_regions, json_ring, gui)

        # Find a nice way to generate specific phases.
        # Also initialize the first phase

    def current_phase(self):
        """ Get the current phase.
        """
        pass

    def end_phase(self):
        """ Run the needed hooks and initializations to advance to the next phase.
        """
        pass
