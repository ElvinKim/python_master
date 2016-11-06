class MySeq(object):
    def __getitem__(self, index):
        return index


if __name__ == "__main__":
    s = MySeq()

    print(s[1])  # 1
    print(s[1:4])  # slice(1, 4, None)
    print(s[1:4:2])  # slice(1, 4, 2)
    print(s[1:4:2, 9])  # (slice(1, 4, 2), 9)
    print(s[1:4:2, 7:9])  # (slice(1, 4, 2), slice(7, 9, None))

    print(slice)  # <class 'slice'>
    print(dir(slice))
    """
    [..., 'indices', 'start', 'step', 'stop']
    """
    print(slice(None, 10, 2).indices(5))  # (0, 5, 2)
    print(slice(-3, None, None).indices(5))  # (2, 5, 1)
