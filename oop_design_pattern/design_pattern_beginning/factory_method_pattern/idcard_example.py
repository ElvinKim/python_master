import abc

class Product(abc.ABC):

    @abc.abstractmethod
    def use(self):
        pass


class Factory(abc.ABC):

    def create(self, owner):
        product = self.create_product(owner)
        self.register_product(product)
        return product

    @abc.abstractmethod
    def create_product(self, owner):
        pass

    def register_product(self, product):
        pass


class IDCard(Product):

    def __init__(self, owner):
        print("{}님의 ID카드를 만듭니다.".format(owner))
        self._owner = owner

    def use(self):
        print("{}님의 ID카드를 사용합니다..".format(self._owner))

    @property
    def owner(self):
        return self._owner


class IDCardFactory(Factory):

    def __init__(self):
        self._owners = list()

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self._owners.append(product.owner)

    @property
    def owners(self):
        return self._owners


if __name__ == "__main__":

    factory = IDCardFactory()
    card1 = factory.create("Hong")
    card2 = factory.create("Lee")
    card3 = factory.create("Kim")

    card1.use()
    card2.use()
    card3.use()





