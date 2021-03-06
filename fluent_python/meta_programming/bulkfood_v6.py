import model_v6 as model

@model.entity
class LineItem(object):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == "__main__":

    apple = LineItem("apple", 100, 10)

    print(dir(apple)[:3])
