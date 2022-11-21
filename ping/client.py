import socket
import pandas as pd
import sys
from sklearn.tree import DecisionTreeClassifier


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #open file
    file = open("data/yt.txt", "r")
    data = file.read()
    #send 
    s.send("yt.txt".encode('utf-8'))
    msg = s.recv(2048).decode('utf-8')
    print(f"[SERVER]: {msg}")
    #
    s.send(data.encode('utf-8'))
    msg = s.recv(2048).decode('utf-8')
    print(f"[SERVER]: {msg}")
    file.close()

s.close()
print(f"[DISCONNECTED]  disconnected.")