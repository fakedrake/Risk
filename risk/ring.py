import json

from random import randint

from region import Region


# TODO: allow it to start from somewhere in the middle
class Ring(object):
    """Everything you need to know about the ring."""

    def __init__(self, board, path_file=None, path=None):
        """Given a ring path and th current position.
        """
        self.path = path
        if path is None and path_file is not None:
            self.path = self.parse(path_file, board)

        self.iter = iter(self.path)
        self.position, self.roll_base = self.iter.next()

    def parse(self, fn, board):
        """Return a path of regions from a json list file."""
        with open(fn) as f:
            return [(board.get_region(i['name']), i['base']) for i in json.loads(f.read())]




    def move(self, force=False):
        """Move and return the (dice result or None, wether it moved). """
        roll = None
        if self.roll_base > -1 and not force:
            roll = randint(1,6)
            if roll <= self.roll_base:
                return (roll, False)

        self.position, self.roll_base = self.iter.next()
        return (roll, True)
