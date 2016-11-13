class A:

    def ping(self):
        print('A - ping : ', self)

    def pang(self):
        print('A - pang', self)

class B(A):

    def pong(self):
        print("B - pong", self)


class C(A):

    def pong(self):
        print("C - pong", self)

    def pang(self):
        print("C - pang", self)

class D(B, C):

    def ping(self):
        super().ping()
        print("post-ping", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


class E(C, B):

    def ping(self):
        super().ping()
        print("post-ping", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == "__main__":

    d = D()
    d.pong()
    C.pong(d)

    print(D.__mro__)

    d.ping()
    d.pang()
    print("=" * 20)
    d.pingpong()
    """
    B - pong <__main__.D object at 0x100750588>
    C - pong <__main__.D object at 0x100750588>
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    A - ping :  <__main__.D object at 0x100750588>
    post-ping <__main__.D object at 0x100750588>
    C - pang <__main__.D object at 0x100750588>
    ====================
    A - ping :  <__main__.D object at 0x100750588>
    post-ping <__main__.D object at 0x100750588>
    A - ping :  <__main__.D object at 0x100750588>
    B - pong <__main__.D object at 0x100750588>
    B - pong <__main__.D object at 0x100750588>
    C - pong <__main__.D object at 0x100750588>
    """

    print(E.__mro__)