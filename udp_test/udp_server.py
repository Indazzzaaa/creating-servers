# UPD server side
import socket

# Create server side socket IPV4 (AF_INET) and UPD (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind our socket to a tuple of (Ip address,port number)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# we are not listening or accepting connection since UPD is a connectionless protocol

# But we have to define the size of message  to be received
message, address = server_socket.recvfrom(1024)
print(f"From {address} Received : ", message.decode("utf-16"))
