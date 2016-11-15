"""
   ____    _
  / __ \  | |
 | |  | | | |__    ___    ___   _ __  __   __   ___   _ __
 | |  | | | '_ \  / __|  / _ \ | '__| \ \ / /  / _ \ | '__|
 | |__| | | |_) | \__ \ |  __/ | |     \ V /  |  __/ | |
  \____/  |_.__/  |___/  \___| |_|      \_/    \___| |_|



* 언제 사용하는가?
    - 관찰 대상의 상태가 변화할 때 관찰자에게 알려주는 패턴

* 주요 특징은 무엇인가?
    - 상태 변화에 따른 처리를 기술할 때 효과적
    - Subject(관찰 대상자)는 Observer(관찰자)인지는 알지만 구체적으로 어떤 Observer인지는 알 필요 없다.
      마찬가지로 Observer는 Subject인지는 알지만 구체적으로 어떤 Subject인지는 알 필요 없다.
    - Observer가 Subject에 영향을 미친다면 주의해야함
      Subject 상태 변화 -> Observer 전달 -> Observer에 의해 Subject 상태 변화 -> Observer 에게 전달 ...
      이 루프에 빠지지 않게 주의
    - Observer 패턴은 publish-subscribe패턴 이라고도 함
    - MVC에서 Model과 View의 관계가 Observer와 Subject 관계임
"""

import abc
import random


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, generator):
        pass


class NumberGenerator(abc.ABC):

    def __init__(self):
        self._observers = list()

    def add_observer(self, observer):
        self._observers.append(observer)

    def delete_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    @abc.abstractmethod
    def get_number(self):
        pass

    @abc.abstractmethod
    def excute(self):
        pass


class RandomNumberGenerator(NumberGenerator):

    def __init__(self):
        super().__init__()
        self._number = None

    def get_number(self):
        return self._number

    def excute(self):
        for _ in range(20):
            self._number = random.randint(1, 50)
            self.notify_observers()


class DigitObserver(Observer):

    def update(self, generator):
        print("DigitObserver : ", generator.get_number())


class GraphObserver(Observer):

    def update(self, generator):
        print("GraphObserver : ", flush=True, end="")

        count = generator.get_number()

        for i in range(count):
            print("*", flush=True, end="")
        print("")


if __name__ == "__main__":
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)

    generator.excute()
