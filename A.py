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

port1 = 4996
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

s = socket.socket()
port = port1  
s.connect(('127.0.0.1', port))

print ('From A to TSA')
s.send(str.encode(message))

new_message = s.recv(2048)

splitted_message = new_message.split(str.encode("||"))
encrypted_hash = splitted_message[0]
hashed_file = splitted_message[1]
time = splitted_message[4]
expiry = splitted_message[5]
B_key = splitted_message[6]

B_key = RSA.importKey(B_key)
TSA_key = splitted_message[7]
TSA_key = RSA.importKey(TSA_key)

decrypted_hash = methods.decrypt(encrypted_hash, TSA_key)







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
