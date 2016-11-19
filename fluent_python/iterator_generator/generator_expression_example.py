if __name__ == "__main__":

    res1 = (x for x in range(10))
    res2 = [x for x in range(10)]

    print(res1)  # <generator object <genexpr> at 0x100626938>
    print(res2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(next(res1))  # 0
    #print(next(res2))  # TypeError: 'list' object is not an iterator
