from coroaverager1 import averager
from inspect import getgeneratorstate


if __name__ == "__main__":
    coro_avg = averager()
    print(coro_avg.send(40))

    try:
        print(coro_avg.send("Spam"))
    except:
        pass

    print(getgeneratorstate(coro_avg))  # GEN_CLOSED

