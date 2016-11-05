class Demo(object):

    @classmethod
    def class_method(*args):
        return args

    @staticmethod
    def static_method(*args):
        return args

print(Demo.class_method())  # (<class '__main__.Demo'>,)
print(Demo.class_method('Test'))  # (<class '__main__.Demo'>, 'Test')

print(Demo.static_method())  # ()
print(Demo.static_method('Test'))  # ('Test',)
