
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))

print(averager.__code__)
print(averager.__code__.co_varnames) #('new_value', 'total')
print(averager.__code__.co_freevars) #('series',)

print("="*60)

print(averager.__closure__)
print(averager.__closure__[0]) #<cell at 0x10070dbb8: list object at 0x10074ed88>
print(averager.__closure__[0].cell_contents) #[10, 20, 30]


