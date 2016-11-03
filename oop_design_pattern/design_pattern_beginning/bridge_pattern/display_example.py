import abc
import random

class Display(object):

    def __init__(self, impl):
        self._impl = impl

    def open(self):
        self._impl.raw_open()

    def print(self):
        self._impl.raw_print()

    def close(self):
        self._impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):

    def __init__(self, impl):
        super().__init__(impl)

    def multiple_display(self, times):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class RandomDisplay(Display):

    def __init__(self, impl):
        self._impl = impl

    def random_display(self, times):
        times = random.randint(1, times)

        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl(abc.ABC):

    @abc.abstractmethod
    def raw_open(self):
        pass

    @abc.abstractmethod
    def raw_print(self):
        pass

    @abc.abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):

    def __init__(self, string):
        self._string = string
        self._width = len(string)

    def raw_open(self):
        self._print_line()

    def raw_print(self):
        print("|{}|".format(self._string))

    def raw_close(self):
        self._print_line()

    def _print_line(self):
        print("+", flush=True, end="")
        [print("-", flush=True, end="") for _ in range(self._width)]
        print("+")

if __name__ == "__main__":
    d1 = Display(StringDisplayImpl("Hello, Korea."))
    d2 = CountDisplay(StringDisplayImpl("Hello, World."))
    d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))
    d4 = RandomDisplay(StringDisplayImpl("Hello, Random World."))

    d1.display()
    d2.display()
    d3.display()
    d3.multiple_display(5)
    d4.random_display(10)