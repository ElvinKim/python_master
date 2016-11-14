class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == "__main__":
    dd = DoppelDict(one=1)
    print(dd)  # {'one': 1}
    dd['two'] = 2
    print(dd)  # {'two': [2, 2], 'one': 1}
    dd.update(three=3)
    print(dd)  # {'three': 3, 'two': [2, 2], 'one': 1}