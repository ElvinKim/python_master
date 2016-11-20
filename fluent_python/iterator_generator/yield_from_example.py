def chain_v1(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain_v2(*iterables):
    for i in iterables:
        yield from i


if __name__ == "__main__":
    s = 'ABC'
    t = tuple(range(1, 10))
    print(list(chain_v1(s, t)))
    print(list(chain_v2(s, t)))

