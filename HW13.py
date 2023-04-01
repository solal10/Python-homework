import socket
import threading

ports = [9999, 9998, 9997, 9996, 9995]
i = input("enter index:")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('127.0.0.1', ports[int(i)]))
ports.remove(ports[int(i)])
sock.listen(1)


def respond_to_client(conn_socket, client_address):
    print('start listening from', client_address)
    while True:
        data = conn_socket.recv(1024)
        if not data:
            print('connection closed by', client_address)
            break
        print('received from', client_address, 'text', data.decode())
        conn_socket.send('world'.encode())


def waiting_for_client():
    while True:
        conn, client_address = sock.accept()
        print('new connection from', client_address)
        threading.Thread(target=respond_to_client, args=(conn, client_address)).start()


threading.Thread(target=waiting_for_client, args=()).start()
for port in ports:
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        client_sock.connect(('127.0.0.1', port))
        client_sock.send("hello".strip().encode())
        reply_data = client_sock.recv(1024)
        print('server reply', reply_data.decode())
        client_sock.close()
    except ConnectionRefusedError:
        print("no server available for connection")