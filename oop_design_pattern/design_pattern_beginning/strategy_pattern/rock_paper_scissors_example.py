"""
   _____   _                    _
  / ____| | |                  | |
 | (___   | |_   _ __    __ _  | |_    ___    __ _   _   _
  \___ \  | __| | '__|  / _` | | __|  / _ \  / _` | | | | |
  ____) | | |_  | |    | (_| | | |_  |  __/ | (_| | | |_| |
 |_____/   \__| |_|     \__,_|  \__|  \___|  \__, |  \__, |
                                              __/ |   __/ |
                                             |___/   |___/

* 언제 사용하는가?
    - 동일 계열의 알고리즘군을 정의하고 각각의 알고리즘을 캡슐화하고 이 알고리즘을 상호적으로 교환할 수 있게 해주는 패턴.
    - 이 알고리즘을 다양하게 추가할 수 있고 사용자와 독립적으로 확장 가능함.

* 주요 특징은 무엇인가?
    - 실행중에 동적으로 클래스를 교체하며 동작 방식을 바꿀 수 있다.

* 생각해 볼 수 있는 사용 예
    - RPG 게임에서 공격 버튼을 누를 때 무기가 바뀔 때마다 공격 액션이 달라지는 로직
"""

import abc
import random

ROCK = 0
SCISSORS = 1
PAPER = 2


class Hand(object):

    def __init__(self, hand_value):
        self._hand_value = hand_value

    @property
    def hand_value(self):
        return self._hand_value

    def is_stronger_than(self, hand):
        return self._fight(hand) == 1

    def is_weaker_than(self, hand):
        return self._fight(hand) == -1

    def _fight(self, hand):
        if self.hand_value == hand.hand_value:
            return 0
        elif (self.hand_value + 1) % 3 == hand.hand_value:
            return 1
        else:
            return -1


class HandFactory(object):

    hand = [Hand(ROCK), Hand(SCISSORS), Hand(PAPER)]

    @classmethod
    def get_hand(cls, hand_value):
        return cls.hand[hand_value]


class Strategy(abc.ABC):

    @abc.abstractmethod
    def next_hand(self):
        pass

    @abc.abstractmethod
    def study(self, win):
        pass


class WinningStrategy(Strategy):

    def __init__(self):
        self._won = False
        self._pre_hand = None

    def next_hand(self):
        if not self._won:
            self._pre_hand = HandFactory.get_hand(random.randint(0, 2))

        return  self._pre_hand

    def study(self, win):
        self._won = win


class ProbStrategy(Strategy):

    def __init__(self):
        self._prev_hand_value = 0
        self._current_hand_value = 0
        self._history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

    def next_hand(self):
        bet = random.randint(1, self._get_sum(self._current_hand_value))
        hand_value = 0

        if bet < self._history[self._current_hand_value][0]:
            hand_value = 0
        elif bet < self._history[self._current_hand_value][0] + self._history[self._current_hand_value][1]:
            hand_value = 1
        else:
            hand_value = 2
        self._prev_hand_value = self._current_hand_value
        self._current_hand_value = hand_value

        return HandFactory.get_hand(hand_value)

    def _get_sum(self, hv):
        sum = 0

        for i in range(3):
            sum += self._history[hv][i]

        return sum

    def study(self, win):
        if win:
            self._history[self._prev_hand_value][self._current_hand_value] += 1
        else:
            self._history[self._prev_hand_value][(self._current_hand_value + 1) % 3] += 1
            self._history[self._prev_hand_value][(self._current_hand_value + 2) % 3] += 1


class Player(object):

    def __init__(self, name, strategy):
        self._name = name
        self._strategy = strategy
        self._win_count = 0
        self._lose_count = 0
        self._game_count = 0

    def next_hand(self):
        return self._strategy.next_hand()

    def win(self):
        self._strategy.study(True)
        self._win_count += 1
        self._game_count += 1

    def lose(self):
        self._strategy.study(False)
        self._lose_count += 1
        self._game_count += 1

    def even(self):
        self._game_count += 1

    def __str__(self):
        return "[{} : game count - {}, win count - {}, lose count - {}]"\
            .format(self._name, self._game_count, self._win_count, self._lose_count)


if __name__ == "__main__":
    player1 = Player("하나", WinningStrategy())
    player2 = Player("두리", WinningStrategy())

    for _ in range(100):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()

        if next_hand1.is_stronger_than(next_hand2):
            print("Winner : ", player1)
            player1.win()
            player2.lose()
        elif next_hand2.is_stronger_than(next_hand1):
            print("Winner : ", player2)
            player2.win()
            player1.lose()
        else:
            print("Even...")
            player1.even()
            player2.even()

    print("total result:")
    print(player1)
    print(player2)