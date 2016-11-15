import abc


class A(abc.ABC):
    @abc.abstractmethod
    def test(self):
        pass


class B(A):
    pass


if __name__ == "__main__":
    b = B()
