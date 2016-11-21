def gen_123():
    yield 1
    yield 2
    yield 3

def gen_AB():
    print('start')
    yield "A"
    print('continue')
    yield "B"
    print('end.')


if __name__ == "__main__":
    print(gen_123)  # <function gen_123 at 0x10061f598>
    print(gen_123())  # <generator object gen_123 at 0x100626938>

    for i in gen_123():
        print(i)

    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    #print(next(g))  # ERROR !! StopIteration

    print("-=" * 20)

    for c in gen_AB():
        print("--->", c)
    """
    start
    ---> A
    continue
    ---> B
    end.
    """


