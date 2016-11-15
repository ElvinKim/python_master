import decimal

if __name__ == "__main__":

    ctx = decimal.getcontext()
    ctx.prec = 40

    one_third = decimal.Decimal('1') / decimal.Decimal('3')
    print(one_third)  # 0.3333333333333333333333333333333333333333
    print(one_third == +one_third)  # True
    ctx.prec = 28

    print(one_third)  # 0.3333333333333333333333333333333333333333
    print(one_third == +one_third)  # False
