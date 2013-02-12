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
        return cards

    def shuffle(self,d):
        random.shuffle(d)
        return d

    def write(self, d):
        with open('new.txt','w') as nd:
            for i in d:
                nd.write(i)

    def pick(self):
        cards = self.read_file('new.txt')
        if cards:
            card = cards.pop(0)
            self.write(cards)
            return card
        else:
            print 'no cards'
            
    
class PlayerCards:    
    def __init__(self, playerc):
        self.playerc = playerc

    def draw(self,deck):
        card = deck.pick()
        if card:
            self.playerc.append(card)
        print self.playerc
        self.check(self.playerc)
        
    def check(self, playerc):
        if len(playerc)==5:
            print "You must trade your cards!"
            reinforcements = self.trade(playerc)
            
    def trade(self,playerc):
        tr1 = tr2 = tr3 = [2]
        c1 = int(raw_input("Which cards you want to trade? (type something like '1' or '2' etc.)\n"))
        c2 = int(raw_input())
        c3 = int(raw_input())

        tr1 = playerc[c1-1].rsplit()
        tr2 = playerc[c2-1].rsplit()
        tr3 = playerc[c3-1].rsplit()

        if tr1[0]==tr2[0]==tr3[0]=='inf':
            reinf = 4
        elif tr1[0]==tr2[0]==tr3[0]=='art':
            reinf = 6
        elif tr1[0]==tr2[0]==tr3[0]=='cav':
            reinf = 8
        elif tr1[0]!=tr2[0]!=tr3[0]:
            reinf = 10
        else:
            print "invalid trade"
            self.trade(playerc)
        
        del playerc[c3-1]
        del playerc[c2-1]
        del playerc[c1-1]
        print "Your cards now:", playerc
        print "You take ", reinf, "reinforcements!"
        return reinf

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
    
