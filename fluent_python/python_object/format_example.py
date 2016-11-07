from vector2d_v1 import Vector2d


if __name__ == "__main__":
    brl = 1/2.43
    print(brl)
    print(format(brl, '0.5f'))
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
    print("-" * 40)

    print(format(Vector2d(1, 1), 'p'))
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '.5fp'))









