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
# print(pile.draw())
# pile.printdeck()
middle=[]
p1=[]
p2=[]
for x in range(26):
    p1.append(pile.pile[0])
    pile.draw()
    p2.append(pile.pile[0])
    pile.draw()
game=True
while game==True:
    middle.append(p1[0])
    print("Player 1 plays: "+ str(p1[0]))
    p1.remove(p1[0])
    middle.append(p2[0])
    print("Player 2 plays: "+ str(p2[0]))
    p2.remove(p2[0])

    if middle[0].value>middle[1].value:
        print("Player 1 had a higher card")
        p1.append(middle[0])
        middle.remove(middle[0])
        p1.append(middle[0])
        middle.remove(middle[0])
    elif middle[1].value> middle[0].value:
        print("Player 2 had a higher card")
        p2.append(middle[0])
        middle.remove(middle[0])
        p2.append(middle[0])
        middle.remove(middle[0])
    elif middle[1].value== middle[0].value:
        if len(p1)>4 and len(p2)>4:
            print("WAR")
            middle.append(p1[0])
            print("Player 1 plays: "+ str(p1[0]))
            p1.remove(p1[0])
            middle.append(p2[0])
            print("Player 2 plays: "+ str(p2[0]))
            p2.remove(p2[0])
            if middle[0].value>middle[1].value:
                print("Player 1 had a higher card")
                for i in range(5):
                    p1.append(middle[0])
                    middle.remove(middle[0])
            elif middle[1].value> middle[0].value:
                print("Player 2 had a higher card")
                for j in range(5):
                    p2.append(middle[0])
                    middle.remove(middle[0])
        else:
            if len(p1)<4:
                print("Player 1 lost")
                break
            elif len(p2)<4:
                print("Player 2 lost")
                break





    print("Player 1 has: " + str(len(p1))+" cards")
    print("Player 2 has: " + str(len(p2))+" cards")
    








