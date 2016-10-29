import functools

def add(a, b):
    return a + b


def add2(a, *args, b=10):
    return a + b

five_add_number = functools.partial(add, 5)
ten_add_number = functools.partial(add2, b=10)

print(five_add_number(10))
print(ten_add_number(10))
