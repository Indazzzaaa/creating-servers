import socket
import cv2
import numpy as np

# create a TCP/IP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# receive the size of the video file from the server
filesize = int(client_socket.recv(1024).decode())

# create an OpenCV video reader object to read the received frames from memory
frame_width, frame_height = 640, 360
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_reader = cv2.VideoWriter('temp2.mp4', fourcc, 30, (frame_width, frame_height))
received_frames = []
received_size = 0

# receive the video data from the server and display the frames as they are received
while received_size < filesize:
    data = client_socket.recv(1024)
    received_size += len(data)
    frame_data = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imdecode(frame_data, cv2.IMREAD_COLOR)
    received_frames.append(frame)
    if len(received_frames) >= 30:
        for frame in received_frames:
            cv2.imshow('Received Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            video_reader.write(frame)
        received_frames = []

# play back the received video file using OpenCV
cap = cv2.VideoCapture('temp2.mp4')
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
