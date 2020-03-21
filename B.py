import pickle
import methods
import socket

port1 = 7001

B = 0

with open('initialsetup.pkl', 'rb') as input:
	pickle.load(input)
	pickle.load(input)
	B = pickle.load(input)

'''
Communication between A and B
'''

s = socket.socket()          
port = port1
s.bind(('', port))           
s.listen()      
print ("socket is listening")      

c, addr = s.accept()      
print ('Connected to A') 
s.close()