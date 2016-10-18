import threading

class Printer(object):
    """
    *todo
     - Printer()로 객체를 생성할 수 없게 막는 기능
    """
    _printer = None

    @classmethod
    def get_printer(cls):
        if cls._printer is None:
            cls._printer = Printer()
        return cls._printer

    def print(self, contents):
        print(contents)

class User(object):

    def __init__(self, name):
        self._name = name

    def print(self):
        printer = Printer.get_printer()
        printer.print("[printer id : {}][user : {}]".format(id(printer), self._name))


if __name__ == "__main__":
    user_list = [User(str(num) + "-user") for num in range(5)]
    thread_list = [threading.Thread(target=user_list[n].print) for n in range(5)]

    for n in range(5):
        thread_list[n].start()




