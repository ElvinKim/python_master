import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


class Sentence(object):

    def __init__(self, text):
        self._text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" %reprlib.repr(self._text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == "__main__":
    s3 = Sentence("Hi there good!")
    it = iter(s3)
    print(it)

    print(next(it))
    print(next(it))
    print(next(it))
    print(isinstance(s3, abc.Iterable))  # True
    print(issubclass(Sentence, abc.Iterable))  # True




