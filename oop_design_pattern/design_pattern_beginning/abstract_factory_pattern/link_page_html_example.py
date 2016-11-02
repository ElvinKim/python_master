import abc

class Item(abc.ABC):

    def __init__(self, caption):
        self._caption = caption

    @abc.abstractmethod
    def make_html(self):
        pass


class Link(Item):

    def __init__(self, caption, url):
        super().__init__(caption)
        self._url = url


class ListLink(Link):

    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return "<li><a href=\"{url}\">{caption}</a></li>\n".format(url=self._url, caption=self._caption)


class TableLink(Link):

    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return "<td><a href=\"{url}\">{caption}</a></td>\n".format(url=self._url, caption=self._caption)


class Tray(Item):

    def __init__(self, caption):
        super().__init__(caption)
        self._tray = []

    def add(self, item):
        self._tray.append(item)


class ListTray(Tray):

    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        result_html = """<li>{}<ul>\n""".format(self._caption)

        for item in self._tray:
            result_html += item.make_html()

        result_html += "</ul>\n</li>\n"

        return result_html


class TableTray(Tray):

    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        result_html = "<td><table width=\"100%\" border=\"1\"><tr>" \
                      "<td bgcolor=\"#cccccc\" align=\"center\" colspan=\"{size}\"><b>{caption}</b>" \
                      "</td></tr><tr>\n".format(size=len(self._tray), caption=self._caption)

        for item in self._tray:
            result_html += item.make_html()

        result_html += "</tr></table></td>"

        return result_html


class Page(abc.ABC):

    def __init__(self, title, author):
        self._content = []
        self._title = title
        self._author = author

    def add(self, item):
        self._content.append(item)

    def output(self):
        filename = self._title + ".html"
        writer = open(filename, 'a', encoding='utf-8')
        writer.write(self.make_html())
        writer.close()
        print(filename + " 을 작성하였습니다.")

    @abc.abstractmethod
    def make_html(self):
        pass


class ListPage(Page):

    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        result_html = "<html><head><title>{title}</title></head>\n<body><h1>{title}</h1><ul>".format(title=self._title)

        for item in self._content:
            result_html += item.make_html()

        result_html += "</ul><hr><address>{author}</address></body></html>".format(author=self._author)

        return result_html


class TablePage(Page):

    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        result_html = "<html><head><title>{title}</title></head>\n<body><h1>{title}</h1><ul>".format(title=self._title)
        result_html += "<table width=\"80%\" border=\"3\"> \n"

        for item in self._content:
            result_html += "<tr>{}</tr>".format(item.make_html())

        result_html += "</table><hr><address>{author}</address></body></html>".format(author=self._author)

        return result_html


class Factory(abc.ABC):

    @classmethod
    def get_factory(cls, classname):
        try:
            factory = eval("{}()".format(classname))
        except:
            raise TypeError("There is no '{}".format(classname))

        return factory

    @abc.abstractmethod
    def create_link(self, caption, url):
        pass

    @abc.abstractmethod
    def create_tray(self, caption):
        pass

    @abc.abstractmethod
    def create_page(self, title, author):
        pass


class ListFactory(Factory):

    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, author):
        return ListPage(title, author)


class TableFactory(Factory):

    def create_link(self, caption, url):
        return TableLink(caption, url)

    def create_tray(self, caption):
        return TableTray(caption)

    def create_page(self, title, author):
        return TablePage(title, author)


if __name__ == "__main__":
    #factory = Factory.get_factory("ListFactory")
    factory = Factory.get_factory("TableFactory")

    joins = factory.create_link("중앙일보", "http://www.joins.com")
    chosun = factory.create_link("조선일보", "http://www.chosun.com")
    
    us_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.com")
    kr_yahoo = factory.create_link("Yahoo! Korea", "http://www.yahoo.co.kr")
    
    excite = factory.create_link("Excite", "http://www.excite.com")
    google = factory.create_link("Google", "http://www.google.com")

    tray_news = factory.create_tray("News")
    tray_news.add(joins)
    tray_news.add(chosun)
    
    tray_yahoo = factory.create_tray("Yahoo!")
    tray_yahoo.add(us_yahoo)
    tray_yahoo.add(kr_yahoo)
    
    tray_search = factory.create_tray("Search")
    tray_search.add(tray_yahoo)
    tray_search.add(excite)
    tray_search.add(google)
    
    #page = factory.create_page("LinkPage", "Page")
    page = factory.create_page("TablePage", "Page")
    page.add(tray_news)
    page.add(tray_search)
    page.output()