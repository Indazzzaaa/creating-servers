import socket

# create a TCP/IP socket object
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-16"
BYTESIZE = 1024
# create a server socket, bind it to a ip/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Accept any incoming connection and let them know they are connected
print("Server is running...\n")
client_socket, client_address = server_socket.accept()
print(f"connected to client : {client_address}")

# open the file
import os
filename = './temp.mp4'  # replace with the path to your file
filesize = os.path.getsize(filename)
client_socket.send(str(filesize).encode('utf-8'))
with open(filename, 'rb') as f:
    # read the file in chunks and send them to the server
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.sendall(data)

# close the file and socket
server_socket.close()
