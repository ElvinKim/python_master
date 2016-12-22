def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("{} : {}".format(message, values_str))


log("My numbers are", 1, 2)
log("Hi there!")

print("-*" * 30)

favorites= [1, 3, 5]
log("Favorite numbers", favorites)
log("Favorite numbers", *favorites)
