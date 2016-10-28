import abc
import copy

class Product(abc.ABC):

    @abc.abstractmethod
    def use(self, s):
        pass

    @abc.abstractmethod
    def create_clone(self):
        pass


class Manager(object):

    def __init__(self):
        self._show_case = dict()

    def register(self, name, product):
        self._show_case[name] = product

    def create(self, product_name):
        return self._show_case[product_name].create_clone()


class MessageBox(Product):

    def __init__(self, decochar):
        self._decochar = decochar

    def use(self, s):

        [print(self._decochar, flush=True, end="") for _ in range(len(s) + 4)]
        print("")
        print("{decochar} {s} {decochar}".format(s=s, decochar=self._decochar))
        [print(self._decochar, flush=True, end="") for _ in range(len(s) + 4)]
        print("")

    def create_clone(self):
        p = copy.deepcopy(self)
        return p


class UnderlinePen(Product):

    def __init__(self, ulchar):
        self._ulchar = ulchar

    def use(self, s):
        print("\"{}\"".format(s))
        print(" ", flush=True, end="")
        [print(self._ulchar, flush=True, end="") for _ in range(len(s))]
        print(" ")

    def create_clone(self):
        p = copy.deepcopy(self)
        return p

if __name__ == "__main__":
    manager = Manager()
    upen = UnderlinePen("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")

    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("splash box", sbox)

    p1 = manager.create("strong message")
    p1.use("Hello, world")

    p2 = manager.create("warning box")
    p2.use("Hello, world")

    p3 = manager.create("splash box")
    p3.use("Hello, world")

    p4 = manager.create("strong message")

    print(id(p1))
    print(id(p4))
