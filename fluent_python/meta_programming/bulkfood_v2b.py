class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 여기서 이미 setter함수 호출
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("value must be > 0")

    weight = property(get_weight, set_weight)

if __name__ == "__main__" :
    raisins = LineItem("Golden raisns", 10, 6.95)
    print(raisins.subtotal())
    raisins.weight = -20
    print(raisins.subtotal())

