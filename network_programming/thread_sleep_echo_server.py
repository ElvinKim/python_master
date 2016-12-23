"""
Client가 숫자를 보내면 그 숫자만큼 sleep하고

그 숫자를 다시 보내주는 서버
"""
import socket
import threading
import time


def count_num():
    connection, client_address = server_socket.accept()
    print("Client[{}] connect...".format(client_address))
    data = connection.recv(100)
    sleep_time = int(data)

    if sleep_time == 0:
        connection.send("done")
    else:
        for x in range(1, sleep_time + 1):
            print(x)
            time.sleep(1)

        connection.send(data)

    print("Client[{}] close".format(client_address))
    connection.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 9999))
    server_socket.listen(5)

    while True:
        try:
            threading.Thread(target=count_num).start()
        except:
            pass

