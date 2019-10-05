import hundred
import pytest

g = hundred.Game()

def test_Game():
    #check Game object is created to specification
    assert len(g.decks) == 4
    assert g.pile != None
    assert g.hand != None
    assert len(g.pile.deck) + len(g.hand.deck) == 99
    assert len(g.hand.deck) == 8

c = hundred.Card(12)
def test_Card():
    #check Card object is created to specification
    assert c.number == 12
    assert c.face == True
    #test Card functions
    c.flip()
    assert c.face == False

d = hundred.Deck(True)
def test_Deck():
    #check Deck object is created to specification
    assert len(d.deck) == 0
    assert d.ascend == True
    #test Deck functions
    assert d.pushable(c) == True
    d.push(c)
    assert len(d.deck) == 1
    assert d.top() == '12'
    d.pop()
    assert len(d.deck) == 0
    d.push(hundred.Card(13))
    d.push(hundred.Card(14))
    d.push(hundred.Card(15))
    assert len(d.deck) == 3
    previous = d.deck
    d.shuffle()
    assert set(previous) == set(d.deck)

def test_Move():
    #test valid moves
    g.decks[0].push(hundred.Card(99))
    g.decks[1].push(hundred.Card(97))
    g.decks[2].push(hundred.Card(1))
    g.decks[3].push(hundred.Card(3))
    g.pile.deck = []
    g.hand.deck = [hundred.Card(98), hundred.Card(2), hundred.Card(' '), hundred.Card(' '), hundred.Card(' '), hundred.Card(' '), hundred.Card(' '), hundred.Card(' ')]
    #valid move 1
    assert g.checkmoves() == True
    assert g.move(1, 1) == False
    assert g.move(1, 3) == False
    assert g.move(1, 4) == False
    assert g.move(1, 2) == True
    assert g.hand.deck[0].number == ' '
    #valid move 2
    assert g.checkmoves() == True
    assert g.move(2, 1) == False
    assert g.move(2, 2) == False
    assert g.move(2, 3) == False
    assert g.move(2, 4) == True
    #no more valid moves
    assert g.checkmoves() == False
    #do not accept invalid move
    g.hand.deck[0] = hundred.Card(10)
    assert g.checkmoves() == False
    assert g.move(1, 1) == False


