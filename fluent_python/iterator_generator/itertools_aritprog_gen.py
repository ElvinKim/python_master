import itertools
from decimal import Decimal


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)

    print("--->", ap_gen)

    if end is not None:
        ap_gen = itertools.takewhile(lambda n : n < end, ap_gen)

    return ap_gen


if __name__ == "__main__":
    ap = aritprog_gen(0, 1, 3)
    print(ap)  # <itertools.takewhile object at 0x101d6e8c8>
    print(list(ap))

    ap = aritprog_gen(1, .5, 3)
    print(ap)  # <itertools.takewhile object at 0x101d6e988>
    print(list(ap))

    ap = aritprog_gen(0, Decimal('.1'), .3)
    print(ap)  # <itertools.takewhile object at 0x101d6ea48>
    print(list(ap))
