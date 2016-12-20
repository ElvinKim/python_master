import select
import socket


class EventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented("must implement")

    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'Return True if sending is requested'
        return False

    def handle_send(self):
        "Send outgoing data"
        pass


class EchoServer(EventHandler):
    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        #  이벤트 루프 핸들러 리스트에 클라이언트 추가
        self.handler_list.append(self.client_handler(client, self.handler_list))


class TCPClient(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        #자기 자신을 이벤트 루프 핸들러 리스트에서 제거
        self.handler_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        print("self.outgoing : ", self.outgoing)
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoClient(TCPClient):
    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]

        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

        print("can_recv : ", can_recv)
        print("can_send : ", can_send)

        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


if __name__ == "__main__":
    handlers = list()
    handlers.append(EchoServer(("", 16000), TCPEchoClient, handlers))
    event_loop(handlers)
