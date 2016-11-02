class Gizmo(object):
    def __init__(self):
        print('Gizmo id : %d' % id(self))


if __name__ == "__main__":
    x = Gizmo()
    #y = Gizmo() * 10


    #튜플의 상대적 불변성 테스트
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])

    print(t1 == t2)

    print(id(t1))
    t1[-1].append(50)
    print(id(t1))



