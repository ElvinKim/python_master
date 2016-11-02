import abc

class Builder(abc.ABC):

    @abc.abstractmethod
    def make_title(self, title):
        pass

    @abc.abstractmethod
    def make_string(self, string):
        pass

    @abc.abstractmethod
    def make_items(self, items):
        pass

    @abc.abstractmethod
    def close(self):
        pass


class Director(object):

    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.make_title("Greeting")
        self._builder.make_string("아침과 낮에")
        self._builder.make_items(["좋은 아침입니다.", "안녕하세요."])
        self._builder.make_string("밤에")
        self._builder.make_items(["안녕하세요.", "안녕히 주무세요.", "안녕히 계세요."])
        self._builder.close()


class TextBuilder(Builder):

    def __init__(self):
        self._text = ""

    def make_title(self, title):
        self._text += "=" * 40 + "\n"
        self._text += "◁{}▷".format(title) + "\n"

    def make_string(self, string):
        self._text += '■{}'.format(string) + "\n"

    def make_items(self, items):
        for item in items:
            self._text += "\tº{}".format(item) + "\n"

    def close(self):
        self._text += "=" * 40 + "\n"

    def get_result(self):
        return self._text

class HTMLBuilder(Builder):

    def __init__(self):
        self._filename = ""
        self._writer = None

    def make_title(self, title):
        self._filename = title + ".html"

        self._writer = open(self._filename, 'a', encoding='utf-8')
        self._writer.write("<html>\n<head>\n<meta charset='utf-8'>\n<title>{}</title>\n</head>\n<body>\n".format(title))
        self._writer.write("<h1>{}</h1>\n".format(title))

    def make_string(self, string):
        self._writer.write("<p>{}</p>\n".format(string))


    def make_items(self, items):
        self._writer.write("<ul>\n")

        for item in items:
            self._writer.write("<li>{}</li>\n".format(item))

        self._writer.write("</ul>\n")

    def close(self):
        self._writer.write("</body></html>\n")
        self._writer.close()

    def get_result(self):
        return self._filename


if __name__ == "__main__":
    #TextBuilder
    text_builder = TextBuilder()
    director = Director(text_builder)
    director.construct()
    result = text_builder.get_result()
    print(result)

    #HTMLBuilder
    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct()
    result = html_builder.get_result()
    print(result)

"""
Builder pattern은 객체를 생성하는 면에서는 추상 팩토리 패턴과 비슷하지만 조금 다르다.

일반적으로 건물을 짓듯, 생성자에서 받아서 바인딩하는 매개변수들을 따로따로 설정하고 이를 통합하여

하나의 객체를 만들어 반환하는 패턴이다.

예를 들어 로봇을 만든다고 할 때

robot = Robot(head, body, arms, legs, wings)라고 하면 순서라도 바뀌면 정상적으로 생성이 안된다.
이때
director.set_head(head)
	.set_arms(arms)
	.set_wings(wings) # 순서가 바뀌어도 상관 없다.
	.set_legs(legs).build()

이런식으로 객체를 생성한다.
"""