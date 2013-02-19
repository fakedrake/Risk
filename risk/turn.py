class TurnManager(object):
    """Creates turns and cycles through them. Checks end of game
    conditions.
    """

    def __init__(self, middleware, board):
        """
	"""
        self.middleware = middleware
        self.board = board
        self.turns = []

    def get_turn(self, index):
        """Return turn after index no of turns. Creates the turn and all
        previous ones if it doesn't exist
        """

        while index <= len(self.turns):
            self.create_turn()

        return self.turns[index]

    @property
    def current_turn(self):
        """ Returns the current turn
        """
        return self.get_turn(0)

    @property
    def players(self):
        """ Player list in the order the play
        """
        return self.board.players

    def create_turn(self):
        self.turns.append(Turn(self.next_player(), self.middleware, self.board))

    def next_player(self, player=None):
        """
        """
        if player is None:
            player = self.turns[-1].player

        return self.players[(self.players.index(player)+1) % len(self.players)]

    def run_turn(self):
        pass


class Turn(object):
    """ A single turn
    """

    def __init__(self, player, middleware, board):
        """
        """

        self.player = player
        self.middleware = middleware
        self.board = board
        self.phases = [
            ReinforcementPhase(),
            AttackPhase(),
            TacticalPhase()
        ]

    def current_phase(self):
        """ Returns the current phase. Returns None if there are no phases.
        """

        if not self.phases:
            return None
        else:
            return self.phases[0]

    def __call__(self):
        """ Runs through all the phases
        """

        while self.phases:
            self.current_phase()()
            self.phases.pop(0)
