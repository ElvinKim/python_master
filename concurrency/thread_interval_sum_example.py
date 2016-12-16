"""
1 부터 200000000 더하기

real	0m19.076s
user	0m18.923s
sys	0m0.320s
"""

import threading

TOTAL_VALUE = 0
MUTEX = threading.Lock()


def interval_sum(start_num, last_num):
    global TOTAL_VALUE

    total = 0

    for x in range(start_num, last_num + 1):
        total += x

    MUTEX.acquire()
    TOTAL_VALUE += total
    MUTEX.release()

if __name__ == "__main__":
    thread_list = []

    for index in range(5):
        interval = int(200000000/5)
        start_num = 1+(interval*index)
        last_num = interval*(index+1)

        thread_list.append(threading.Thread(target=interval_sum, args=(start_num, last_num, )))

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print(TOTAL_VALUE)


