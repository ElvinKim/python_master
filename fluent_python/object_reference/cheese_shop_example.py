import weakref

class Cheese(object):

    def __init__(self, kind):
        self._kind = kind

    @property
    def kind(self):
        return self._kind

    def __repr__(self):
        return "Cheese({})".format(self._kind)


if __name__ == "__main__":
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese("Tilsit"), Cheese("Brie"), Cheese("Parmesan")]

    for cheese in catalog:
        stock[cheese.kind] = cheese

    print(sorted(stock.keys())) # ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

    del catalog
    print(sorted(stock.keys())) # ['Parmesan']

    del cheese
    print(sorted(stock.keys())) # []



