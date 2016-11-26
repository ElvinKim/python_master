from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func()
        next(gen)
        return gen
    return primer

