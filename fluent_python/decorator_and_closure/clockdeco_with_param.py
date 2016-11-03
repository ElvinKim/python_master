import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args})->{result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()

            elapsed = end_time - start_time
            name = func.__name__
            arg_str = ', '.join((repr(arg) for arg in args))
            print(fmt.format(**locals()))
            return result

        return clocked
    return decorate


if __name__ == "__main__":

    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    @clock('{name} : {elapsed}s')
    def snooze2(seconds):
        time.sleep(seconds)


    def snooze3(seconds):
        time.sleep(seconds)

    snooze3 = clock('{name} : {elapsed}s')(snooze3)

    for i in range(3):
        snooze(.123)

    print("*" * 40)

    for i in range(3):
        snooze2(.123)

    print("*" * 40)

    for i in range(3):
        snooze3(.123)


