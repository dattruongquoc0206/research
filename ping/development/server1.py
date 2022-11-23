import socket
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
          #filename = conn.recv(4361000).decode('utf-8')
          #print(f"[RECV] Receiving the filename.")
          #file = open(filename, "w")
          #conn.send("Filename received.".encode('utf-8'))
          #
          data = conn.recv(4361000).decode('utf-8')
          #print(f"[RECV] Receiving the file data.")
          #file.write(data)
          #conn.send("File data received".encode('utf-8'))
          #
          print(data)
          #file.close()
          if not data:
            break

conn.close()
print(f"[DISCONNECTED] {addr} disconnected.")