
class ComputerDevice(object):
    def __init__(self, power, price):
        self._power = power
        self._price = price

    @property
    def power(self):
        return self._power

    @property
    def price(self):
        return self._price


class Keyboard(ComputerDevice):

    def __init__(self, power, price):
        super().__init__(power, price)


class Body(ComputerDevice):

    def __init__(self, power, price):
        super().__init__(power, price)


class Monitor(ComputerDevice):

    def __init__(self, power, price):
        super().__init__(power, price)


class Speaker(ComputerDevice):

    def __init__(self, power, price):
        super().__init__(power, price)


class Computer(object):

    def __init__(self):
        self._component_list = list()
        self._body = None
        self._keyboard = None
        self._monitor = None
        self._speaker = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body
        self._component_list.append(body)

    @property
    def keyboard(self):
        return self._keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self._keyboard = keyboard
        self._component_list.append(keyboard)

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor
        self._component_list.append(monitor)

    @property
    def speaker(self):
        return self._speaker

    @speaker.setter
    def speaker(self, speaker):
        self._speaker = speaker
        self._component_list.append(speaker)

    def get_price(self):
        return sum([component.price for component in self._component_list])

    def get_max_price(self):
        return max([component.price for component in self._component_list])

    def get_power(self):
        return sum([component.power for component in self._component_list])

    def get_max_power(self):
        return max([component.power for component in self._component_list])

if __name__ == "__main__":

    body = Body(100, 70)
    keyboard = Keyboard(5, 2)
    monitor = Monitor(20, 30)
    speaker = Monitor(10, 10)

    computer = Computer()
    computer.body = body
    computer.keyboard = keyboard
    computer.monitor = monitor
    computer.speaker = speaker

    print("Compter Power : {}W".format(computer.get_power()))
    print("Compter Price : {}만원".format(computer.get_price()))

"""
*복합체(Composite Pattern)*
객체들의 관계를 트리 구조로 구성하여 부분-전체 계층을 포현하는 패턴으로,
사용자가 단일 객체와 복합 객체 모두 동일하게 다루도록 한다.
출처 : GoF 디자인 패턴
"""