
from evalsupport import deco_alpha

print("<[1]> evaltime module start")

class ClassOne():
    print("<[2]> ClassOne body")

    def __init__(self):
        print("<[3]> ClassOne:__init__")

    def __del__(self):
        print("<[4]> ClassOne:__del__")

    def method_x(self):
        print("<[5]> ClassOne:method_x")

    class ClassTwo(object):
        print("<[6]> ClassTwo body")


@deco_alpha
class ClassThree():
    print("<[7]> ClassThree body")

    def method_y(self):
        print("<[8]> ClassThree.method_y")


class ClassFour(ClassThree):
    print("<[9]> ClassFour body")

    def method_y(self):
        print("<[10]> ClassFour.method_y")


if __name__ == "__main__":
    print("<[11]> ClassOne tests", 30 * ".")
    one = ClassOne()
    one.method_x()

    print("<[12]> ClassThree tests", 30 * ".")
    three = ClassThree()
    three.method_y()

    print("<[13]> ClassFour tests", 30 * ".")
    four = ClassFour()
    four.method_y()


print("<[14]> evaltime module end")


"""
Key Point
* ClassThree의 본체를 평가한 뒤 데커레이터 함수를 실행했다
 - 당연하다 데커레이터 함수가 처리할 클래스 객체를 받아야 하므로 객체를 먼저 생성하는 것은 당연하다.

* ClassFour 는 ClassThree를 상속 받았지만 데커레이터가 서브클래스(ClassFour)에 영향을 주지 않을 수 있다는 점이다
"""
