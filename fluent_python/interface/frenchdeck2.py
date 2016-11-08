import collections


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck(collections.MutableSequence):
    rank = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'Spades diamonds slubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value):
        self._cards[index] = value


if __name__ == "__main__":
    deck = FrenchDeck()

