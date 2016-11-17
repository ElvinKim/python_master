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
