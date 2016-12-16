"""
1 부터 200000000 더하기

real	0m4.315s
user	0m19.942s
sys	0m0.065s
"""

import multiprocessing


RESULT_Q = multiprocessing.Queue()
LOCK = multiprocessing.Lock()


def interval_sum(start_num, last_num):
    global RESULT_Q

    total = 0

    for x in range(start_num, last_num + 1):
        total += x

    LOCK.acquire()
    RESULT_Q.put(total)
    LOCK.release()


if __name__ == "__main__":
    process_list = []
    total = 0

    for index in range(5):
        interval = int(200000000/5)
        start_num = 1+(interval*index)
        last_num = interval*(index+1)
        process_list.append(multiprocessing.Process(target=interval_sum, args=(start_num, last_num, )))

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()

    for _ in range(5):
        total += RESULT_Q.get()

    print(total)


