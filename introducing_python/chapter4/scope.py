animal1 = "dog"
animal2 = "dog"
animal3 = "dog"

def print_animal():
    animal1 = "duck"
    print(animal1) #duck

def print_animal2():
    global animal2
    animal2 = "pig"
    print(animal2) #pig

def print_animal3():
    animal3 = "elephant"
    print(animal3) #elephant


if __name__ == "__main__":
    animal3 = "cow"

    print_animal()
    print(animal1) #dog

    print_animal2()
    print(animal2) #pig

    print_animal3()
    print(animal3) #cow
