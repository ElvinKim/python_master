"""
   _____   _             _
  / ____| | |           | |
 | (___   | |_    __ _  | |_    ___
  \___ \  | __|  / _` | | __|  / _ \
  ____) | | |_  | (_| | | |_  |  __/
 |_____/   \__|  \__,_|  \__|  \___|



* 언제 사용하는가?
    - 객체 내부의 상태에 따라 스스로 행동을 변경할 수 있게끔 허가하는 패턴

* 주요 특징은 무엇인가?
    - 상태에 따라 if-else if - else 문을 사용하는 것을 상태에 따른 행동 변화로 구현함
    - if-else if - else으로 처리하면 상태가 추가 될 때마다 이전 코드를 수정해야 함
    - 상태라는 것을 클래스로 표현함으로써 복잡한 프로그램을 분할하여 처리할 수 있음
    - 상태 전환에서 ConcreateState가 상태 전환 동작을 수행하면 장단점이 생김
        - 장점 : 다른 상태로 전환하는 시점이 언제인지를 한의 클래스내에 정리되어 있다는 점
        - 단점 : 하나의 ConcreateState가 다른 ConcreateState의 역할을 알아야 한다는 점
            -> 이는 특정 클래스 삭제시 이를 전환하는 클래스도 수정해야함을 의미

* 구성요소
    - State : 상태를 나타내는 클래스. 상태가 변할 때마다 다른 동작을 하는 인터페이스를 결정.
    - ConcreateState : 구체적인 각각의 상태를 표현.
    - Context : 현재 상태를 나타내는 ConcreateState의 역할을 가짐. State 의 이용 패턴을 사용자에게 제공.
"""


import abc
from singleton import Singleton
import time


class State(metaclass=Singleton):

    @abc.abstractmethod
    def do_clock(self, context, hour):
        """시간 설정"""

    @abc.abstractmethod
    def do_use(self, context):
        """금고 사용"""

    @abc.abstractmethod
    def do_alarm(self, context):
        """비상벨"""

    @abc.abstractmethod
    def do_phone(self, context):
        """일반통화"""


class DayState(State):

    def do_clock(self, context, hour):
        if hour < 9 or hour >= 17:
            context.change_state(NightState())

    def do_use(self, context):
        context.record_log("금고사용(주간)")

    def do_alarm(self, context):
        context.call_security_center("비상벨(주간)")

    def do_phone(self, context):
        context.call_security_center("일반통화(주간)")

    def __str__(self):
        return "[주간]"


class NightState(State):

    def do_clock(self, context, hour):
        if 9 <= hour < 17:
            context.change_state(DayState())

    def do_use(self, context):
        context.call_security_center("비상 : 야간금고 사용!")

    def do_alarm(self, context):
        context.call_security_center("비상벨(야간)")

    def do_phone(self, context):
        context.call_security_center("야간통화 녹음")

    def __str__(self):
        return "[야간]"


class SafeFrame(object):

    def __init__(self):
        self._state = DayState()

    def click_use_btn(self):
            self._state.do_use(self)

    def click_alarm_btn(self):
        self._state.do_alarm(self)

    def click_phone_btn(self):
        self._state.do_phone(self)

    def set_clock(self, hour):
        clock_string = "현재시간은 {}:00".format(str(hour).zfill(2))
        print(clock_string)
        self._state.do_clock(self, hour)

    def change_state(self, state):
        print("{}에서 {}로 상태가 변화했습니다.".format(self._state, state))
        self._state = state

    def call_security_center(self, msg):
        print("Call! ", msg)

    def record_log(self, msg):
        print("record ...", msg)


if __name__ == "__main__":

    frame = SafeFrame()

    for hour in range(24):
        print("-*" * 10, hour, "-*" * 10)
        frame.set_clock(hour)
        frame.click_use_btn()
        frame.click_alarm_btn()
        frame.click_phone_btn()
        time.sleep(1)
