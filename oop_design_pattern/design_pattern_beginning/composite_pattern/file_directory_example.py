"""
   _____                                             _   _
  / ____|                                           (_) | |
 | |        ___    _ __ ___    _ __     ___    ___   _  | |_    ___
 | |       / _ \  | '_ ` _ \  | '_ \   / _ \  / __| | | | __|  / _ \
 | |____  | (_) | | | | | | | | |_) | | (_) | \__ \ | | | |_  |  __/
  \_____|  \___/  |_| |_| |_| | .__/   \___/  |___/ |_|  \__|  \___|
                              | |
                              |_|

* 언제 사용하는가?
    - 그릇과 내용물을 동일시하는 패턴.(복수와 단수 역시 동실시 한다고 할 수 있다.)
    - 그릇과 내용물을 동일시하여 재귀적인 구조를 만들기 위한 디자인 패턴
    - 객체들의 관계를 트리 구조로 구성하여 부분-전체 계층을 표현하는 패턴

* 주요 특징은 무엇인가?
    - 사용자가 단일 객체와 복합 객체를 모두 동일하게 다루도록 한다.
"""

import abc

class Entry(abc.ABC):

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @abc.abstractmethod
    def print_list(self, prefix):
        pass

    def add(self, entry):
        pass

    def __str__(self):
        return "{}({})".format(self.name, self.size)

class File(Entry):

    def __init__(self, name, size):
        self._name = name
        self._size = size

    def print_list(self, prefix):
        print("{}/{}".format(prefix, self))


class Directory(Entry):

    def __init__(self, name):
        self._name = name
        self._directory = list()

    @property
    def size(self):
        return sum([each_file.size for each_file in self._directory])

    def add(self, entry):
        self._directory.append(entry)
        return self

    def print_list(self, prefix):
        print("{}/{}".format(prefix, self))

        for each_entry in self._directory:
            each_entry.print_list("{}/{}".format(prefix, self.name))


if __name__ == "__main__":
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

    root_dir.print_list("")
    print("-----------------------------------------")
    print("Making root entries...")
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
    root_dir.print_list("")