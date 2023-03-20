# TCP client side

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to a server located at a given ip and port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# to receive a message from server you must specify the max number of bytes to receive
message = client_socket.recv(1024)
print("Received : ", message.decode("utf-16"))


# close the connection
client_socket.close()
