from concurrent import futures
import os
from flags import save_flag, get_flag, show, main


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    with futures.ProcessPoolExecutor() as excutor:
        res = excutor.map(download_one, sorted(cc_list))

    print(res)  # <itertools.chain object at 0x104bf3978>

    for x in res:
        print(x)

    return len(list(res))

if __name__ == "__main__":
    print("CPU count : ", os.cpu_count())
    main(download_many)
    """
    20 flags downloaded in 0.60s
    """

