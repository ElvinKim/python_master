from enum import Enum

DOOR_STATUS = Enum("DOOR_STATUS", "CLOSED OPENED")
MOTOR_STATUS = Enum("MOTOR_STATUS", "MOVING STOPPED")


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



