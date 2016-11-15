from array import array
import math


class Vector2d(object):
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=""):
        if format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_format = '<{}, {}>'
        else:
            coords = self
            outer_format = '({}, {})'

        components = (format(c, format_spec) for c in coords)
        return outer_format.format(*components)


    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


    def angle(self):
        return math.atan2(self.y, self.x)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == "__main__":
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    v3 = Vector2d(4, 3)

    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(v1)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1))
    print(bool(Vector2d(0,0)))
    print(hash(Vector2d(3, 4)))
    print("*" * 20, " hash ", "*" * 20)
    print(hash(v1))
    print(hash(v2))
    print(hash(v3))

