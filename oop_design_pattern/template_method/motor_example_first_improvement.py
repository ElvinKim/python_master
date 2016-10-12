import abc
from constant import *

class Door(object):

    def __init__(self):
        self._door_status = None

    @property
    def door_status(self):
        return self._door_status

    def close(self):
        self._door_status = DOOR_STATUS.CLOSED

    def open(self):
        self._door_status = DOOR_STATUS.OPENED


class Motor(abc.ABC):

    def __init__(self, door):
        self._door = door
        self._motor_status = MOTOR_STATUS.STOPPED

    @property
    def motor_status(self):
        return self._motor_status

    @motor_status.setter
    def motor_status(self, motor_status):
        self._motor_status = motor_status


class HyundaiMotor(Motor):

    def __init__(self, door):
        super().__init__(door)

    def _move_hyundai_motor(self, direction):
        print("move Hyundai Motor : ", direction)

    def move(self, direction):
        if self._motor_status == MOTOR_STATUS.MOVING:
            return

        if self._door.door_status == DOOR_STATUS.OPENED:
            self._door.close()

        self._move_hyundai_motor(direction)
        self._motor_status = MOTOR_STATUS.MOVING


class LGMotor(Motor):

    def __init__(self, door):
        super().__init__(door)

    def _move_lg_motor(self, direction):
        print("move LG Motor : ", direction)

    def move(self, direction):
        if self._motor_status == MOTOR_STATUS.MOVING:
            return

        if self._door.door_status == DOOR_STATUS.OPENED:
            self._door.close()

        self._move_lg_motor(direction)
        self._motor_status = MOTOR_STATUS.MOVING


if __name__ == "__main__":
    door = Door()
    hyundai_motor = HyundaiMotor(door)
    hyundai_motor.move(DIRECTION.UP)

    lg_motor = LGMotor(door)
    lg_motor.move(DIRECTION.UP)

"""
*문제점*
두 클래스의 로직이 똑같은 메소드(완전히 중복되는 메소드)에 대해서는 Motor 클래스를 상속받아서 중복을 피했다.
하지만 move 메소드는 비교해보면 한 라인을 제외하곤 다른 모든 로직이 똑같아서 코드 중복의 문제가 있다.
즉 완전히 중복되지는 않지만 부분적으로 중복되는 경우에도 상속을 활용해서 중복을 피할 방법을 찾아야 한다.
"""

