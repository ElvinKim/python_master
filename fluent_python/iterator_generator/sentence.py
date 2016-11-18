import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


class Sentence(object):

    def __init__(self, text):
        self._text = text
        self._words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self._words[index]

    def __len__(self):
        return len(self._words)

    def __repr__(self):
        return "Sentence(%s)" %reprlib.repr(self._text)


if __name__ == "__main__":
    s = Sentence('"The Time has come," The Walrus said')
    print(s)

    for word in s:
        print(word)

    print(list(s))  # ['The', 'Time', 'has', 'come', 'The', 'Walrus', 'said']
    print(isinstance(s, abc.Iterable))  # False
    print(issubclass(Sentence, abc.Iterable))  # False
    print("-*" * 20)

    s3 = Sentence("Pig and Pepper")
    it = iter(s3)
    print(it)
    print(next(it))
    print(next(it))
    print(next(it))
    print(list(it))


