"""
  _____           _                                         _
 |_   _|         | |                                       | |
   | |    _ __   | |_    ___   _ __   _ __    _ __    ___  | |_    ___   _ __
   | |   | '_ \  | __|  / _ \ | '__| | '_ \  | '__|  / _ \ | __|  / _ \ | '__|
  _| |_  | | | | | |_  |  __/ | |    | |_) | | |    |  __/ | |_  |  __/ | |
 |_____| |_| |_|  \__|  \___| |_|    | .__/  |_|     \___|  \__|  \___| |_|
                                     | |
                                     |_|


* 언제 사용하는가?
    - 주어진 언어에 대한 그 언어의 문법을 위한 표현 수단을 정의하고,
      이와 어울러 그 표현 수단을 사용하여 해당 언어로 작성된 문장을 해석하는 해석기를 정의하는 패턴

* 주요 특징은 무엇인가?
    - 그 외 미니 언어 : 정규 표현, 검색용 표현, 일괄(batch) 처리 언어

* 구성요소
    - AbstractExpression : 구문 트리의 노드에 공통의 인터페이스(API)를 결정하는 역할
    - TerminalExpression : BNF(Backus Normal Form)의 TerminalExpression에 대응하는 역할
    - NonterminalExpression : BNF의 NonterminalExpression에 대응하는 역할
    - Context : 인터프리터가 구문해석을 실행하기 위한 정보를 제공하는 역할
    - Client : 구문 트리를 조립하기 위해서 TerminalExpression과 NonterminalExpression을 호출하는 역할
"""


import abc
import re


class Node(abc.ABC):

    @abc.abstractmethod
    def parse(self, context):
        pass


class Context(object):

    def __init__(self, text):
        self._tokens = re.split('\s+', text)
        self._current_token = None
        self.next_token()

    def next_token(self):
        if len(self._tokens) != 0:
            self._current_token = self._tokens.pop(0)
        else:
            self._current_token = None
        return self._current_token

    def current_token(self):
        return self._current_token

    def skip_token(self, token):
        if token != self._current_token:
            raise ValueError("Warning {} is expected but {} is found".format(token, self._current_token))

        self.next_token()

    def current_number(self):
        return int(self._current_token)


class RepeatCommandNode(Node):

    def __init__(self):
        self._number = None
        self._command_list_node = None

    def parse(self, context):
        context.skip_token("repeat")
        self._number = context.current_number()
        context.next_token()
        self._command_list_node = CommandListNode()
        self._command_list_node.parse(context)

    def __str__(self):
        return "[repeat {} {}]".format(self._number, self._command_list_node)


class PrimitiveCommandNode(Node):

    def __init__(self):
        self._name = None

    def parse(self, context):
        self._name = context.current_token()
        context.skip_token(self._name)

        if self._name != 'go' and self._name != 'right' and self._name != 'left':
            raise ValueError("{} is undefined".format(self._name))

    def __str__(self):
        return self._name


class CommandNode(Node):

    def __init__(self):
        self._node = None

    def parse(self, context):
        if context.current_token() == "repeat":
            self._node = RepeatCommandNode()
            self._node.parse(context)
        else:
            self._node = PrimitiveCommandNode()
            self._node.parse(context)

    def __str__(self):
        return self._node.__str__()


class CommandListNode(Node):

    def __init__(self):
        self._list = list()

    def parse(self, context):
        while True:
            if context.current_token() is None:
                raise ValueError("Missing 'end'")
            elif context.current_token() == "end":
                context.skip_token("end")
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self._list.append(command_node)

    def __str__(self):
        node_list = []
        for node in self._list:
            node_list.append(node.__str__())

        return "[{}]".format(" ".join(node_list))


class ProgramNode(Node):

    def __init__(self):
        self._command_list_node = []

    def parse(self, context):
        context.skip_token("program")
        self._command_list_node = CommandListNode()
        self._command_list_node.parse(context)

    def __str__(self):
        return "[program {}]".format(self._command_list_node)


if __name__ == "__main__":
    with open("program.txt") as f:
        for text in f.readlines():
            print("text = \"{}\"".format(text.strip()))
            node = ProgramNode()
            node.parse(Context(text))
            print("node = ", node)
            print("-*" * 50)
