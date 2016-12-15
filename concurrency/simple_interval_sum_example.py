"""
1 부터 200000000 더하기

real	0m16.303s
user	0m16.271s
sys	0m0.019s
"""

TOTAL_VALUE = 0


def interval_sum(start_num, last_num):
    global TOTAL_VALUE

    total = 0

    for x in range(start_num, last_num + 1):
        total += x

    TOTAL_VALUE += total


if __name__ == "__main__":
    interval_sum(1, 200000000)

    print(TOTAL_VALUE)


