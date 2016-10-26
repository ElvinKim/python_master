from constant import *

class Lamp(object):
    def turn_on(self):
        print("Lamp On...")


class Alarm(object):
    def start(self):
        print("Alarming...")


class Button(object):

    def __init__(self, alarm, lamp):
        self._alarm = alarm
        self._lamp = lamp
        self._mode = None

    @property
    def alarm(self):
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        self._alarm = alarm

    @property
    def lamp(self):
        return self._lamp

    @lamp.setter
    def lamp(self, lamp):
        self._lamp = lamp

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode

    def pressed(self):
        if self._mode == DEVICE.LAMP:
            lamp.turn_on()
        elif self._mode == DEVICE.ALARM:
            alarm.start()


if __name__ == "__main__":
    alarm = Alarm()
    lamp = Lamp()
    button = Button(alarm, lamp)
    button.mode = DEVICE.LAMP
    button.pressed()

    button.mode = DEVICE.ALARM
    button.pressed()





