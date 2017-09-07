import random

class Card:

    def __init__(self, rank, suite):
        self.suite = suite
        self.rank = rank


    def get_rank(self):
        return self.rank

    def get_suite(self):
        return self.suite

    def BJValue(self):
        if self.rank == 'Ace':
            return 1
            #if unicode in future, maybe change these values to unicode strings
        elif self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
            return 10
        else:
            return int(self.rank)

    def __str__(self):
        return ('{0} of {1}'.format(self.rank, self.suite))

    #def flip(self): pass

    def __repr__(self):
        return "%s of %s" % (self.rank, self.suite)


def shuffled_deck():
    deck = []
    for suite in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
        for num in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            deck.append(Card(num, suite))
    random.shuffle(deck)
    return deck


# class Deck():
#     def __init__(self): pass  # newDeck()
#     def shuffle(self): pass
#     def draw(self): pass
#     def draw_hand(self, size): pass
#     def draw_faceup(self): pass


'''References/Citations'''
#https://stackoverflow.com/questions/14467933/how-to-approach-implementing-class-card-as-required-by-python-textbook
