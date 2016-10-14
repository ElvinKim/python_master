

class ElevatorManager(object):

    def __init__(self, controller_count):
        self._controllers = [ElevatorController(i) for i in range(controller_count)]
        self._scheduler = ThroughtputScheduler()

    def request_elevator(self, destination, direction):
        selected_elevator = self._scheduler.select_elevator(self, destination, direction)
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