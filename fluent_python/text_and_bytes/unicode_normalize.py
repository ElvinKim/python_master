from unicodedata import normalize

s1 = "café"
s2 = "cafe\u0301"

print(s1, len(s1))
print(s2, len(s2))

print(s1 == s2)

print("=" * 20)

print(normalize('NFC', s1))
print(normalize('NFC', s2))

print(normalize('NFC', s1) == normalize('NFC', s2))

