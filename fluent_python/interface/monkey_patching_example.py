import collections
from random import shuffle


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck(object):
    rank = [str(n) for n in list(range(2, 11)) + list("JQKA")]
    suits = 'Spades diamonds slubs hearts'

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def set_card(self, key, value):
    self._cards[key] = value

if __name__ == "__main__":
    FrenchDeck.__setitem__ = set_card

    deck = FrenchDeck()
    print(deck[:10])
    shuffle(deck)
    print(deck[:10])
