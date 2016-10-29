def f1(a):
    print(a)
    print(b)

b = 6

def f2(a):
    '''
    파이썬이 함수 본체를 컴파일할 때 b가 함수 안에 할당되어 있으므로 변수 b를
    지역 변수로 판단한다
    '''
    print(a)
    print(b) # 6이 출력될 거라고 생각할 수 있지만 Error가 발생

    b = 9

def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f1(3)
#f2(3)
f3(3)
f3(3)
