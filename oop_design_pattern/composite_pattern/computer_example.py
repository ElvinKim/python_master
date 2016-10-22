
class Keyboard(object):

    def __init__(self, power, price):
        self._power = power
        self._price = price

    @property
    def power(self):
        return self._power

    @property
    def price(self):
        return self._price


class Body(object):

    def __init__(self, power, price):
        self._power = power
        self._price = price

    @property
    def power(self):
        return self._power

    @property
    def price(self):
        return self._price


class Monitor(object):

    def __init__(self, power, price):
        self._power = power
        self._price = price

    @property
    def power(self):
        return self._power

    @property
    def price(self):
        return self._price


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

    def get_power(self):
        power_list = list()
        power_list.append(self._body.power)
        power_list.append(self._keyboard.power)
        power_list.append(self._monitor.power)

        return sum(power_list)


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