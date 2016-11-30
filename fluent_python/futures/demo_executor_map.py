from time import sleep
from time import strftime

from concurrent import futures


def display(*args):
    print(strftime("[%H:%M:%S]"), end=" ")
    print(*args)


def loiter(n):
    msg = "{}loiter({}) : doing nothing for {}s..."
    display(msg.format('\t' * n, n, n))
    sleep(4-n)
    msg = '{}liter({}) : done.'
    display(msg.format("\t" * n, n))
    return n * 10


def main():
    display("Script starting.")
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display("results:", results)
    display("Waiting for individual results:")
    for i, result in enumerate(results):
        display('results {} : {}'.format(i, result))

if __name__ == "__main__":
    main()




