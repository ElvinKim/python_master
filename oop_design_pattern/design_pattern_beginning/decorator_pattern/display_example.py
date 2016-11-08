"""
  _____                                         _
 |  __ \                                       | |
 | |  | |   ___    ___    ___    _ __    __ _  | |_    ___    _ __
 | |  | |  / _ \  / __|  / _ \  | '__|  / _` | | __|  / _ \  | '__|
 | |__| | |  __/ | (__  | (_) | | |    | (_| | | |_  | (_) | | |
 |_____/   \___|  \___|  \___/  |_|     \__,_|  \__|  \___/  |_|


* 언제 사용하는가?
    - 주어진 상황 및 용도에 따라 어떤 객체에 책임을 덧붙이는 패턴

* 주요 특징은 무엇인가?
    - 장식을 하면 할 수록 기능이 추가되는 패턴
    - 내용물을 변경하지 않고 기능을 추가 할 수 있음

* 생각해 볼 수 있는 사용 예
    - RPG 게임에서 무기에 속성을 부여하여 뭔가 새로운 기술이 나가는 기능
"""


import abc


class Display(abc.ABC):

    @abc.abstractmethod
    def get_columns(self):
        pass

    @abc.abstractmethod
    def get_rows(self):
        pass

    @abc.abstractmethod
    def get_row_text(self, row):
        pass

    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):

    def __init__(self, string):
        self._string = string

    def get_columns(self):
        return len(self._string)

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row == 0:
            return self._string
        else:
            return None


class Border(Display):

    def __init__(self, display):
        self._display = display


class SideBorder(Border):

    def __init__(self, display, char):
        super().__init__(display)
        self._border_char = char

    def get_columns(self):
        return 1 + self._display.get_columns() + 1

    def get_rows(self):
        return self._display.get_rows()

    def get_row_text(self, row):
        return "{border_char}{text}{border_char}".format(text=self._display.get_row_text(row),
                                                         border_char=self._border_char)

class FullBorder(Border):

    def __init__(self, display):
        super().__init__(display)

    def get_columns(self):
        return 1 + self._display.get_columns() + 1

    def get_rows(self):
        return 1 + self._display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0 or row == self._display.get_rows() + 1:
            return "+{}+".format("-" * self._display.get_columns())
        else :
            return "|{}|".format(self._display.get_row_text(row-1))


if __name__ == "__main__":

    b1 = StringDisplay("Hello, World.")
    b2 = SideBorder(b1, "#")
    b3 = FullBorder(b2)
    b4 = SideBorder(FullBorder(FullBorder(SideBorder(FullBorder(StringDisplay("Hello!!!!!")), "*"))), "/")

    b1.show()
    b2.show()
    b3.show()
    b4.show()