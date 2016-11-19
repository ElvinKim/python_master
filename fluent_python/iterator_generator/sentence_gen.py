import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence(object):

    def __init__(self, text):
        self._text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" %reprlib.repr(self._text)

    def __iter__(self):
        for word in self._words:
            yield word
        return


if __name__ == "__main__":
    s3 = Sentence("Hi there good!")
