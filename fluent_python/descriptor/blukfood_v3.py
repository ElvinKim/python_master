class Quantity(object):

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        """
        self는 디스크립터 객체
        instance는 관리 대상 객체
        """
        if value > 0:
            instance.__dict__[self.storage_name] = value

        else :
            raise ValueError("value must be > 0")


class LineItem(object):

    weight = Quantity("weight")
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight #이때 Quantity 의 __set__ 함수가 호출 된다
        self.price = price #이때 Quantity 의 __set__ 함수가 호출 된다

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":

    apple = LineItem("apple", 100, 10)
    orange = LineItem("orange", 100, 0)

    """
    이 예제의 아쉬운 점은 Quantity객체에 속석명을 명시적으로 지정해야 한다는 점이다
    """
