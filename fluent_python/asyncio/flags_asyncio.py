import asyncio
import aiohttp

from flags import BASE_URL, save_flag, show, main


@asyncio.coroutine
def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    print("resp : ", resp)
    image = yield from resp.read()
    print("image : ", image)
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    [print("download_one(cc) : ", gen) for gen in to_do]
    wait_coro = asyncio.wait(to_do)
    print("wait_coro : ", wait_coro)  # wait_coro :  <generator object wait at 0x10583d8e0>
    res, _ = loop.run_until_complete(wait_coro)
    print("res : ", res)

    print("before loop close")
    loop.close()

    return len(res)


if __name__ == "__main__":
    main(download_many)
