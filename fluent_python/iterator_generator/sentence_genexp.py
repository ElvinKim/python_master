import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence(object):

    def __init__(self, text):
        self._text = text

    def __repr__(self):
        return "Sentence(%s)" %reprlib.repr(self._text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self._text))


if __name__ == "__main__":
    s3 = Sentence("Hi there good!")

    for c in s3:
        print(c)
