# def make_averager():
#     count = 0
#     total = 0
#
#
#     def averager(new_value):
#         count += 1
#         total += new_value
#
#         return total / count
#
#     return averager
#
#
# averager = make_averager()
# averager(10)


def make_averager():
    count = 0
    total = 0


    def averager(new_value):
        nonlocal count
        nonlocal total
        count += 1
        total += new_value

        return total / count

    return averager

averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))