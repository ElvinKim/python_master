import sys
import socket
import select


RECV_BUFFER = 4096


def chat_client():

    host = "localhost"
    port = 9090

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(2)

    try:
        client_socket.connect((host, port))
    except:
        sys.exit()

    print("Connected to remote host. You can start sending messages")
    sys.stdout.write("[Me]")
    sys.stdout.flush()

    while True:
        socket_list = [sys.stdin, client_socket]

        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [])

        for sock in ready_to_read:
            if sock == client_socket:
                data = sock.recv(RECV_BUFFER)
                msg = data.decode("utf-8")
                sys.stdout.write(msg)
                sys.stdout.write('[Me]')
                sys.stdout.flush()
            else:
                msg = sys.stdin.readline()
                sys.stdout.write(msg)
                client_socket.send(msg.encode("utf-8"))
                sys.stdout.write("[Me]")
                sys.stdout.flush()


if __name__ == "__main__":
    sys.exit(chat_client())




