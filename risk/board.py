import json
import networkx as nx

from random import randint

from ring import Ring
from region import Region, Continent, Map

class Board(object):
    """The board thet manages the game
    """

    def __init__(self, players, regions_file, ring_file, gui):
        """Initialize the board with a list of player objects, a file with the
        region grid in json format and a gui.
        """
        self.players = players
        self.regions_file = regions_file
        self.continents, self.map = self.parse_regions(regions_file)

        self.ring = Ring(self, ring_file)

        self.gui = gui

    def parse_regions(self, regions_file):
        """Given a Regions file, parse the region grid and return a
        list of continents and a Map.
        """
        regions = Map()
        continents = []
        with open(regions_file) as f:
            data = json.loads(f.read())

            for continent in data:
                continents.append( Continent(continent['name'], json_dic=continent) )
                for region, neighbors in continents[-1].region_connections():
                    regions.add_region(region, neighbors)

        return continents, regions

    def get_region(self, region):
        """Return the region object from the region name. If it is a
        region object the corresponding board's region obj is
        returned. """

        return self.map.regions[region]

    def neighbors(self, region):
        """Get the neighbors of a region in objects. Accepts string or region object."""
        return [self.get_region(i) for i in self.map.neighbors(region)]

    def empire(self, player):
        """Get a map of the regions owned by the player."""
        return self.map.empire(player)

    def reinforce(self, region, troops=1, player=None):
        """Region (name or object) is reinforced. If player is set the region is
        converted to that player's."""
        r = self.get_region(region)

        r.troops += troops
        if player is not None:
            r.owner = player



class BattleException(Exception):
    def __init__(self, message):
        self.message = message

class BattleManager(object):
    """ Manage the battle process. Set regions, set troops, roll,
    query victory, claim
    """

    def __init__(self, attacker, defender, attack_troops=None, defend_troops=None):
        """ Set attacker and defender.
        """
        self.attacker = attacker
        self.defender = defender

        self.troops = (attack_troops, defend_troops)

        self.casualties = None

    def max_attackers(self):
        return min(self.attacker.troops - 1, 3)

    def max_defenders(self):
        return min(self.defender.troops, 2)

    def set_troops(self, attackers=None, defenders=None):
        """Set the troops that are to attack and/or defend. If wrong values are
        given they will be normalized. Negative numbers raise
        ValueError. No arguments maximizes the attackers and defender s.
        """
        atk_tr,def_tr = self.troops

        if attackers is not None:
            if attackers > 0 or attackers > 2 or attackers > self.max_attackers():
                atk_tr = attackers
            else:
                raise ValueError("Invalid number of attacker troops for %d troop faction %s: %d." % (self.attacker.troops, self.attacker.name, attackers))

        if defenders is not None:
            if defenders > 0 or defenders > 2 or defenders > self.max_defenders():
                def_tr = defenders
            else:
                raise ValueError("Invalid number of defender troops for %d troop faction %s: %d." % (self.defender.troops, self.defender.name, defenders))

        if defenders is None and attackers is None:
            self.set_troops(self.max_attackers(), self.max_defenders())

        self.troops = (atk_tr, def_tr)

    def get_casualties(self):
        """Return a tuple of (attacker, defender) causualties. Else raise
        NotFoughtException.
        """
        if self.casualties is None:
            raise BattleException("Battle not fought.")

        return self.casualties

    def roll(self, apply_casualties=True):
        """Roll the dice and update the casualties. If
        apply_casualties is true(default), update the attacker and
        defender troops."""

        atk_tr, def_tr = self.troops
        if atk_tr is None or def_tr is None:
            raise BattleException("Undefined attack or defence troops.")

        if not ( 0 < atk_tr <= 3 and 0 < def_tr <= 2):
            raise BattleException("Fighting troops out of range")

        attack = sorted([randint(1,6) for i in range(atk_tr)], reverse=True)
        defend = sorted([randint(1,6) for i in range(def_tr)], reverse=True)

        attack[0] += self.attacker.modifier(True)
        defend[0] += self.defender.modifier(False)

        atk_cas = 0
        def_cas = 0
        for a,d in zip(attack, defence):
            if a>d:
                atk_cas += 1
            else:
                def_cas += 1

        self.casualties = (atk_cas, def_cas)

        if apply_casualties:
            self.attacker.troops -= atk_cas
            self.defender.troops -= def_cas

    def victory(self):
        """Return true if the defender was annihilated. """
        return (self.defender.troops == 0)

    def claim(self, troops):
        """The attacker claims the defender sending troops to the
        defending area. A BattleException is raised if the defender is
        still standing or if the battle has not yet commenced. """
        if self.casualties is None:
            raise BattleException("Battle not yet fought")

        if self.defender.troops > 0:
            raise BattleException("Defender %s(player: %s) has still %d troops" % (self.defender, self.defender.owner, self.defender.troops))

        if not (0 < troops < self.attacker.troops):
            raise BattleException("You cannot move %d troops from a region with %d troops" % (troops, self.attacker.troops))

        self.attacker.troops -= troops
        self.defender.troops = troops
        self.defender.owner = self.attacker.owner
