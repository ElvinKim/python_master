from clockdeco import clock
import functools

@functools.lru_cache()
@clock
def finobacci(n):
    if n < 2:
        return n
    return finobacci(n-2) + finobacci(n-1)


if __name__ == "__main__":
    print(finobacci(30))