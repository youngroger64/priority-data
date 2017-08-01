import socket
import sys
import ast
import pickle
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 30015))
##DATA_SET_PATH = (r'C:\Users\r.young\Downloads\fordTestA.csv')
##dataset = pd.read_csv(DATA_SET_PATH)
dataset = ast.literal_eval(sys.argv[1])
##dataset = ([[39.7485,10.7769,1224,49.0196,0.073947,624,96.1538,0,0,0,0,0,0.015875,366,0,0,1,70,2,0.77,-0.455,752,37.4937,0,646,0,0,0,1,11.5886]])

    
data_string = pickle.dumps(dataset)
    

s.sendall(data_string)

prediction = s.recv(1024)
pred = prediction[0]

print  (pred)
print('goodbye')
s.close()

##NOTE --ENCASE INCOMING DATA WITH ([ ])  WHEN USING COMMAND LINE ARG