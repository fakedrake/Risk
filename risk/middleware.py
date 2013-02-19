class MiddleWare(object):
    """
    """

    def __init__(self):
        """
	"""

        pass

    def get_region_cards(self, player):
        """
        """

        pass

    def clickable_regions(self, regions, override=True):
        """Makes the regiongs passed clickable. Overrides previous clickable
        regions by default.
        """

        pass

    def clicked_region(self):
        """Lets the player choose from the set of clickable regions. Returns
        region and right or left click. Conventionally, left click is
        affirmative, right is cancel etc. Returns None,None if player
        chooses to end phase.
        """

        pass

    def update_reinforcments(self, reinforcments):
        """ Update the number of available reinforcments in the gui.
        """

        pass
