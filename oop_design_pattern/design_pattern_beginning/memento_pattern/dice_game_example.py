"""
  __  __                                     _
 |  \/  |                                   | |
 | \  / |   ___   _ __ ___     ___   _ __   | |_    ___
 | |\/| |  / _ \ | '_ ` _ \   / _ \ | '_ \  | __|  / _ \
 | |  | | |  __/ | | | | | | |  __/ | | | | | |_  | (_) |
 |_|  |_|  \___| |_| |_| |_|  \___| |_| |_|  \__|  \___/



* 언제 사용하는가?
    - 인스턴스의 상태를 나타내는 역할을 도입하여 캡슐화의 파괴에 빠지지 않고 저장과 복원을 실행하는 패턴

* 주요 특징은 무엇인가?
    - 어떤 시점의 인스턴스의 상태를 확실하게 기록한 뒤 나중에 인스턴스를 그 시점으로 되돌릴 수 있음
    - wide interface : 오브젝트의 상태를 원래의 상태로 돌리기 위해 필요한 정보를 모두 얻을 수 있는 메소드의 집합
    - narrow interface : 외부의 Caretaker 역할에게 보여주는 것. 할수 있는 것의 한계가 있고 외부에 공개되는 것을 방지


* 구성요소
    - Originator : 현재 상태를 저장하고 싶어하는 구성 요소 이며 Memento를 생성
    - Memento : Originator의 정보를 가지고 있지만 누구에게도 그 정보를 공개하지 않음
    - Caretaker : 현재의 Originator의 역할의 상태를 저장하고 싶을 때 그것을 Originator에게 전달
"""


import copy
import random


class Memento(object):

    def __init__(self, money):
        self._fruits = list()
        self._money = money

    @property
    def money(self):
        return self._money

    def add_fruit(self, fruit):
        self._fruits.append(fruit)

    @property
    def fruits(self):
        return copy.deepcopy(self._fruits)


class Gamer(object):

    def __init__(self, money):
        self._money = money
        self._fruits = list()
        self._fruitsname = ["사과", "포도", "바나나", "귤"]

    @property
    def money(self):
        return self._money

    def bet(self):
        dice_number = random.randint(1, 6)

        if dice_number == 1:
            self._money += 100
            print("소지금이 증가했습니다.")
        elif dice_number == 2:
            self._money /= 2
            print("소지금이 절반이 되었습니다.")
        elif dice_number == 6:
            fruit = self._get_fruit()
            print("과일({})을 받았습니다.".format(fruit))
            self._fruits.append(fruit)
        else:
            print("변한 것이 없습니다.")

    def create_memento(self):
        memento = Memento(self._money)

        for fruit in self._fruits:
            if "맛있는" in fruit:
                memento.add_fruit(fruit)

        return memento

    def restore_memento(self, memento):
        self._money = memento.money
        self._fruits = memento.fruits

    def __str__(self):
        return "money = {} , fruits = {}".format(self._money, self._fruits)

    def _get_fruit(self):
        prefix = ""

        if bool(random.getrandbits(1)):
            prefix = "맛있는"

        return prefix + self._fruitsname[random.randint(0, len(self._fruitsname) - 1)]

if __name__ == "__main__":
    gamer = Gamer(100)
    memento = gamer.create_memento()

    for i in range(100):
        print("-----", i)
        print(gamer)

        gamer.bet()

        print("소지금은 {}원이되었습니다.".format(gamer.money))

        if gamer.money > memento.money:
            print("(많이 증가했으므로 현재 상태를 저장하자.)")
            memento = gamer.create_memento()
        elif gamer.money < memento.money / 2:
            print("(많이 감소했으므로 이전의 상태로 복원하자.)")
            gamer.restore_memento(memento)

        print("")

