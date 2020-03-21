import pickle
import methods
import socket
import datetime

port1 = 5001
port2 = 7001

A = 0

with open('initialsetup.pkl', 'rb') as input:
	pickle.load(input)
	A = pickle.load(input)

#####################################################################################

'''
Communication between A and TSA
'''

s = socket.socket()
port = port1  
s.connect(('127.0.0.1', port))
time_now = datetime.datetime.now()
message = 'from A to TSA' + '||' + str(time_now)
s.send(str.encode(message))
s.close()

#####################################################################################

'''
Communication between A and B
'''

s = socket.socket()
port = port2  
s.connect(('127.0.0.1', port))
time_now = datetime.datetime.now()
message = 'from A to B' + '||' + str(time_now)
s.send(str.encode(message))
s.close() 
