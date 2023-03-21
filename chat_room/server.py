# Chat Room Server Side
import socket
import threading

# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-16"
BYTESIZE = 1024

# create a server socket, bind it to a ip/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Create two blank lists to store connected client sockets and their names
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} Left .... !".encode(ENCODER))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server_socket.accept()
        print(f"connected with {address}")
        client.send('NICK'.encode(ENCODER))
        nickname = client.recv(1024).decode(ENCODER)
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f'{nickname} Just Joined..!'.encode(ENCODER))
        client.send('Connected to the server ... '.encode(ENCODER))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server started ......")
receive()
