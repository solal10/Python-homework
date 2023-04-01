import socket
import threading
import struct

ports = [9999, 9998, 9997, 9996, 9995]
i = input("enter index:")

connected_users = {}
connected_servers = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', ports[int(i)]))
ports.remove(ports[int(i)])
sock.listen(1)


def respond_to_client(conn_socket, client_address):
    print('start listening from', client_address)
    data = conn_socket.recv(1024)
    type_m, sub_type, leng, sub_leng = struct.unpack('>BBhh', data[:6])
    final_string = struct.unpack('>{}s'.format(leng), data[6:6 + leng])[0].decode('utf-8')
    if type_m == 0:
        if sub_type == 0:
            type_m = 1
            sub_type = 0
            server_strings = []
            for server_ip, server_port in connected_servers.items():
                server_string = f"({server_ip}:{server_port})\0"
                server_strings.append(server_string)
            final_string = "".join(server_strings)
            leng = len(final_string)
            sub_leng = 0
            sended_msg = struct.pack('>BBhh'.format(len(final_string)), type_m, sub_type, leng, sub_leng)+final_string.encode()
            conn_socket.sendall(sended_msg)
            connected_servers[client_address[0]] = client_address[1]
            print(connected_servers)
        elif sub_type == 1:
            type_m = 1
            sub_type = 1
            user_strings = []
            for user_name, user_details in connected_users.items():
                user_string = f"{user_name}\0"
                user_strings.append(user_string)
            final_string = "".join(user_strings)
            leng = len(final_string)
            sub_leng = 0
            sended_msg = struct.pack('>BBhh'.format(len(final_string)), type_m, sub_type, leng, sub_leng)+ final_string.encode()
            conn_socket.sendall(sended_msg)
        else:
            print("ERROR IN THE SUB_TYPE VALUE")
    if type_m == 1:
        if sub_type == 0:
            type_m, sub_type, leng, sub_leng = struct.unpack('>BBhh', data[:6])
            server_strings = struct.unpack(f'>{leng}s', data[6:])[0].decode().split('\0')[:-1]
            for server_string in server_strings:
                server_ip, server_port = server_string.strip('()').split(':')
                connected_servers[server_ip] = {'ip': server_ip, 'port': int(server_port)}
                sender_ip = client_address[0]
                sender_port = conn_socket.getsockname()[1]
                connected_servers[sender_ip] = {'ip': sender_ip, 'port': sender_port}
        elif sub_type == 1:
            type_m, sub_type, leng, sub_leng = struct.unpack('>BBhh', data[:6])
            user_strings = struct.unpack(f'>{leng}s', data[6:])[0].decode().split('\0')[:-1]
            for user_string in user_strings:
                connected_users[user_string] = {'ip': client_address[0], 'port': client_address[1]}
    if type_m == 2:
        if sub_type == 0:
            print("no idea what this does")
        elif sub_type == 1:
            leng = struct.unpack('>h', data[2:4])
            username = struct.unpack(f'>{leng}s', data[6:])[0].decode()
            connected_users[username] = {'ip': client_address[0], 'port': client_address[1]}
            print(f"New user connected: {username}")
        else:
            print("ERROR IN THE SUB_TYPE VALUE")
    if type_m == 3:
        if sub_type == 0:
            type_m, sub_type, leng, sub_leng = struct.unpack('>BBhh', data[:6])
            message = struct.unpack(f'>{leng}s', data[6:])[0].decode().split('\0')[:-1]
            if sub_leng == len(message[0]):
                message.insert(0, get_key_by_value(connected_users, client_address))
                if message[1] in connected_users:
                    receiver_info = connected_users[message[1]]
                    receiver_ip = receiver_info['ip']
                    receiver_port = receiver_info['port']
                    message_str = '\0'.join(message)
                    packet = struct.pack(f'>BBhh{len(message_str)}s',
                                         type_m, sub_type, len(message_str), len(message[0]) + len(message[1]) + 2,
                                         message_str.encode())
                    receiver_address = (receiver_ip, receiver_port)
                    try:
                        conn_socket.sendto(packet, receiver_address)
                    except Exception as e:
                        print(f"Error sending message to {receiver_address}: {e}")
                else:
                    # Receiver user not found in connected_users
                    # Send message to all servers in the network
                    message_str = '\0'.join(message)
                    packet = struct.pack(f'>BBhh{len(message_str)}s',
                                         type_m, sub_type, len(message_str), len(message[0]) + len(message[1]) + 2,
                                         message_str.encode())
                    for server_address in connected_servers:
                        try:
                            conn_socket.sendto(packet, server_address)
                        except Exception as e:
                            print(f"Error sending message to {server_address}: {e}")
            else:
                # message was transferred from another server
                sender, receiver, msg = message[0].split('\0')
                message_str = f"{sender}\0{receiver}\0{msg}"
                packet = struct.pack(f'>BBhh{len(message_str)}s',
                                     type_m, sub_type, len(message_str), len(sender) + len(receiver) + len(msg) + 2,
                                     message_str.encode())
                if receiver in connected_users:
                    # message is intended for a connected user on this server
                    receiver_info = connected_users[receiver]
                    receiver_ip = receiver_info['ip']
                    receiver_port = receiver_info['port']
                    receiver_address = (receiver_ip, receiver_port)
                    try:
                        conn_socket.sendto(packet, receiver_address)
                    except Exception as e:
                        print(f"Error sending message to {receiver_address}: {e}")
                else:
                    # message is not intended for a connected user on this server
                    for server_address in connected_servers:
                        try:
                            conn_socket.sendto(packet, server_address)
                        except Exception as e:
                            print(f"Error sending message to {server_address}: {e}")
        else:
            print("ERROR IN THE SUB_TYPE VALUE")


def waiting_for_client():
    while True:
        conn, client_address = sock.accept()
        print('new connection from', client_address)
        threading.Thread(target=respond_to_client, args=(conn, client_address)).start()


def get_key_by_value(d, value):
    for k, v in d.items():
        if v == value:
            return k
    # Value not found
    return None


threading.Thread(target=waiting_for_client, args=()).start()
for port in ports:
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        client_sock.connect(('127.0.0.1', port))
        type_m = 0
        sub_type = 0
        leng = 0
        subleng = 0
        message = struct.pack('>BBhh', type_m, sub_type, leng, subleng)
        client_sock.send(message)
        client_sock.close()
    except ConnectionRefusedError:
        print("no server available for connection")
