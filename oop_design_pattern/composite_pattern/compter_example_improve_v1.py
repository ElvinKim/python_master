
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


class Computer(object):

    _body = None
    _keyboard = None
    _monitor = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def keyboard(self):
        return self._keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self._keyboard = keyboard

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    def get_price(self):
        price_list = list()
        price_list.append(self._body.price)
        price_list.append(self._keyboard.price)
        price_list.append(self._monitor.price)

        return sum(price_list)

    def get_max_price(self):
        price_list = list()
        price_list.append(self._body.price)
        price_list.append(self._keyboard.price)
        price_list.append(self._monitor.price)

        return max(price_list)

    def get_power(self):
        power_list = list()
        power_list.append(self._body.power)
        power_list.append(self._keyboard.power)
        power_list.append(self._monitor.power)

        return sum(power_list)

    def get_max_power(self):
        power_list = list()
        power_list.append(self._body.power)
        power_list.append(self._keyboard.power)
        power_list.append(self._monitor.power)

        return max(power_list)

if __name__ == "__main__":

    body = Body(100, 70)
    keyboard = Keyboard(5, 2)
    monitor = Monitor(20, 30)

    computer = Computer()
    computer.body = body
    computer.keyboard = keyboard
    computer.monitor = monitor

    print("Compter Power : {}W".format(computer.get_power()))
    print("Compter Price : {}만원".format(computer.get_price()))

"""
*문제점*
만약 부품으로 Speaker가 추가된다고 가정해 보자.
그러면 4개의 함수 get_price, get_power, get_max_price, get_max_power를 모두 수정 해야 한다.
이는 OCP를 위반하며 만약 함수의 수가 더 많았다면 수정해야 하는 부분이 더욱 많아질 것이다.
"""