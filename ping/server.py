import socket
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

datacols = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]
  
data_train=pd.read_csv('https://raw.githubusercontent.com/twelfthywn/research/main/data/KDDTrain%2B.txt', sep=",", names=datacols)
data_test=pd.read_csv('https://raw.githubusercontent.com/twelfthywn/research/main/data/KDDTest%2B.txt', sep=",", names=datacols)
#drop unwanted column lasted flag 
data_train = data_train.iloc[:,:-1]
data_test = data_test.iloc[:,:-1]

def none_preprocessing(train, test):
  for i in ['protocol_type',"service","flag"]:
    train[i] = train[i].astype('category').cat.codes
    test[i] = test[i].astype('category').cat.codes

  X_train = train.iloc[:,:40]
  y_train = train.iloc[:,-1]

  X_test = test.iloc[:,:40]
  y_test = test.iloc[:,-1]
  return X_train, y_train, X_test, y_test

X_train, y_train, X_test, y_test = none_preprocessing(data_train,data_test)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
          filename = conn.recv(2048).decode('utf-8')
          print(f"[RECV] Receiving the filename.")
          file = open(filename, "w")
          conn.send("Filename received.".encode('utf-8'))
          #
          data = conn.recv(2048).decode('utf-8')
          print(f"[RECV] Receiving the file data.")
          file.write(data)
          conn.send("File data received".encode('utf-8'))
          #
          file.close()
          if not data:
            break

conn.close()
print(f"[DISCONNECTED] {addr} disconnected.")