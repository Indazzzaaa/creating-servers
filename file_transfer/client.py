import socket
from tqdm import tqdm

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-16"
BYTESIZE = 1024

# create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# receive the data in chunks and write it to a new file
filename = 'temp2.mp4'  # replace with the name of the file you want to save
filesize = int(client_socket.recv(1024).decode("utf-8"))
with open(filename, 'wb') as f:
    with tqdm(total=filesize, unit='B', unit_scale=True) as progress_bar:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
            progress_bar.update(len(data))

# close the file and socket
client_socket.close()
