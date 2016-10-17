import datetime
from  constant import *

class ElevatorManager(object):

    def __init__(self, controller_count):
        self._controllers = [ElevatorController(i) for i in range(controller_count)]
        self._scheduler = ThroughtputScheduler()

    def request_elevator(self, destination, direction):
        """
        스트래티지 패턴을 사용하여 스케줄링을 설계한 것이다.
        """
        hour = datetime.datetime.now().hour

        if hour < 12:
            schedule = ResponseTimeSchedule()
        else:
            schedule = ThroughtputScheduler()

        selected_elevator = schedule.select_elevator(self, destination, direction)
        self._controllers[selected_elevator].goto_floor(destination)


class ElevatorController(object):

    def __init__(self, elevator_id):
        self._elevator_id = elevator_id
        self._cur_floor = 1

    def goto_floor(self, destination):
        print("Elevator [{}] Floor {} => {}".format(self._elevator_id, self._cur_floor, destination))
        self._cur_floor = destination


class ThroughtputScheduler(object):

    def select_elevator(self, manager, destination, direction):
        return 0 #임의로 선택함


class ResponseTimeSchedule(object):

    def select_elevator(self, manager, destination, direction):
        return 1 #임의로 선택함


if __name__ == "__main__":
    elevator_manager = ElevatorManager(3)
    elevator_manager.request_elevator(10, DIRECTION.UP)

"""
*문제점*
엘레베이터 스케줄링 전략이 추가 되거나 동적 스케줄링 방식으로 전략이 선택되도록 하면
해당 스케줄링 전략을 지원하는 클래스를 생성해야 하고
request_elevator 메서드가 수정되어야 한다. 이는 OCP 에 위반된다.
"""