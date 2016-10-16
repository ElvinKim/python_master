
class Descriptior(object):

    def __init__(self):
        self.a = None

    def __get__(self, instance, owner):
        print("__get__ function call")
        print("\t", self, instance, owner)

    def __set__(self, instance, value):
        print("__set__ function call")
        print("\t", self, instance, value)



class Manager(object):

    m1 = Descriptior()
    m2 = Descriptior()


if __name__ == "__main__":
    manager = Manager()

    print(manager)
    manager.m1
    manager.m2 = 10





