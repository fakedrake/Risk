class Player(object):
    """Player object. A player is the interface with the board. From here we
    will be requesting the board for each move.
    """

    def __init__(self, name, color, leaders=[], reinforcements=0):
        """ Create a player given a name and a color.
        """
        self.name = name
        self.color = color
        self.leaders = leaders

        self.reinforcements = reinforcements

    def leader_in(self, region):
        """Return true if the player has a leader in the given
        region."""
        for l in self.leaders:
            if l == region:
                return True
        return False

    def kill_leader(self, region):
        self.leaders.remove(region)

    def spawn_leader(self, region):
        self.leaders.append(region)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Player object name: \"%s\" color: \"%s\">" % (self.name, self.color)
