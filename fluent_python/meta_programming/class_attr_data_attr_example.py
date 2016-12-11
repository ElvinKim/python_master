class Class:
    data = "the class data attr"

    @property
    def prop(self):
        return "the prop value"


class Class2:
    data = 20

    def __init__(self):
        self.data = 10

    def foo(self):
        pass


if __name__ == "__main__":
    obj = Class()
    print(vars(obj))  # {}
    print(obj.__dict__)  # {}
    print(obj.data)  # the class data attr
    obj.data = "bar"
    print(vars(obj))  # {'data': 'bar'}
    print(obj.data)  # bar
    print(Class.data)  # the class data attr
    print(obj.__dict__)  # {'data': 'bar'}

    print("-*" * 30)

    obj2 = Class2()
    print(obj2.data)  # 10
    print(Class2.data)  # 20
    print(vars(obj2))  # {'data': 10}
    print(obj2.__dict__)

    print("-*" * 30)
    print(Class.prop)

    """
    obj.prop = 10  # AttributeError: can't set attribute
    """

    print(vars(obj))  # {'data': 'bar'}
    obj.__dict__['prop'] = "foo"
    print(vars(obj))  # {'data': 'bar', 'prop': 'foo'}
    print(obj.prop)  # the prop value => foo 가 나오지 않는다.
    Class.prop = "baz"  # 이제 더이상 prop가 프로퍼티(property)가 아니다
    print(obj.prop)  # foo

    print("-*" * 30)

    """
    새로운 클래스 프로퍼티는 기존 객체의 속성을 가릴 수 있다.
    """
    class Class3:

        def __init__(self):
            self.data = 10


    obj3 = Class3()
    Class3.data = 20
    print(obj3.data)  # 10
    Class3.data = property(lambda self: 20)
    print(obj3.data)  # 20

    print("-*" * 30)

    class Class4:
        data = 10

        def __init__(self):
            data = 20

    class Class5(Class4):
        pass


    obj4 = Class5()
    print(obj4.data)  # 10


