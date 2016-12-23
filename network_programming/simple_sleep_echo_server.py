"""
Client가 숫자를 보내면 그 숫자만큼 sleep하고

그 숫자를 다시 보내주는 서버
"""
import socket
import time


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 9999))
    server_socket.listen(5)

    while True:
        connection, client_address = server_socket.accept()
        print("Client[{}] connect...".format(client_address))
        try:
            data = connection.recv(100)
            sleep_time = int(data)

            for x in range(1, sleep_time + 1):
                print(x)
                time.sleep(1)

            connection.send(data)
        except:
            connection.close()

        print("Client[{}] close".format(client_address))
        connection.close()


