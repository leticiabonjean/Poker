from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        """
        initializes a 5-card power hand delt from deck
        :param deck: a Deck object from which to deal cards
        """
        cards = [] #this is where "cards" came from
        for i in range(5):
            cards.append(deck.deal()) #deal is a method created in the other class
        self._cards = cards #the _ is a naming convention, it signals the variable is for "private use only"

    @property
    def cards(self):
        """
        getter method for cards
        :return: cards
        """
        return self._cards

    def __str__(self):
        """
        magic method tha returns a human-readable version of cards
        :return: cards in string method
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        determine if cards in the hand are a poker flush
        :return: True if hand is a flush, False otherwise
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:  #HOWEVER, here we're accounting the royal flush as a flush, but it's not
                return False
        return True

    @property
    def number_matches(self):
        """
        calculates the number of duplicate rank matches in the hand
        :return: an integer count of rank matches
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        determine if cards in the hand is a poker pair
        :return: True if hand is a pair, False otherwise
        """
        if self.number_matches == 2: #more simple
            return True
        return False

    @property
    def is_two_pair(self):
        """
        determines if cards in the hand correspond to two poker pairs
        :return: True if hand consists of two pairs, False otherwise
        """
        if self.number_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
        determines if cards in the hand are a poker triple
        :return: True if hand is a triple, False otherwise
        """
        if self.number_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        determines if cards in the hand correspond to a poker full house
        :return: True is hand is full house, False otherwise
        """
        return self.is_trips and self.is_pair

    @property
    def is_straight(self):
        """
        determines if cards in the hand correspond to a poker straight
        :return: True id hand is a straight, False otherwise
        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) -Card.RANKS.index(self.cards[0].rank)  # starts counting from 0 so, 0, 1, 2, 3, 4 = 5 cards, backslash is to mean it continues
#we know that the last card minus the index of the last one must be 4
        return self.number_matches == 0 and distance == 4


# count = 0
# flushes = 0
# while flushes < 1000:
#     deck = Deck()
#     deck.shuffle()
#     hand = PokerHand(deck)
#     if hand.is_flush:
#         flushes += 1
#     count += 1
#
# print(f"probability of a flush is {100*flushes/count}%")

count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight: #no need to use () for is_straight) since we added the property decorator before
        matches += 1
        #print(hand)
    count += 1

print(f"probability of a flush is {100*matches/count}%")

deck = Deck()
deck.shuffle()
hand = PokerHand(deck)
print(hand) #will give you 5 random cards from the deck, which was just shuffled