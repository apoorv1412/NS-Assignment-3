import pickle
import methods
import socket
import datetime

ID = -1
key = -1
PrivateKey = -1
PublicKey = -1
listOfID = {}

with open('initialsetup.pkl', 'rb') as input:
	pickle.load(input)
	pickle.load(input)
	ID = pickle.load(input) 
	key = pickle.load(input)
	B_ID = pickle.load(input) 
	pickle.load(input) 

listOfID['B'] = B_ID
PrivateKey = key
PublicKey = key.publickey()

port1 = 4999
port2 = 7000

#####################################################################################

'''
Communication between A and TSA
'''

f = open('file.txt', 'r')
file = ''
for line in f:
	file += line

hashed_file = methods.hash_string(file)
message = hashed_file + '||' + str(listOfID['B'])
print (message)

s = socket.socket()
port = port1  
s.connect(('127.0.0.1', port))

print ('From A to TSA')
s.send(str.encode(message))
s.close()



#####################################################################################

'''
Communication between A and B
'''

# s = socket.socket()
# port = port2  
# s.connect(('127.0.0.1', port))
# time_now = datetime.datetime.now()
# message = 'from A to B' + '||' + str(time_now)
# s.send(str.encode(message))
# s.close() 
