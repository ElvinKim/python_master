
def doc_test(param):
    'doc string test'
    print(param)

def doc_test2(param, param2):
    '''
    doc string test 2

    :param param:
    :param param2:
    :return:
    '''
    print(param)

print("*" * 20)
print(">>help(doc_test)")
help(doc_test)

print("*" * 20)
print(">>help(doc_test2)")
help(doc_test2)

print("*" * 20)
print(">>print(doc_test.__doc__)")
print(doc_test.__doc__)

print("*" * 20)
print(">>print(doc_test.__doc__)")
print(doc_test2.__doc__)


"""
함수 몸체 시작 부분에 문자열을 포함시켜 함수 정의에 문서(documentation)을
붙일 수 있는데 이것이 docstring이다
"""
