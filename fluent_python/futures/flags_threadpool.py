from concurrent import futures

from flags import save_flag, get_flag, show, main


MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as excutor:
        res = excutor.map(download_one, sorted(cc_list))

    print(res)  # <generator object Executor.map.<locals>.result_iterator at 0x1027b7200>

    for x in res:
        print(x)

    return len(list(res))

if __name__ == "__main__":
    main(download_many)
    """
    20 flags downloaded in 0.60s
    """
