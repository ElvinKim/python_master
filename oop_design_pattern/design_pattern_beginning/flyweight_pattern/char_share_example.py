"""
  ______   _                             _           _       _
 |  ____| | |                           (_)         | |     | |
 | |__    | |  _   _  __      __   ___   _    __ _  | |__   | |_
 |  __|   | | | | | | \ \ /\ / /  / _ \ | |  / _` | | '_ \  | __|
 | |      | | | |_| |  \ V  V /  |  __/ | | | (_| | | | | | | |_
 |_|      |_|  \__, |   \_/\_/    \___| |_|  \__, | |_| |_|  \__|
                __/ |                         __/ |
               |___/                         |___/


* 언제 사용하는가?
    - 인스턴스를 최대한 공유시켜서 쓸데 없이 객체를 생성하지 않게 하는 패턴
    - 이미 만들어져 있는 객체는 다시 생성하지 않고 공유해서 이용하는 패턴

* 주요 특징은 무엇인가?
    - 공유한다는 것은 여려 장소에 영향을 미친다는 의미이고 이는 변경은 여러 장소에 영향을 미친다는 말고 같음
        - 변경할 경우 신중하게 처리해야 함
    - intrinsic한 정보 : 장소나 상황에 의존하지 않음. 공유할 수 있음
    - extrinsic한 정보 : 장소나 상황에 의존함. 공유할 수 없음

* 구성요소
    - Flyweight : 평소대로 처리하면 프로그램이 무거워지기 때문에 공유하는 것이 좋은 것을 나타내는 역할
    - FlyweightFactory : Flyweight을 만드는 역할. 만들어진 Flyweight는 공유됨
    - Client : FlyweightFactory를 이용하여 Flyweight 역할을 만들고 사용하는 역할
"""


from singleton import Singleton


class BigChar(object):

    def __init__(self, char_name):
        self._char_name = char_name
        self._font_data = ""

        try:
            with open("big{}.txt".format(char_name)) as f:
                for line in f.readlines():
                    self._font_data += line

        except FileNotFoundError:
            self._font_data = char_name + "?"

    def print(self):
        print(self._font_data)


class BigCharFactory(metaclass=Singleton):

    def __init__(self):
        self._pool = dict()

    def get_big_char(self, char_name):
        return self._pool.setdefault(char_name, BigChar(char_name))


class BigString(object):

    def __init__(self, string):
        self._big_chars = []
        self._factory = BigCharFactory()

        for i in range(len(string)):
            self._big_chars.append(self._factory.get_big_char(string[i]))

    def print(self):
        for big_char in self._big_chars:
            big_char.print()


if __name__ == "__main__":
    big_string = BigString("13579")
    big_string.print()





