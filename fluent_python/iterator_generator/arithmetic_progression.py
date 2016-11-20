from decimal import Decimal


class ArithmeticProgression(object):

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0

        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0

    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == "__main__":
    ap = ArithmeticProgression(0, 1, 3)
    print(ap)  # <__main__.ArithmeticProgression object at 0x1018500f0>
    print(list(ap))

    ap = ArithmeticProgression(1, .5, 3)
    print(ap)  # <__main__.ArithmeticProgression object at 0x101850128>
    print(list(ap))

    ap = ArithmeticProgression(0, Decimal('.1'), .3)
    print(ap)  # <__main__.ArithmeticProgression object at 0x101850198>
    print(list(ap))

    print("-=" * 30)

    ap = aritprog_gen(0, 1, 3)
    print(ap)  # <generator object aritprog_gen at 0x101846e08>
    print(list(ap))

    ap = aritprog_gen(1, .5, 3)
    print(ap)  # <generator object aritprog_gen at 0x101846d58>
    print(list(ap))

    ap = aritprog_gen(0, Decimal('.1'), .3)
    print(ap)  # <generator object aritprog_gen at 0x101846e08>
    print(list(ap))

