import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    write = sys.stdout.write
    flush = sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        status = char + " " + msg
        write(status)
        flush()
        write('\x08' * len(status))

        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    write(" " * len(status) + "\x08" * len(status))


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42


@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('thinking!'))
    print("spinner object : ", spinner)  # spinner object :  <Task pending coro=<spin()...
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    print(loop)  # <_UnixSelectorEventLoop running=False closed=False debug=False>
    print(supervisor())  # <generator object supervisor at 0x105211258>

    result = loop.run_until_complete(supervisor())
    loop.close()
    print("Answer : ", result)  # Answer :  42


if __name__ == "__main__":
    main()

