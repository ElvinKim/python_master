class Foo(object):

    def __getitem__(self, index):
        return range(30)[index]


if __name__ == "__main__":
    f = Foo()

    print(f[1])  # 1
    print(f[-1])  # 29
    print("---------------------")

    for i in f:
        print(i)

    print("---------------------")
    print(20 in f)  # True
    print(40 in f)  # False
