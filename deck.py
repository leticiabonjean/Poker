import random

class Card:
    """
    represents a standard playing card with suit & rank
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    def __init__(self, suit, rank):
        """
        initializes a card with a specified suit and rank
        :param suit: one of the valid suits (in SUITS)
        :param rank: one of the valid ranks (in RANKS)
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit #this _suit is the name you're giving, the RHS is the attribute/variable
        self._rank = rank

    def __eq__(self, other):
        """
        compares two cards for equality based on their rank
        :param other: another Card object
        :return: True if the ranks are the same, False otherwise
        """
        return self.rank == other.rank

    def __gt__(self, other):     #you can't compare ranks, cause rn they're strings. you should compare the POSITION of the rank on the list
        """
        compare two cards to determine if one is greater than another. Based on the tank's position in the predefined order
        :param other: another Card object
        :return: True if this card's (self) rank is higher than the other (other). False otherwise
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank) #compare the position in the rank list of self. versus the position in the rank of other.

    def __str__(self): #this is to be able to print the cards
       """
       magic method tha returns a human-readable representation of the Card instance
       :return: "rank suit"
       """
        return f"{self._rank}{self._suit}" #establishing the order it will be printed in

    def __repr__(self):
        """
        returns the official string representation of the card for debugging the lists
        :return: same as __str__, "rank suit"
        """
        return self.__str__() #this is to be able to print a list

    @property #to access the suit
    def suit(self):
        """
        Getter method for suit
        :return: suit of the card
        """
        return self._suit

    @property
    def rank(self):
        """
        Getter method for rank
        :return: rank of the card (as a string)
        """
        return self._rank

    # jack_clubs = Card("♣", "J")
    # print(jack_clubs)

#now you want to crease a class for a DECK

class Deck:
    """
    Class that represents a standard 52-card deck with the ability to shuffle and deal cards
    """
    def __init__(self):
        """
        initialized a deck containing 52 unique cards, one of each possible combination between suit and rank
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        magic method tha returns a human-readable representation of the Card instance
        :return: a list of card strings
        """
        return str(self._deck) #creating a string, string representation of the list

    def shuffle(self):
        """
        randomly shuffles the rder of cards in the deck
        :return: shuffled version of _deck
        """
        random.shuffle(self._deck) #needed to import random for this

    def deal(self):
        """
        deals the top card from the deck
        :return: a Card instance from the top of the deck
        """
        return self._deck.pop(0)

deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print(deck.deal())


