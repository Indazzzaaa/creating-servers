import socket
import os
import tqdm
import cv2

# create a TCP/IP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# receive the size of the video file from the server
filesize = int(client_socket.recv(1024).decode())
filename = 'received.mp4'
# create a progress bar using the tqdm library
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

# create an OpenCV video writer object to write the received frames to a file

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(filename, fourcc, 30.0, (640, 360))

# receive the video data from the server and write it to a file
received_size = 0
while received_size < filesize:
    data = client_socket.recv(1024)
    received_size += len(data)
    progress.update(len(data))
    video_writer.write(data)

# close the video writer object and the client socket
video_writer.release()
client_socket.close()

# play back the received video file using OpenCV
cap = cv2.VideoCapture(filename)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Received Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# release the OpenCV video capture and destroy the display window
cap.release()
cv2.destroyAllWindows()
