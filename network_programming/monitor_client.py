import socket
import time
import threading

n = 0


def monitor():
    global n

    while True:
        time.sleep(1)
        print(n, "reqs/sec")
        n = 0


if __name__ == "__main__":
    threading.Thread(target=monitor).start()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 7777))

    while True:
        client_socket.send(b"1")
        client_socket.recv(100)
        n += 1


