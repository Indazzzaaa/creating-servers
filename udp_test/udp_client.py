# UPD client side
import socket

# create udp ipv4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some information via a connectionless protocol
# in this we first specify the message we want to send to and then the destination
client_socket.sendto("You are welcome 😀".encode("utf-16"),
                     (socket.gethostbyname(socket.gethostname()), 12345))
