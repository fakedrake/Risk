import random
import json
import player

class RegionDeck(object):
    """A deck of region cards
    """

    def __init__(self):
        """
        """
        pass

    def read_file(self,f):
        """Read cards from json file.
        """
        
        with open(f,'r') as d:
            json_inp = json.loads(d.read())
        return [RegionCard(**c) for c in json_inp]

    def shuffle(self):
        """Shuffle the deck in place
        """
        random.shuffle(self.cards)

    def draw(self):
        """Draw a single card from the deck and return it.
        """

        if not self.cards:
            self.cards = self.discard_pile
            self.discard_pile = []
            self.shuffle()
        return self.cards.pop(0)
    
class RegionCard(object):
    """A single region card
    """
    
    def __init__(self, region, kind):
        """Region may be None and kind may be '*'.
        """
        self.region = region
        self.kind = kind

    def is_wild(self):
        """Returns True if card is wildcard, False otherwise.
        """
        if self.kind == "*":
            return True
        else:
            return False

if __name__=="__main__":        
    deck = Deck()
    cards = deck.read_file('RiskCards.txt')
    deck.shuffle(cards)
    deck.write(cards)
    print cards            
    #card = deck.pick()
    #print card
    #players = int(raw_input("How many players?\n"))
    playerc1=[]
    playerc2=[]
    playerc3=[]
    playerc4=[]
    playercards1 = PlayerCards(playerc1)
    playercards2 = PlayerCards(playerc2)
    playercards3 = PlayerCards(playerc3)
    playercards4 = PlayerCards(playerc4)
    
    #playercards1.draw(deck)
    
