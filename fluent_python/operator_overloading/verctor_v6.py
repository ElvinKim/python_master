from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector(object):
    typecode = 'd'
    shorcut_names = "xyzt"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("["):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else :
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

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
        print("hash call")
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{cls.__name__} indices must be intergers"
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shorcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]

        msg = "{._name__!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shorcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_anme=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self):
        return math.atan2(self.y, self.x)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == "__main__":
    v1 = Vector([3, 4, 5])
    v2 = Vector([6, 7, 8])
    v3 = Vector([1, 2])

    print(v1 + v2)
    print(v1 + v3)
    #print(v1 + 2)  # TypeError: zip_longest argument #2 must support iteration
    #print(2 + v1)  # TypeError: unsupported operand type(s) for +: 'int' and 'Vector'

    print("-*" * 15)
    print(v1 * 2)
    print(3 * v1)
    v4 = Vector([3, 4, 5])
    print("-*" * 15)
    print(v1 == v4)
    print(v1 == v3)

    print("-" * 20)

    va = Vector([1.0, 2.0, 3.0])
    vb = Vector(range(1, 4))
    print(va == vb)
    vc = Vector([1, 2])
    from vector2d_v3 import Vector2d
    v2d = Vector2d(1, 2)
    print(vc == v2d)
    t3 = (1, 2, 3)
    print(va == t3)

    print("-*" * 15)

    v1_alias = v1
    print(id(v1))

    v1 += Vector([4, 5, 6])
    print(v1)
    print(id(v1))
    print(v1_alias)
    v1 *= 11
    print(v1)
    print(id(v1))






