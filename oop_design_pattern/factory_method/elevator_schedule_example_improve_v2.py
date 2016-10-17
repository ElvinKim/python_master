import datetime
from  constant import *

class ScheduleFactory(object):

    @staticmethod
    def get_scheduler(strategy_id):
        if strategy_id == SCHEDULE_STRATEGY_ID.RESPONSE_TIME:
            return ResponseTimeSchedule()
        elif strategy_id == SCHEDULE_STRATEGY_ID.THROUGH_PUT:
            return ThroughtputScheduler()
        elif strategy_id == SCHEDULE_STRATEGY_ID.DYNAMIC:
            if datetime.datetime.now().hour < 12:
                return ResponseTimeSchedule()
            else:
                return ThroughtputScheduler()


class ElevatorManager(object):

    def __init__(self, controller_count, strategy_id):
        self._controllers = [ElevatorController(i) for i in range(controller_count)]
        self._strategy_id = strategy_id

    @property
    def strategy_id(self):
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        self._strategy_id = strategy_id

    def request_elevator(self, destination, direction):
        scheduler = ScheduleFactory.get_scheduler(self._strategy_id)
        print(scheduler)

        selected_elevator = scheduler.select_elevator(self, destination, direction)
        self._controllers[selected_elevator].goto_floor(destination)


class ElevatorController(object):

    def __init__(self, elevator_id):
        self._elevator_id = elevator_id
        self._cur_floor = 1

    def goto_floor(self, destination):
        print("Elevator [{}] Floor {} => {}".format(self._elevator_id, self._cur_floor, destination))
        self._cur_floor = destination


class ThroughtputScheduler(object):
    """
    스케줄링 기능을 제공하는 클래스는 오직 하나의 객체만 생성해서 사용해도 충분하다.
    그러므로 싱글턴(Singleton) 패턴으로 설계하면 좋다.
    """

    def select_elevator(self, manager, destination, direction):
        return 0 #임의로 선택함


class ResponseTimeSchedule(object):
    """
    스케줄링 기능을 제공하는 클래스는 오직 하나의 객체만 생성해서 사용해도 충분하다.
    그러므로 싱글턴(Singleton) 패턴으로 설계하면 좋다.
    """

    def select_elevator(self, manager, destination, direction):
        return 1 #임의로 선택함


if __name__ == "__main__":
    response_time_scheduler = ElevatorManager(2, SCHEDULE_STRATEGY_ID.RESPONSE_TIME)
    response_time_scheduler.request_elevator(10, DIRECTION.UP)

    through_put_scheduler = ElevatorManager(2, SCHEDULE_STRATEGY_ID.THROUGH_PUT)
    through_put_scheduler.request_elevator(10, DIRECTION.UP)

    dynamic_scheduler = ElevatorManager(2, SCHEDULE_STRATEGY_ID.DYNAMIC)
    dynamic_scheduler.request_elevator(10, DIRECTION.UP)










