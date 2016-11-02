import weakref

a_set = {0, 1}

wref = weakref.ref(a_set)
print(wref) # <weakref at 0x1006cd048; to 'set' at 0x100725ba8>
print(wref()) # {0, 1}

a_set = {2, 3, 4}
print(wref()) # None
print(wref() is None) # True

