import socket

UDP_IP = '0.0.0.0'
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))
clients = {}
while True:
    data, addr = sock.recvfrom(1024)
    print('received message:', data.decode())
    if addr in clients.values():
        name = data.decode().split()[0]
        if name in clients:
            sock.sendto(data.decode().split(" ",1)[1].encode(), clients[name])
        else:
            sock.sendto("אין כזה משתמש".encode(),addr)
    else:
        clients[data.decode()] = addr
