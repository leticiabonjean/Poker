import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    def __init__(self, suit, rank): # needs to take both a suit and a rank
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __str__(self): #this is to be able to print the cards
        return f"{self._rank}{self._suit}" #establishing the order it will be printed on

    def __repr__(self):
        return self.__str__() #this is to be able to print a list

    @property #to access the suit
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    # jack_clubs = Card("♣", "J")
    # print(jack_clubs)

#now you want to crease a class for a DECK

class Deck:
    def __init__(self):
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        return str(self._deck) #creating a string, string representation of the list

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0)

deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print(deck.deal())


