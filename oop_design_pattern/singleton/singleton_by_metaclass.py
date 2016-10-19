
class Singleton(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class A(metaclass=Singleton):
    pass


if __name__ == "__main__":
    a = A()
    b = A()

    print(a is b)
