"""
 __      __  _         _   _
 \ \    / / (_)       (_) | |
  \ \  / /   _   ___   _  | |_    ___    _ __
   \ \/ /   | | / __| | | | __|  / _ \  | '__|
    \  /    | | \__ \ | | | |_  | (_) | | |
     \/     |_| |___/ |_|  \__|  \___/  |_|


* 언제 사용하는가?
    - 데이터의 구조와 처리를 분리하는 패턴
    - 데이터 구조를 돌아다니는 주체인 '방문자'를 나타내는 클래스를 준비해서 그 클래스에게 처리를 위임하는 구조


* 주요 특징은 무엇인가?
    - element.accept(visitor)
    visitor.visit(element)
    이 두가지만 보면 완전히 반대의 관계에 있음.

    - ConcreteElement역할과 ConcreteVisitor역할을 하는 한 쌍에 의해 처리됨
        -> 이것을 일반적으로 더블 디스패치(Double Dispatch :이중 분리)라고 함.
"""

import abc
from functools import singledispatch
from functools import update_wrapper


def method_dispatch(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)
    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


class Element(abc.ABC):

    @abc.abstractmethod
    def accept(self, v):
        pass


class Entry(Element):

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    def add(self, entry):
        pass

    def accept(self, v):
        pass

    def __str__(self):
        return "{}({})".format(self.name, self.size)


class File(Entry):

    def __init__(self, name, size):
        self._name = name
        self._size = size

    def accept(self, v):
        v.visit(self)


class Directory(Entry):

    def __init__(self, name):
        self._name = name
        self._directory = list()

    @property
    def size(self):
        return sum([each_file.size for each_file in self._directory])

    @property
    def file_list(self):
        return self._directory

    def add(self, entry):
        self._directory.append(entry)
        return self

    def accept(self, v):
        v.visit(self)

class Visitor(abc.ABC):

    @singledispatch
    @abc.abstractmethod
    def visit(self, entry):
        pass

    @visit.register(File)
    @abc.abstractmethod
    def _(self, file):
        pass

    @visit.register(Directory)
    @abc.abstractmethod
    def _(self, directory):
        pass


class ListVisitor(Visitor):

    def __init__(self):
        self._current_dir = ""

    @method_dispatch
    def visit(self, entry):
        print("visit call")

    @visit.register(File)
    def _(self, file):
        print("{}/{}".format(self._current_dir, file))

    @visit.register(Directory)
    def _(self, directory):
        print("{}/{}".format(self._current_dir, directory))
        save_dir = self._current_dir
        self._current_dir += "/" + directory.name

        for entry in directory.file_list:
            entry.accept(self)

        self._current_dir = save_dir


if __name__ == "__main__" :
    print("Making root entries...")
    root_dir = Directory("root")
    bin_dir = Directory("bin")
    tmp_dir = Directory("tmp")
    usr_dir = Directory("usr")

    root_dir.add(bin_dir)
    root_dir.add(tmp_dir)
    root_dir.add(usr_dir)

    bin_dir.add(File('vi', 10000))
    bin_dir.add(File('latex', 20000))
    root_dir.accept(ListVisitor())

    print("Visiting bin entries...")
    bin_dir.accept(ListVisitor())

    print("Making user entries...")

    kim = Directory("kim")
    lee = Directory("lee")
    park = Directory("park")

    usr_dir.add(kim)
    usr_dir.add(lee)
    usr_dir.add(park)

    kim.add(File("diary.html", 100))
    kim.add(File("composite.java", 200))
    lee.add(File("memo.tex", 300))
    park.add(File("game.doc", 400))
    park.add(File("june.mail", 500))

    root_dir.accept(ListVisitor())