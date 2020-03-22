import pickle
import methods
import socket
import datetime
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import hashlib
import random
import datetime

ID = -1
key = -1
PrivateKey = -1
PublicKey = -1
listOfPublicKeys = {}

with open('initialsetup.pkl', 'rb') as input:
	ID = pickle.load(input)
	key = pickle.load(input)
	A_ID = pickle.load(input) 
	A_key = pickle.load(input)
	B_ID = pickle.load(input) 
	B_key = pickle.load(input) 

listOfPublicKeys[A_ID] = A_key.publickey()
listOfPublicKeys[B_ID] = B_key.publickey()
PrivateKey = key
PublicKey = key.publickey()

port1 = 4997
'''
Communication between A and TSA
'''	
s = socket.socket()          
port = port1
s.bind(('', port))    
s.listen()      
print ("socket is listening")      

c, addr = s.accept()      
print ('Connected to A')
hashed_file_from_A = c.recv(1024).decode() 
print (hashed_file_from_A) 
time = datetime.datetime.now()
expiry = time + datetime.timedelta(0,30)

message = hashed_file_from_A + "||" + str(A_ID) + "||" + str(time) + "||"
message += str(expiry) + "||" + str(listOfPublicKeys[B_ID]) + "||" + str(key)

hash_to_be_sent = methods.hash_string(message)
encrypted_hash_to_be_sent = methods.encrypt(hash_to_be_sent, key)
# encrypted_hash_to_be_sent = key.encrypt(hash_to_be_sent, 32)


c.send(str.encode(encrypted_hash_to_be_sent+"||"+message))



s.close()
