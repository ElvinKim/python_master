import abc
from constant import *

class Door(abc.ABC):

    def __init__(self):
        self._door_status = DOOR_STATUS.CLOSED

    @property
    def door_status(self):
        return self._door_status

    def close(self):
        if self._door_status == DOOR_STATUS.CLOSED:
            return

        self.do_close()
        self._door_status = DOOR_STATUS.CLOSED

    @abc.abstractmethod
    def do_close(self):
        pass

    def open(self):
        if self._door_status == DOOR_STATUS.OPENED:
            return

        self.do_open()
        self._door_status = DOOR_STATUS.OPENED

    @abc.abstractmethod
    def do_open(self):
        pass


class LGDoor(Door):

    def __init__(self):
        super().__init__()

    def do_close(self):
        print("close LG Door")

    def do_open(self):
        print("open LG Door")


class HyundaiDoor(Door):

    def __init__(self):
        super().__init__()

    def do_close(self):
        print("close Hyundai Door")

    def do_open(self):
        print("open Hyundai Door")


class SamsungDoor(Door):

    def __init__(self):
        super().__init__()

    def do_close(self):
        print("close Samsung Door")

    def do_open(self):
        print("open Samsung Door")


class Motor(abc.ABC):

    def __init__(self):
        self._door = None
        self._motor_status = MOTOR_STATUS.STOPPED

    @property
    def motor_status(self):
        return self._motor_status

    @motor_status.setter
    def motor_status(self, motor_status):
        self._motor_status = motor_status

    @property
    def door(self):
        return self._door

    @door.setter
    def door(self, door):
        self._door = door

    def move(self, direction):
        if self._motor_status == MOTOR_STATUS.MOVING:
            return

        if self._door.door_status == DOOR_STATUS.OPENED:
            self._door.close()

        self._move_motor(direction)
        self._motor_status = MOTOR_STATUS.MOVING

    @abc.abstractmethod
    def _move_motor(self, dirction):
        pass


class HyundaiMotor(Motor):

    def __init__(self):
        super().__init__()

    def _move_motor(self, direction):
        print("move Hyundai Motor : ", direction)


class LGMotor(Motor):

    def __init__(self):
        super().__init__()

    def _move_motor(self, direction):
        print("move LG Motor : ", direction)


class SamsungMotor(Motor):

    def __init__(self):
        super().__init__()

    def _move_motor(self, direction):
        print("move Samsung Motor : ", direction)


class ElevatorFactory(abc.ABC):

    @abc.abstractmethod
    def create_motor(self):
        pass

    @abc.abstractmethod
    def create_door(self):
        pass


class LGEelevatorFactory(ElevatorFactory):

    def create_motor(self):
        return LGMotor()

    def create_door(self):
        return LGDoor()


class HyundaiElevatorFactory(ElevatorFactory):

    def create_motor(self):
        return HyundaiMotor()

    def create_door(self):
        return HyundaiDoor()


class SamsungElevatorFactory(ElevatorFactory):

    def create_motor(self):
        return SamsungMotor()

    def create_door(self):
        return SamsungDoor()


class ElevatorFactoryFactory() :

    @classmethod
    def get_factory(cls, vendor_id):
        if vendor_id == VENDOR_ID.LG:
            return LGEelevatorFactory()
        elif vendor_id == VENDOR_ID.HYUNDAI:
            return HyundaiElevatorFactory()
        elif vendor_id == VENDOR_ID.SAMSUNG:
            return SamsungElevatorFactory()


if __name__ == "__main__":
    vendor_id = VENDOR_ID.SAMSUNG

    factory = ElevatorFactoryFactory.get_factory(vendor_id)

    motor = factory.create_motor()
    door = factory.create_door()

    motor.door = door

    door.open()
    motor.move(DIRECTION.DOWN)

"""
*Key Point*
추상 팩토리(Abstract Factory)는 관련성 있는 여러 종류의 객체를 일관된 방식으로 생성할 때 유용하다.
"""