
class Dog(object):
    __mood = "bad"

    def __init__(self):
        self.__mood = "good"


if __name__ == "__main__":
    print(Dog.__dict__)  # {'__doc__': None, '_Dog__mood': 'bad', '...

    dog = Dog()
    print(dog._Dog__mood)  # good
    dog._Dog__mood = "happy"
    print(dog._Dog__mood)  # happy