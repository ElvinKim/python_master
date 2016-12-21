flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]

for flavor in flavor_list:
    print("{} is delicious".format(flavor))

print("-*" * 30)

for index, flavor in enumerate(flavor_list):
    print(index + 1, flavor)
