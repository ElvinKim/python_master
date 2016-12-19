import socket
from fib import fib
import threading
import concurrent.futures


pool = concurrent.futures.ProcessPoolExecutor(5)


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        future = pool.submit(fib, n)
        result = future.result()
        resp = str(result).encode("ascii") + b"\n"
        client.send(resp)
    print("Closed")
    client.close()


if __name__ == "__main__":
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_sock.bind(("", 7777))
    server_sock.listen(5)

    while True:
        client, client_addr = server_sock.accept()
        print("[CONNECTION]", client_addr)
        threading.Thread(target=fib_handler, args=(client,)).start()
