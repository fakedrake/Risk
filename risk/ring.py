from random import randint

from regions import Region


# TODO: allow it to start from somewhere in the middle
class Ring(object):
    """Everything you need to know about the ring."""

    def __init__(self, board, path_file=None, path=None):
        """Given a ring path and th current position.
        """
        self.path = path
        if path is None and path_file is not None:
            self.path = self.parse(path_file, board)

        self.iter = iter(path)
        self.position, self.roll_base = self.iter.next()

    def parse(self, path_file, board):
        """Parse the path file. The file is a list of dicts with
        'name' and 'base'. Base is -1 if there is a fee pass.
        """
        with f as open(path_file):
            data = json.loads(f.read())

            ret = []
            for i in data:
                ret.append((board.get_region(i["name"]), i["base"]))



    def move(self, force=False):
        """Move and return the (dice result or None, wether it moved). """
        roll = None
        if self.roll_base > -1 and not force:
            roll = randint(1,6)
            if roll <= :
                return (roll, False)

        self.position, self.roll_base = self.iter.next()
        return (roll, True)
