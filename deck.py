from random import shuffle


class Deck:

    ranks = list(range(2, 11)) + ["Ace", "Jack", "Queen", "King"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self):
        """ generate a deck of 52 cards"""
        self.deck = ['{0} {1}'.format(rank, suit) for rank
                     in self.ranks for suit in self.suits]
        shuffle(self.deck)

    def get_deck(self, num=52):
        """ return a deck of (num) cards """
        if not 0 < num < 53:
            raise Exception("Can't return a deck of 0 or more than 52 cards")
        return self.deck[:num]
