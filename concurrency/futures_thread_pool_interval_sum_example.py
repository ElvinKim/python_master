"""
1 부터 200000000 더하기

real	0m20.435s
user	0m19.866s
sys	0m0.323s
"""

from concurrent import futures


def interval_sum(index):
    total = 0

    interval = int(200000000/5)
    start_num = 1+(interval*index)
    last_num = interval*(index+1)

    for x in range(start_num, last_num + 1):
        total += x
    return total


if __name__ == "__main__":
    workers_cnt = 5

    with futures.ThreadPoolExecutor(workers_cnt) as executor:
        res = executor.map(interval_sum, list(range(5)))

    print(sum(list(res)))

