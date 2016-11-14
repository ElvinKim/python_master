class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

if __name__ == "__main__":

    ad = AnswerDict(a='foo')
    print(ad['a'])  # 42
    d = {}
    d.update(ad)
    print(d['a'])  # foo
    print(d)  # {'a': 'foo'}