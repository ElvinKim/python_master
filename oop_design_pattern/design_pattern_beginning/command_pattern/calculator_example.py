"""
   _____                                                       _
  / ____|                                                     | |
 | |        ___    _ __ ___    _ __ ___     __ _   _ __     __| |
 | |       / _ \  | '_ ` _ \  | '_ ` _ \   / _` | | '_ \   / _` |
 | |____  | (_) | | | | | | | | | | | | | | (_| | | | | | | (_| |
  \_____|  \___/  |_| |_| |_| |_| |_| |_|  \__,_| |_| |_|  \__,_|




* 언제 사용하는가?
    - 요청(명령)을 객체의 형태로 캡슐화하여 서로 요청이 다른 사용자의 매개변수화, 요청 저장 또는 로깅,
      그리고 연산의 취소를 지원하게 만드는 패턴

* 주요 특징은 무엇인가?
    - 명령들의 이력을 저장하면 그 동안 수행한 명령들을 재 실행할 수 있음

* 구성요소
    - Command : 명령의 인터페이스(API)
    - ConcreteCommand : Command 역할의 인터페이스(API)를 실제고 구현하는 역할. 일반적으로 execute 함수의 실제 구현
    - Receiver : Command 가 명령에 대한 실행(처리)할 때 처리의 대상
    - Invoker : Command 역할에서 정의되는 인터페이스(API)를 호출하는 역할
    - Client : ConcreteCommand를 생성하고 Receiver를 할당하는 역할
"""


import abc


class Operand(object):

    def __init__(self, first_op, second_op):
        self._first_op = first_op
        self._second_op = second_op

    @property
    def first_op(self):
        return self._first_op

    @property
    def second_op(self):
        return self._second_op


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass


class PlusCommand(Command):

    def __init__(self, operands):
        self._operands = operands

    def execute(self):
        first_op = self._operands.first_op
        second_op = self._operands.second_op

        print("{} + {} = {}".format(first_op, second_op, first_op + second_op))


class SubtractCommand(Command):

    def __init__(self, operands):
        self._operands = operands

    def execute(self):
        first_op = self._operands.first_op
        second_op = self._operands.second_op

        print("{} - {} = {}".format(first_op, second_op, first_op - second_op))


class Calculator(object):

    def __init__(self):
        self._command = None

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command

    def print_result(self):
        self._command.execute()

if __name__ == "__main__":
    operand = Operand(10, 20)

    plus_command = PlusCommand(operand)
    sub_command = SubtractCommand(operand)

    calculator = Calculator()

    calculator.command = plus_command
    calculator.print_result()

    calculator.command = sub_command
    calculator.print_result()

