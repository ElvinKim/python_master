import sys
import socket
import select


HOST = ""
PORT = 9090

SOCKET_LIST = []
RECV_BUFFER = 4096


def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)

    print("Chat server started on port ", str(PORT))

    while True:
        ready_to_read, write_to_ready, in_error = select.select(SOCKET_LIST, [], [], 0)

        for sock in ready_to_read:
            if sock == server_socket:
                # a enw connection request recieved
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print("Client {} connected".format(addr))
                msg = "[{}] entered our chatting room".format(addr)
                print(msg)
                broadcast(server_socket, sockfd, msg)
            else:
                # process data recieved from client
                try:
                    data = sock.recv(RECV_BUFFER)

                    if data:
                        msg = "[{}]{}".format(sock.getpeername(), data.decode("utf-8"))
                        print(msg)
                        broadcast(server_socket, sock, msg)
                    else:
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        msg = "Client offline\n"
                        broadcast(server_socket, sock, msg)
                except:
                    msg = "Client offline\n"
                    broadcast(server_socket, sock, msg)

    server_socket.close()


def broadcast(server_sock, sock, msg):
    for s in SOCKET_LIST:
        if s != server_sock and s != sock:
            try:
                s.send(msg.encode("utf-8"))
            except Exception as e:
                print(e)
                SOCKET_LIST.remove(s)
                s.close()

if __name__ == "__main__":
    sys.exit(chat_server())




