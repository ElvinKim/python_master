"""
  ______                              _
 |  ____|                            | |
 | |__      __ _    ___    __ _    __| |   ___
 |  __|    / _` |  / __|  / _` |  / _` |  / _ \
 | |      | (_| | | (__  | (_| | | (_| | |  __/
 |_|       \__,_|  \___|  \__,_|  \__,_|  \___|


* 언제 사용하는가?
    - 커다란 프로그램을 사용해서 처리를 실행할 때 이 처리를 수행하는 창구를 만들면 좋은데 이것이 Facade 패턴


* 주요 특징은 무엇인가?
    - 복잡하게 얽혀 있는 것을 정리해서 높은 레벨의 인터페이스를 제공
    - 시스템의 외부에 대해서는 단순한 인터페이스를 보여주고 내부에서는 각 클래스의 역할이나 의존관계를 생각하여 구현
"""


class Property(object):

    def __init__(self):
        self._prop_dict = dict()

    def load(self, filename):
        with open(filename, encoding="utf-8") as f:
            for line in f.readlines():
                if "=" not in line:
                    raise ValueError("Wrong format!")

                key, value = line.split("=")
                key = key.strip()
                value = value.strip()

                self._prop_dict[key] = value

        return self._prop_dict

    def get_property(self, key):
        return self._prop_dict[key]


class Database(object):

    @classmethod
    def get_properties(cls, dbname):
        filename = dbname + ".txt"
        prop = Property()
        prop.load(filename)
        return prop


class HtmlWriter(object):

    def __init__(self, writer):
        self._writer = writer

    def title(self, title):
        self._writer.write("<html>")
        self._writer.write("<head>")
        self._writer.write("<title>{}title>".format(title))
        self._writer.write("</head>")
        self._writer.write("<body>\n")
        self._writer.write("<h1>{}</h1>\n".format(title))

    def paragraph(self, msg):
        self._writer.write("<p>{}</p>\n".format(msg))

    def link(self, href, caption):
        self._writer.write("<a href=\"{}\"/>{}</a>".format(href, caption))

    def mailto(self, mailaddr, username):
        self.link("mailto:" + mailaddr, username)

    def close(self):
        self._writer.write("</body>")
        self._writer.write("</html>\n")
        self._writer.close()


class PageMaker(object):

    @classmethod
    def make_welcome_page(cls, mailaddr, filename):
        mailprop = Database.get_properties("maildata")
        username = mailprop.get_property(mailaddr)
        writer = HtmlWriter(open(filename, "a", encoding="utf-8"))
        writer.title("Welcome to {}'s  page!!".format(username))
        writer.paragraph("{}의 페이지에 오신 걸 환영합니다.".format(username))
        writer.paragraph("메일을 기다리고 있습니다.")
        writer.mailto(mailaddr, username)
        writer.close()
        print("{} is created for {}({})".format(filename, mailaddr, username))


if __name__ == "__main__":
    PageMaker.make_welcome_page("youngjin@youngjin.com", "welcome.html")