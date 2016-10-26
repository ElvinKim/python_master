colors = ["black", "white"]
sizes = ["S", "M", "L"]

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

tshirts = [(color, size) for color in colors
                        for size in sizes]
print(tshirts)

