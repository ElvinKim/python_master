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


class MotorFactory(object):

    @classmethod
    def create_motor(cls, vendor_id):
        if vendor_id == VENDOR_ID.LG:
            return LGMotor()
        elif vendor_id == VENDOR_ID.HYUNDI:
            return HyundaiMotor()

class DoorFactory(object):

    @classmethod
    def create_door(cls, vendor_id):
        if vendor_id == VENDOR_ID.LG:
            return LGDoor()
        elif vendor_id == VENDOR_ID.HYUNDI:
            return HyundaiDoor()


if __name__ == "__main__":
    vendor_id = VENDOR_ID.LG

    door = DoorFactory.create_door(vendor_id)
    motor = MotorFactory.create_motor(vendor_id)

    motor.door = door

    door.open()
    motor.move(DIRECTION.UP)


"""
*문제점*
* 만약 다른 제조 업체의 부품을 사용해야 한다면? 예를 들어 지금은 LG 의 부품을 사용하지만 Hyundi 부품을 사용해야 한다면?

    vendor_id = VENDOR_ID.Hyundai <- 여기만 수정하면 됨

    door = DoorFactory.create_door(vendor_id)
    motor = MotorFactory.create_motor(vendor_id)

    motor.door = door

    door.open()
    motor.move(DIRECTION.UP)

* 새로운 제조 업체의 부품을 지원해야 한다면? 삼성에서 엘레베이터 부품을 시작해서 지원해야 한다면?

    @classmethod
    def create_motor(cls, vendor_id):
        if vendor_id == VENDOR_ID.LG:
            return LGMotor()
        elif vendor_id == VENDOR_ID.HYUNDI:
            return HyundaiMotor()
        elif vendor_id == VENDOR_ID.SAMSUNG
            return SamsungMotor()


    @classmethod
    def create_door(cls, vendor_id):
        if vendor_id == VENDOR_ID.LG:
            return LGDoor()
        elif vendor_id == VENDOR_ID.HYUNDI:
            return HyundaiDoor()
        elif vendor_id == VENDOR_ID.SAMSUNG
            return SamsungDoor()

기존 코드를 수정해야 하는 부분이 많다. 지금이야 Door와 Motor 2개만 있어서 수정해야 할 곳이 적지만
만약 Sensor, Speaker 등등 더 있었다면 수정해야 할 곳이 많이 진다.
*
"""