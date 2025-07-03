from random import randint, shuffle

class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class deck:
    def __init__(self):
        self.suits = ["heart", "spades", "clubs", "diamond"]
        self.pile = []
        for x in range(4):
            for y in range(13):
                c = card(self.suits[x], y + 1)
                self.pile.append(c)
                
    def printdeck(self):
        for c in self.pile:
            print(c)
            
    def draw(self):
        topcard = self.pile[0]
        self.pile.remove(topcard)
        return topcard

    def shuffle(self):
        shuffle(self.pile)

pile = deck()
pile.shuffle()

p1 = []
p2 = []
middle = []

# Deal the cards
for x in range(26):
    p1.append(pile.draw())
    p2.append(pile.draw())

game = True
while game:
    middle = []  # Reset the middle pile at the start of each round
    middle.append(p1[0])
    middle.append(p2[0])

    p1.remove(p1[0])
    p2.remove(p2[0])

    print(f"Player 1 plays: {middle[0]}")
    print(f"Player 2 plays: {middle[1]}")

    if middle[0].value > middle[1].value:
        print("Player 1 wins the round")
        p1.extend(middle)
    elif middle[1].value > middle[0].value:
        print("Player 2 wins the round")
        p2.extend(middle)
    else:  # It's a tie, so war happens
        print("WAR!")
        if len(p1) >= 4 and len(p2) >= 4:
            for _ in range(3):  # Both players place 3 cards face down
                middle.append(p1[0])
                p1.remove(p1[0])
                middle.append(p2[0])
                p2.remove(p2[0])

            # Players place 1 card face up
            middle.append(p1[0])
            middle.append(p2[0])

            p1.remove(p1[0])
            p2.remove(p2[0])

            if middle[-2].value > middle[-1].value:
                print("Player 1 wins the war")
                p1.extend(middle)
            elif middle[-1].value > middle[-2].value:
                print("Player 2 wins the war")
                p2.extend(middle)
            else:
                print("War results in another tie!")
                middle = []  # Reset for another round
        else:  # Not enough cards to continue war
            if len(p1) < 4:
                print("Player 1 lost")
                game = False
            elif len(p2) < 4:
                print("Player 2 lost")
                game = False

    # Check for game over condition
    if len(p1) == 0:
        print("Player 1 lost")
        game = False
    elif len(p2) == 0:
        print("Player 2 lost")
        game = False
