import socket
import subprocess

# create a TCP/IP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# receive the size of the video file from the server
filesize = int(client_socket.recv(1024).decode())

# launch VLC media player and pipe the received video stream to it
player = subprocess.Popen([r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe', '-'], stdin=subprocess.PIPE)

# receive the video data from the server and pipe it to VLC
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    player.stdin.write(data)

# close the pipe and the client socket
player.stdin.close()
client_socket.close()
