import abc

class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass


class Button(object):

    def __init__(self):
        self._command = None

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command

    def pressed(self):
        self._command.execute()


class Lamp(object):

    def turn_on(self):
        print("Lamp On...")

    def turn_off(self):
        print("Lamp Off...")


class LampCommand(Command):

    def __init__(self, lamp):
        self._lamp = lamp

    def execute(self):
        self._lamp.turn_on()


class Alarm(object):

    def start(self):
        print("Alarming...")


class AlarmCommand(Command):

    def __init__(self, alarm):
        self._alarm = alarm

    def execute(self):
        self._alarm.start()


class LampOffCommand(Command):

    def __init__(self, lamp):
        self._lamp = lamp

    def execute(self):
        self._lamp.turn_off()


if __name__ == "__main__":
    lamp = Lamp()
    lamp_command = LampCommand(lamp)
    lamp_off_command = LampOffCommand(lamp)

    alarm = Alarm()
    alarm_command = AlarmCommand(alarm)

    button = Button()

    button.command = alarm_command
    button.pressed()

    button.command = lamp_command
    button.pressed()

    button.command = lamp_off_command
    button.pressed()