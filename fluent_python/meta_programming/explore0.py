from collections import abc


class FrozenJSON:

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


from osconfeed import load

raw_feed = load()
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.speakers))
print(sorted(feed.Schedule.keys()))

for key, value in sorted(feed.Schedule.items()):
    print("{:3} {}".format(len(value), key))

print(feed.Schedule.speakers[-1].name)

talk = feed.Schedule.events[40]
print(type(talk))
print(talk.flavor)



