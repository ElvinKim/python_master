import random


class BingoCage(object):

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)


    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty Bingo Cage")


    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == "__main__":
    bingo = BingoCage(range(30))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
