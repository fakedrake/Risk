from regions import Region


# TODO: allow it to start from somewhere in the middle
class Ring(object):
    """Everything you need to know about the ring."""

    def __init__(self, path):
        """Given a ring path and th current position.
        """
        self.path = path
        self.iter = iter(path)
        self.position = path[0]

    def move(self):
        """Move and return the (dice result or None, wether it moved). """
        roll = None
        if self.position.ring_roll:
            roll = randint(1,6)
            if roll <= self.position.ring_roll_base:
                return (roll, False)

        self.position = self.iter.next()
        return (roll, True)
