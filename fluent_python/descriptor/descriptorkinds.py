def cls_name(obj_or_cls):
    cls = type(obj_or_cls)

    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)

    if cls is type:
        return "<class {}>".format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return "<obj {}>".format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print("-> {}.__{}__({})".format(cls_name(args[0]), name, pseudo_args))


class Overriding(object):
    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)

    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class OverridingNoGet(object):

    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class NoneOverriding(object):
    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)


class Managed(object):
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NoneOverriding()

    def spam(self):
        print("-> Managed.spam({})".format(display(self)))


if __name__ == "__main__":

    obj = Managed()
    print(obj.over)

    print(obj.over_no_get) # __get__ 함수가 없으므로 객체 자체를 리턴한다.
    #결과 : <__main__.OverridingNoGet object at 0x101055160>

    obj.over_no_get = 10
    #결과 " -> OverridingNoGet.__set__(<obj OverridingNoGet>, <obj Managed>, 10)
    print(obj.over_no_get)
    obj.__dict__['over_no_get'] = 10
    print(vars(obj))
    print(obj.over_no_get) #속성이 생겼으므로 디스크립터는 가려진다.
