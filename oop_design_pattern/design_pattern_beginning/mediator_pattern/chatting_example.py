"""
  __  __              _   _           _
 |  \/  |            | | (_)         | |
 | \  / |   ___    __| |  _    __ _  | |_    ___    _ __
 | |\/| |  / _ \  / _` | | |  / _` | | __|  / _ \  | '__|
 | |  | | |  __/ | (_| | | | | (_| | | |_  | (_) | | |
 |_|  |_|  \___|  \__,_| |_|  \__,_|  \__|  \___/  |_|


* 언제 사용하는가?
    - 클래스의 복잡도가 증가함에 따라 중재자를 만들어서 복잡도를 줄이는 패턴

* 주요 특징은 무엇인가?
    - 객체간의 M : N 관계를 1 : 1 로 만듦
    - 중재패턴은 Colleague 클래스간의 결합도를 줄여줌
    - 중재클래스와 Colleague 클래스들은 독립적으로 변경, 재사용이 가능
    - 객체들간의 중개 역할을 하나의 객체가 하고 있기 때문에 중개 역할을 하는 객체는 규모가 커지고
      복잡도가 증가할 수 있음
"""


class ChatRoom(object):

    def __init__(self):
        self._users = dict()

    def redirect_msg(self, from_user, to_user, msg):
        if to_user == "ALL":
            for user_name in self._users.keys():
                if user_name != from_user:
                    self._users[user_name].receive_msg(from_user, msg)
        else:
            self._users[to_user].receive_msg(from_user, msg)

    def add_user(self, user):
        if user is None:
            return
        else:
            self._users[user.name] = user


class User(object):

    def __init__(self, name, chat_room):
        self._name = name
        self._chat_room = chat_room

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def send_msg(self, to_user, msg):
        self._chat_room.redirect_msg(self.name, to_user, msg)

    def receive_msg(self, from_user, msg):
        print("[FROM : {}][TO : {}] {}".format(from_user, self._name, msg))


if __name__ == "__main__":
    chat_room = ChatRoom()

    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)
    diana = User("Diana", chat_room)
    elvin = User("Elvin", chat_room)

    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(charlie)
    chat_room.add_user(diana)
    chat_room.add_user(elvin)

    alice.send_msg("Bob", "Hello Bob!")
    bob.send_msg("Alice", "Hello Alice!")
    elvin.send_msg("ALL", "Hello Everyone!")
