condition = 1

class Factory():

    @classmethod
    def get_instance(cls):
        if condition == 1:
            return X()
        elif condition == 2:
            return Z()
        else:
            return Y()

class X():

    def func1(self):
        print("X:func1")

    def func2(self):
        print("X:func2")

    def func3(self):
        print("X:func3")


class Y():

    def func1(self):
        print("Y:func1")

    def func2(self):
        print("Y:func2")

    def func3(self):
        print("Y:func3")


class Z():

    def func1(self):
        print("Z:func1")

    def func2(self):
        print("Z:func2")

    def func3(self):
        print("Z:func3")


class A():

    def func_a(self):
        a = Factory.get_instance()
        a.func()


class B():

    def func_b(self):
        b = Factory.get_instance()
        b.func2()


class C():

    def func_c(self):
        c = Factory.get_instance()
        c.func3()

"""
만약 condition 이 2일 때 Z 클래스의 객체를 생성하여 기존에 함수를 호출하게 한다면

클래스 A, B, C 모두를 수정해야 한다.

그리고 만약 클래스 X 와 Y의 생성되는 부분이 수정된다면 이 역시 클래스 A, B, C 모두를 수정해야 한다.
"""