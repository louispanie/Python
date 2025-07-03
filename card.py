from random import randint
class card:
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
    def __str__(self):
        return  str(self.value) + " of " + self.suit

class deck:
    def __init__(self):
        self.suits=["heart", "spades", "clubs", "diamond"]
        self.pile=[]
        for x in range(4):
            for y in range(13):
                c = card(self.suits[x], y+1)
                self.pile.append(c)
    def printdeck(self):
        for i in range(len(self.pile)):
            print(self.pile[i])
    def draw(self):
        topcard=self.pile[0]
        self.pile.remove(self.pile[0])
        return topcard
    def shuffle(self):
        self.shufflepile=[]
        for i in range(52):
            x=randint(0, len(self.pile))
            self.shufflepile.append(self.pile[x-1])
            self.pile.remove(self.pile[x-1])
        self.pile=self.shufflepile

pile=deck()
pile.shuffle()
print(pile.draw())
pile.printdeck()
















