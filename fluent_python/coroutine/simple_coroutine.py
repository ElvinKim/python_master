from inspect import getgeneratorstate


def simple_coroutine():
    print("-> coroutine started")
    x = yield

    print("-> coroutine received : ", x)


def simple_coroutine2(a):
    print("-> Started : a = ", a)
    b = yield a
    print("-> Received : b = ", b)
    c = yield a + b
    print("-> Received : c = ", c)


if __name__ == "__main__":
    my_coro = simple_coroutine()
    print(my_coro)

    next(my_coro)
    #my_coro.send(42)
    print("=" * 30)

    my_coro2 = simple_coroutine2(14)
    print(getgeneratorstate(my_coro2))  # GEN_CREATED
    print(next(my_coro2))
    print(getgeneratorstate(my_coro2))  # GEN_SUSPENDED
    print(my_coro2.send(28))

    try:
        print(my_coro2.send(99))
    except:
        pass

    print(getgeneratorstate(my_coro2))  # GEN_CLOSED

