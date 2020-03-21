import pickle
import methods
import socket
import datetime

port1 = 5001

TSA = 0

with open('initialsetup.pkl', 'rb') as input:
	TSA = pickle.load(input)
	
s = socket.socket()          
port = port1
s.bind(('', port))         
s.listen()      
print ("socket is listening")      

c, addr = s.accept()      
print ('Connected to A')  
s.close()