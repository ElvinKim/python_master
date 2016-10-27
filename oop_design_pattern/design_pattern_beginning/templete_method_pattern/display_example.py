
import abc

class AbstractDisplay(abc.ABC):
    """
    상위 클래스에서 프로그램의 전체적인 흐름을 결정
    하위 클래스가 추상 메소드를 상속받고 구체적인 흐름을 결정
    """

    @abc.abstractmethod
    def _open(self):
        pass

    @abc.abstractmethod
    def print(self):
        pass

    @abc.abstractmethod
    def _close(self):
        pass

    def display(self):
        self._open()
        for _ in range(5):
            self.print()
        self._close()


class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self._ch = ch

    def _open(self):
        print("<<",end="", flush=True)

    def _close(self):
        print(">>")

    def print(self):
        print(self._ch, end="",  flush=True)


class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self._string = string
        self._width = len(string)

    def _open(self):
        print("+{}+".format("".join(["-" for _ in range(self._width)])))

    def _close(self):
        print("+{}+".format("".join(["-" for _ in range(self._width)])))

    def print(self):
        print("|{}|".format(self._string))


if __name__ == "__main__":
    ch_display = CharDisplay("H")
    ch_display.display()

    str_display = StringDisplay("Hello, World!")
    str_display.display()

