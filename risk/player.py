class Player(object):
    """Player object. A player is the interface with the board. From here we
    will be requesting the board for each move.
    """

    def __init__(self, name, color, leaders=[], reinforcements=0, region_cards=[]):
        """ Create a player given a name and a color.
        """
        
        self.name = name
        self.color = color
        self.leaders = leaders
        self.region_cards = region_cards

        self.reinforcements = reinforcements

    def leader_in(self, region):
        """Return true if the player has a leader in the given
        region.
        """
        
        for l in self.leaders:
            if l == region:
                return True
        return False

    def kill_leader(self, region):
        self.leaders.remove(region)

    def spawn_leader(self, region):
        self.leaders.append(region)

    def draw_card(self, deck):
        """Draw a single card from passed deck.
        """

        self.region_cards.append(deck.draw())
        

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Player object name: \"%s\" color: \"%s\">" % (self.name, self.color)


def playerFactory(player):
    if isinstance(player, Player):
        return player

    return Player(*player)
