"""
  _____
 |  __ \
 | |__) |  _ __    ___   __  __  _   _
 |  ___/  | '__|  / _ \  \ \/ / | | | |
 | |      | |    | (_) |  >  <  | |_| |
 |_|      |_|     \___/  /_/\_\  \__, |
                                  __/ |
                                 |___/


* 언제 사용하는가?
    - Proxy는 대리인이란 의미. 대리인에게 본인이 아니더라도 가능한 일을 맡기고 대리인이 일을 처리하게 하는 패턴
    - 만약 대리인의 능력 밖의 일은 본인에게 물을어 오게 함

* 주요 특징은 무엇인가?
    - 만약 팩스, 프린터, 스캐너, 복사기를 관리하는 프로그램이 있다고 해보자
      만약 4가지를 초기하는데 각각 5초가 걸린다고 하자
      만약 Proxy패턴을 사용하지 않으면 나는 스캐너만 쓰려고 했어도 20초 초기 설정 시간을 기다려야함
    - Proxy에서 처리할 수 없는 것은 RealSubject에게 위임함. 실세계의 위임과는 관계가 반대임
    - Proxy는 투과적인 성질을 가지고 있음. RealSubject를 호출하던 Proxy를 호출하던 결과는 같음
    - HTTP Proxy도 이 Proxy 패턴을 가지고 있음.
      브라우저 : Client, HTTP Proxy : Proxy, 웹서버 : RealSubject

* 구성요소
    - Subject : Proxy 역할과 RealSubject 역할을 동일시 하기 위한  인터페이스
                Subject가 있기 때문에 Client는 Proxy역할과 RealSubject 역할의 차이를 의식할 필요가 없음
    - Proxy : Client 역할의 요구를 할 수 있는 만큼 처리함
              처리할 수 없으면 RealSubject 역할에게 처리를 맡김
    - RealSubject : 대리인인 Proxy 역할에서 감당할 수 없는 일이 발생했을 때 등장하는 것이 본인인 RealSubject임
    - Client : Proxy 패턴을 이용하는 역할
"""

import abc
import time


class Printable(abc.ABC):

    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def print(self, string):
        pass


class Printer(Printable):

    def __init__(self, name):
        self._name = name
        self._heavy_job("Printer의 인스턴스({})을 생성중".format(self._name))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def print(self, string):
        print("=== {} ===".format(self._name))
        print(string)

    def _heavy_job(self, msg):
        print(msg, flush=True, end="")
        for _ in range(5):
            time.sleep(1)
            print(".", flush=True, end="")
        print("완료")


class PrinterProxy(Printable):

    def __init__(self, name):
        self._name = name
        self._real = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._real is not None:
            self._real.name = name
        self._name = name

    def print(self, string):
        self._realize()
        self._real.print(string)

    def _realize(self):
        if self._real is None:
            self._real = Printer(self._name)


if __name__ == "__main__":
    p = PrinterProxy("Alice")
    print("이름은 현재 {} 입니다.".format(p.name))
    p.name = "Bob"
    print("이름은 현재 {} 입니다.".format(p.name))
    p.print("Hello. World!")
    p.print("Hello. World!")
