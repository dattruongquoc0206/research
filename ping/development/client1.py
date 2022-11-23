import socket
import pandas as pd
import sys
from sklearn.tree import DecisionTreeClassifier


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #open file
    file = open("data/KDDTest.txt", "r")
    #data = file.read()
    #send 
    #s.send("KDDTest.txt".encode('utf-8'))
    #msg = s.recv(4361000).decode('utf-8')
    #print(f"[SERVER]: {msg}")
    #
    Lines = file.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        data = line
        s.send(data.encode('utf-8'))
    #msg = s.recv(4361000).decode('utf-8')
    #print(f"[SERVER]: {msg}")
    file.close()

s.close()
print(f"[DISCONNECTED]  disconnected.")