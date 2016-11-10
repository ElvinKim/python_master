"""
   _____   _               _                      __
  / ____| | |             (_)                    / _|
 | |      | |__     __ _   _   _ __       ___   | |_
 | |      | '_ \   / _` | | | | '_ \     / _ \  |  _|
 | |____  | | | | | (_| | | | | | | |   | (_) | | |
  \_____| |_| |_|  \__,_| |_| |_| |_|    \___/  |_|

                                                    _   _       _   _   _   _
                                                   (_) | |     (_) | | (_) | |
  _ __    ___   ___   _ __     ___    _ __    ___   _  | |__    _  | |  _  | |_   _   _
 | '__|  / _ \ / __| | '_ \   / _ \  | '_ \  / __| | | | '_ \  | | | | | | | __| | | | |
 | |    |  __/ \__ \ | |_) | | (_) | | | | | \__ \ | | | |_) | | | | | | | | |_  | |_| |
 |_|     \___| |___/ | .__/   \___/  |_| |_| |___/ |_| |_.__/  |_| |_| |_|  \__|  \__, |
                     | |                                                           __/ |
                     |_|                                                          |___/


* 언제 사용하는가?
    - 복수의 오브젝트(객체)를 사슬(Chain)처럼 연결해 두면,
      그 오브젝트(객체)의 사슬을 차례로 돌아다니면서 목적한 오브젝트(객체)를 결정하는 패턴


* 주요 특징은 무엇인가?
    - 책임을 떠넘기는 구조를 생각했을 때, 요청하는 쪽과 처리하는 쪽의 연결을 유연하게 독립시킬 수 있음
    - set_next(Support)를 통해서 특정 객체가 처리하지 못할 때 다음 Chain으로 넘김
    - 만약 이 패턴을 사용하지 않으면 특정 사항을 누가 처리한다는 정보를 누군가 가지고 있어야 하는데
      그 정보를 요구하는 쪽에서 가지고 있는건 좋지 않음. 이는 독립성이 훼손됨.
    - 처리하는 쪽은 처리하는 것에만 집중할 수 있음
    - 단 처리하는 것이 느려지는 부분이 있지만 이는 트레이드 오프 문제임
"""

import abc


class Trouble(object):

    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number

    def __str__(self):
        return '[Trouble {}]'.format(self._number)


class Support(object):

    def __init__(self, name):
        self._name = name
        self._next = None

    def set_next(self, next):
        self._next = next
        return next

    def support(self, trouble):
        if self._resolve(trouble):
            self._done(trouble)
        elif self._next is not None:
            self._next.support(trouble)
        else:
            self._fail(trouble)

    def __str__(self):
        return "[{}]".format(self._name)

    @abc.abstractmethod
    def _resolve(self, trouble):
        pass

    def _done(self, trouble):
        print("{} is resolved by {}.".format(trouble, self))

    def _fail(self, trouble):
        print("{} cannot be resolved.".format(trouble))


class NoSupport(Support):

    def __init__(self, name):
        super().__init__(name)

    def _resolve(self, trouble):
        return False


class LimitSupport(Support):

    def __init__(self, name, limit):
        super().__init__(name)
        self._limit = limit

    def _resolve(self, trouble):
        return trouble.number < self._limit


class OddSupport(Support):

    def __init__(self, name):
        super().__init__(name)

    def _resolve(self, trouble):
        return trouble.number % 2 == 1


class SpecialSupport(Support):

    def __init__(self, name, number):
        super().__init__(name)
        self._number = number

    def _resolve(self, trouble):
        return trouble.number == self._number


if __name__ == "__main__":
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 100)
    charlie = SpecialSupport("Charlie", 429)
    diana = LimitSupport("Diana", 200)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)

    alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)

    for i in range(0, 500, 33):
        alice.support(Trouble(i))