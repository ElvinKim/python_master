import functools


def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Do something!
        """
        func(*args, **kwargs)

    return wrapper


@deco
def func():
    print("func()")


@deco
def func2(num1):
    print("func2(num1")


if __name__ == "__main__":
    print(func.__name__)
    print(func2.__name__)
