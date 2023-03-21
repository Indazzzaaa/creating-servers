# Chat room client
import socket
import threading

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-16"
BYTESIZE = 1024
NICKNAME = input("Enter Your Nickname : ")

# create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode(ENCODER)
            if message == 'NICK':
                client_socket.send(NICKNAME.encode(ENCODER))
            else:
                print(message)
        except:
            print("An error occured ...!")
            client_socket.close()
            break


def write():
    while True:
        message = f'{NICKNAME} : {input("")}'
        client_socket.send(message.encode(ENCODER))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
