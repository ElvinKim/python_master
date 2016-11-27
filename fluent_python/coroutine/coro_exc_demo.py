from inspect import getgeneratorstate


class DemoException(Exception):
    """ 설명에 사용할 예외 유형 """


def demo_exc_handling():
    print("-> corotine started")

    while True:

        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. Continuing...")
        else:
            print("-> coroutine received : {!r}".format(x))
    raise RuntimeError("This line should never run.")


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    exc_coro.close()  # GEN_CLOSED

    print(getgeneratorstate(exc_coro))

    print("-*" * 30)

    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)

    print(getgeneratorstate(exc_coro))  # GEN_SUSPENDED

    print("-*" * 30)

    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(ZeroDivisionError)

    print(getgeneratorstate(exc_coro))  # GEN_CLOSED
