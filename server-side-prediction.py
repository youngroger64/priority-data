from sklearn import preprocessing
import sys
import ast
from sklearn.externals import joblib
import socket
import pickle

loaded_model = joblib.load(r'C:\Users\r.young\LR_model.sav')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 30015))
s.listen(1)


conn, addr = s.accept()

##while loop
data = conn.recv(1024)
data = pickle.loads(data)
for i in data:
        
        print(i)
    
result = loaded_model.predict(data)

for i in result:
        
        print(i)
        
        conn.send(i)
   

