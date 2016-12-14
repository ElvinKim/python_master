from descriptorkinds import *


class Over:

    def __get__(self, instance, owner):
        print("__get__, owner : ", owner)

    def __set__(self, instance, value):
        print("__set__, value : ", value)


class ManagedClass:
    a = Over()
    b = 20

    def __init__(self):
        self.a = 20
        self.b = 40


if __name__ == "__main__":
    obj = Managed()
    print("obj.over : ", obj.over)
    print("obj.over_no_get : ", obj.over_no_get)
    print("obj.non_over : ", obj.non_over)

    print("-*" * 30)
    obj.over = 1
    obj.over_no_get = 2
    obj.non_over = 3

    print("obj.over : ", obj.over)
    print("obj.over_no_get : ", obj.over_no_get)
    print("obj.non_over : ", obj.non_over)

    print("-*" * 30)
    Managed.over = 1
    Managed.over_no_get = 2
    Managed.non_over = 3

    print("obj.over : ", obj.over)
    print("obj.over_no_get : ", obj.over_no_get)
    print("obj.non_over : ", obj.non_over)

    print("-*" * 30)

    obj2 = ManagedClass()
    print(obj2.a)
    ManagedClass.a = 30
    print(obj2.a)
    obj2.a = 20
    print(obj2.a)

    print(obj2.b)
    del obj2.b
    print(obj2.b)


