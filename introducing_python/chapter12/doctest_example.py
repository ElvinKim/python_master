import doctest
from string import capwords


def just_do_it(text):
    """
    :param text:
    :return:

    doctext
    >>> just_do_it('duck')
    'Duck'
    >>> just_do_it('a veritable flock of ducks')
    'A Veritable Flock Of Ducks'
    >>> just_do_it('dog')
    'Dog'
    """

    return capwords(text)


if __name__ == "_main__":
    doctest.testmod()



