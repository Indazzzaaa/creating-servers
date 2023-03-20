from custom_print import printF
# TCP server side

import socket
import keyboard

# 1. address family  : ipv4 (AF_INET) , 2. Protocol : TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# way to get the ipaddress dynamically
printF(socket.gethostname())
printF(socket.getfqdn())
printF(socket.gethostbyname(socket.gethostname()))

# Bind our new socket to ip and port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# put socket in listening mode to listen for any possible connections
server_socket.listen()

# Listen forever to accept any connection
while True:
    # run until specific key is pressed
    event = keyboard.read_event()
    if event.name == 'q':
        print("Stopping the server..............")
        break
    # Accept every single connection and store tow pieces of information
    client_socket, client_address = server_socket.accept()
    # printF(socket_type=type(client_socket), only_client_socket=client_socket,
    #        address_type=type(client_address), address_only=client_address)
    print(f"Connected to {client_address}")

    # send message to client
    client_socket.send("You are welcome 😀".encode("utf-16"))

# close the connection
server_socket.close()
