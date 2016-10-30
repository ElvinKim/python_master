import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        elapsed = end_time - start_time
        name = func.__name__
        arg_str = ', '.join((repr(arg) for arg in args))
        print("[%0.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result

    return clocked