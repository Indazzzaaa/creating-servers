import socket
import threading
import os
import time

# create a TCP/IP socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# get the size of the video file
filename = 'temp.mp4'  # replace with the name of your video file
filesize = os.path.getsize(filename)

# function to handle each client connection
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    
    # send the size of the video file to the client
    client_socket.send(str(filesize).encode())
    
    # send the video data to the client
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)
            print("Sending the packet.....")
            time.sleep(60)
            

    # close the client socket
    client_socket.close()

# listen for incoming connections
server_socket.listen(5)
print("Server is listening...")

# accept incoming connections and start a new thread for each connection
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()