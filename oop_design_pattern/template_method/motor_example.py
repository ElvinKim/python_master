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


class HyundaiMotor(object):

    def __init__(self, door):
        self._door = door
        self._motor_status = MOTOR_STATUS.STOPPED

    def move_hyundai_motor(self, direction):
        pass

    @property
    def motor_status(self):
        return self._motor_status

    @motor_status.setter
    def motor_status(self, motor_status):
        self._motor_status = motor_status

    def move(self, direction):
        motor_status = self._motor_status

        if motor_status == MOTOR_STATUS.MOVING:
            return

        door_status = self._door.door_status

        if door_status == DOOR_STATUS.OPENED:
            self._door.close()

        self.move_hyundai_motor(direction)
        self._motor_status = MOTOR_STATUS.MOVING


class LGMotor(object):

    def __init__(self, door):
        self._door = door
        self._motor_status = MOTOR_STATUS.STOPPED


    def move_lg_motor(self, direction):
        pass

    @property
    def motor_status(self):
        return self._motor_status

    @motor_status.setter
    def motor_status(self, motor_status):
        self._motor_status = motor_status

    def move(self, direction):
        if self._motor_status == MOTOR_STATUS.MOVING:
            return

        door_status = self._door.door_status

        if door_status == DOOR_STATUS.OPENED:
            self._door.close()

        self.move_lg_motor(direction) #이 라인을 제외하고는 HyundaiMotor의 move 함수와 동일하다
        self._motor_status = MOTOR_STATUS.MOVING

if __name__ == "__main__":
    door = Door()
    hyundai_motor = HyundaiMotor(door)
    hyundai_motor.move(DIRECTION.UP)


"""
*문제점*
LG 모토를 추가하였는데 상당히 많은 중복 코드를 가진다.
일반적으로 코드의 중복은 유지보수를 어렵게 만든다.
만약 SamsungMotor, OtisMotor 등등 추가되면 중복된 코드는 더욱 많아 질 것이다.
"""


