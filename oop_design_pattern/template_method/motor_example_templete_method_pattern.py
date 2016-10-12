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

    def __init__(self, door):
        super().__init__(door)

    def _move_motor(self, direction):
        print("move Hyundai Motor : ", direction)


class LGMotor(Motor):

    def __init__(self, door):
        super().__init__(door)

    def _move_motor(self, direction):
        print("move LG Motor : ", direction)


if __name__ == "__main__":
    door = Door()
    hyundai_motor = HyundaiMotor(door)
    hyundai_motor.move(DIRECTION.UP)

    lg_motor = LGMotor(door)
    lg_motor.move(DIRECTION.DOWN)

"""
템플릿 메소드 패턴(Templete Method Pattern) 은 전체적으로는 동일하면서 부분적으로는 다른 구문으로 구성된 메서드의 코드 중복을 최소화 할때 사용하면 좋다.
즉 동일한 기능을 상위 클래스에서 정의하면서 확장/변화가 필요한 부분만 서브 클래스에서 구현할 수 있도록 한다.
위와 같이 공통 부분은 상위클래스에서 정의하고 확장 혹은 변화되는 부분을 서브 클래스에서 오버라이드 하여 구현하고 호출하는 방식으로 구현한다.
여기서 오버라이드될 필요가 있는 메소드를 primitive 혹은 hook 메소드라고 한다.

-KeyPoint-
템플릿 메소드 패턴은 전체적인 알고리즘은 상위 클래스에서 구현하면서 다른 부분은 하위 클래스에서 구현할 수 있도록 하는 디자인 패턴이다.
전체적인 알고리즘 코드를 재사용하는데 유용하다.

*출처*
(UML 과 GoF 디자인 패턴 핵심 10가지로 배우는)Java  객체지향 디자인 패턴
"""