import random
import os
import sys
import time
class Card:
    def __init__(self, number):
        self.number = number
        self.face = True

    def flip(self):
        self.face = not self.face

class Deck:
    def __init__(self, ascend):
        self.deck = []
        self.ascend = ascend

    def shuffle(self):
        random.shuffle(self.deck)

    def pushable(self, card):
        if not type(card.number) == int:
            return False
        if len(self.deck) <= 0:
            return True
        top = self.deck[-1].number
        if self.ascend:
            if card.number > top or top - 10 == card.number:
                return True
        else:
            if card.number < top or top + 10 == card.number:
                return True
        return False

    def top(self):
        if len(self.deck) == 0:
            return '-'
        return str(self.deck[-1].number)

    def push(self, card):
        self.deck.append(card)

    def pop(self):
        if len(self.deck) != 0:
            return self.deck.pop()
        else:
            return Card(" ")

    def stack(self):
        pre = self.deck
        a = sorted(self.deck, key=lambda x: x.number)
        print ([c.number for c in a])
        self.deck = pre


class Game:
    def __init__(self):
        self.decks = [Deck(True), Deck(True), Deck(False), Deck(False)]
        self.pile = Deck(None)
        self.hand = Deck(None)
        for num in range(1,100):
            c = Card(num)
            self.pile.deck.append(c)
        self.pile.shuffle()
        for _ in range(8): #populate hand
            self.hand.push(self.pile.pop())


    def keypress(self):
        while True:
            key = input("Press Enter to start game / q to exit\n")
            if key == '':
                return True
            elif key == 'q':
                sys.exit()

    def draw(self):
        os.system('clear') #clear screen
        head = [d.top() for d in self.decks]
        hand = [str(c.number) for c in self.hand.deck]
        cardsleft = len(self.hand.deck) + len(self.pile.deck)
        print ("Cards Left: {:2d} \t\t Hundred - Michael Kwan".format(cardsleft) )
        print ("\t\t Decks")
        print ("\t/---\ /---\ /---\ /---\ ")
        print ("\t|   | |   | |   | |   | ")
        print ("\t|   | |   | |   | |   | ")
        print ("\t|{:3s}| |{:3s}| |{:3s}| |{:3s}|".format(head[0], head[1], head[2], head[3]))
        print ("\t|   | |   | |   | |   | ")
        print ("\t|   | |   | |   | |   | ")
        print ("\t\---/ \---/ \---/ \---/ ")
        print ("\t  1     2     3     4   ")
        print ("\t asc   asc   dsc   dsc  ")
        print ("\n")
        print ("\t\t Hand")
        print ("\t  1     2     3     4   ")
        print ("\t/---\ /---\ /---\ /---\ ")
        print ("\t|{:3s}| |{:3s}| |{:3s}| |{:3s}|".format(hand[0], hand[1], hand[2], hand[3]))
        print ("")
        print ("\t  5     6     7     8   ")
        print ("\t/---\ /---\ /---\ /---\ ")
        print ("\t|{:3s}| |{:3s}| |{:3s}| |{:3s}|".format(hand[4], hand[5], hand[6], hand[7]))

    def checkmoves(self):
        if len(self.pile.deck) + len(self.hand.deck) == 0:
            return False

        for card in self.hand.deck:
            for deck in self.decks:
                if deck.pushable(card):
                    return True
        #cannot push cards in hand into any pile
        return False

    def move(self, position, pile):
        current = self.hand.deck[position-1]
        if type(current.number) == str:
            print ("Hand position is empty")
            return False
        if self.decks[pile-1].pushable(current):
            print ("Moving {0} from position {1} to pile {2}".format(current.number, position, pile))
            self.decks[pile-1].push(current)
            self.hand.deck[position-1] = self.pile.pop()
            return True
        else:
            print ("Cannot move {0} from position {1} to pile {2}".format(current.number, position, pile))
            return False

    def drawend(self):
        if len(self.pile.deck) + len(self.hand.deck) == 0:
            os.system("clear")
            print ("\n\n\n")
            print ("You Win!")
        else:
            print ("Sorry, no more moves.")

def intro():
     os.system('clear') #clear screen
     print ("Hundred - Michael Kwan\n")
     print ("RULES:")
     print ("\t.There are 100 cards numbered 1 to 100 inclusive in a deck of cards.")
     print ("\t.There are four stacks, two which ascend in number and two which descend.")
     print ("\t.A card can be placed on an ascending stack if the number is greater than the card before it.")
     print ("\t.However, a card can be placed on ascending deck if it is exactly 10 less than the card before it.")
     print ("\t.The opposite rules go for descending stacks.")
     print ("\t.There are 8 card in your hand, replenished after every placement.")
     print ("\t.Move a card from your hand to a deck by specifying a position number and a deck (ie 52, 14, 73).")
     print ("\t.Game ends if there are no possible moves / cards to place.")

def play():
    intro()
    while keypress():
        g = Game()
        while g.checkmoves():
            g.draw()
            while True:
                move = input("What is your move? \n")
                if len(move) == 2 and move[0] in [str(i) for i in range(1,9)] and move[1] in [str(i) for i in range(1,5)]:
                    status = g.move(int(move[0]), int(move[1]))
                    if status:
                        break
                elif move == 's':
                    g.pile.stack()
                    status = ("Press any key to continue")
                elif move == 'q':
                    sys.exit()
                elif move == 'r':
                    play()
                else:
                    print("Invalid Command")
                g.draw()
        g.draw()
        g.drawend()

def keypress():
     while True:
         key = input("Press Enter to start game / q to exit\n")
         if key == '':
             return True
         elif key == 'q':
             sys.exit()

if __name__ == "__main__":
    play()
