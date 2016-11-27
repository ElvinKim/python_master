class DemoException(Exception):
    """ 설명에 사용할 예외 유형 """


def demo_exc_handling():
    print("-> corotine started")

    try:
        while True:

            try:
                x = yield
            except DemoException:
                print("*** DemoException handled. Continuing...")
            else:
                print("-> coroutine received : {!r}".format(x))

    finally:
        print("-> coroutine ending")

