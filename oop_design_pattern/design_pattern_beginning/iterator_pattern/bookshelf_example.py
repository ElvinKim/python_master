

class Book(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class BookShelfIterator():

    def __init__(self, bookshelf):
        self._index = 0
        self._bookshelf = bookshelf

    def has_next(self):
        return self._index < self._bookshelf.get_length()

    def next(self):
        book = self._bookshelf.get_book_at(self._index)
        self._index += 1
        return book


class BookShelf(object):

    def __init__(self):
        self._books = list()
        self._last = 0

    def append_book(self, book):
        self._books.append(book)
        self._last += 1

    def get_book_at(self, index):
        return self._books[index]

    def get_length(self):
        return self._last

    def interator(self):
        return BookShelfIterator(self)


if __name__ == "__main__":
    bookshelf = BookShelf()
    bookshelf.append_book(Book("Around the World in 80 days"))
    bookshelf.append_book(Book("Bible"))
    bookshelf.append_book(Book("Cinderella"))
    bookshelf.append_book(Book("Daddy-Long-Legs"))

    it = bookshelf.interator()

    while(it.has_next()) :
        book = it.next()
        print(book.name)

