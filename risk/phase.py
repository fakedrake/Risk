class Phase(object):
    """
    """

    def __init__(self, player, middleware, board):
        """
	"""

        self.player = player
        self.middleware = middleware
        self.board = board


class ReinforcementPhase(Phase):
    """
    """

    def __init__(self, player, middleware, board):
        """
	"""

        super(ReinforcementPhase, self).__init__(player, middleware, board)
        self.r_buffer = {str(region):0 for region in self.player.regions()}
        self.reinforcments = 0

    def __call__(self):
        """
        """

        # TODO : check for continent bonus
        self.reinforcements = min(len(self.player.regions()) // 3, 3)
        self.middleware.can_trade_cards(player, self.card_bonus)

        self.middleware.clickable_regions(self.player.regions())

        region, action = self.middleware.clicked_region()
        while region is not None:
            if action == "right" and self.reinforcments > 0:
                self.r_buffer[region] += 1
                self.reinforcements -= 1
            if action == "left" and self.r_buffer[region] > 0:
                self.r_buffer[region] -= 1
                self.reinforcments += 1

            self.middleware.update_reinforcments(self.reinforcments)
            region, action = self.middleware.clicked_region()

    def card_bonus(self, cards):
        """Calculate the bonus from card combination and add it to self.bonus
        """
        # self.reinforcements += bonus
        # Undo card selectability
        pass

    def reinforce_regions(self, cards):
        """ Places reinforcments in the buffer.
        """

        pass

    def commit(self):
        """ Commits the reinforcments from the buffer to the board
        """

        pass


class AttackPhase(Phase):
    """
    """

    def __init__(self, player, middleware, board):
        """
	"""

        super(AttackPhase, self).__init__(player, middleware, board)

    def __call__(self):
        """
        """

        pass


class TacticalPhase(Phase):
    """
    """

    def __init__(self, player, middleware, board):
        """
	"""

        super(TacticalPhase, self).__init__()

    def __call__(self):
        """
        """

        pass
