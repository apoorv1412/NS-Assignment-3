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
	ID = int(pickle.load(input))
	key = pickle.load(input)
	A_ID = int(pickle.load(input))
	A_key = pickle.load(input)
	B_ID = int(pickle.load(input))
	B_key = pickle.load(input)

# print(key)
# print(A_key)
# print(B_key)

listOfPublicKeys[A_ID] = A_key[0]
listOfPublicKeys[B_ID] = B_key[0]
PrivateKey = key[0]
PublicKey = key[1]

PrivateKey, PublicKey = PublicKey, PrivateKey

port1 = 4009
'''
Communication between A and TSA
'''	
s = socket.socket()          
port = port1
s.bind(('', port))    
s.listen()      
print ("socket is listening")      

while True:
	c, addr = s.accept()      
	print ('Connected to A')
	hashed_file_from_A = c.recv(2048).decode() 
	time = datetime.datetime.now()
	expiry = time + datetime.timedelta(0,300)

	message = hashed_file_from_A + "||" + str(A_ID) + "||" + str(time) + "||" + str(expiry)

	# print("message",message)

	# print(message,"---")

	hash_to_be_sent = methods.hash_string(message)

	# print(hash_to_be_sent)
	# hash_to_be_sent = str.encode(hash_to_be_sent)
	encrypted_hash_to_be_sent = methods.encrypt(hash_to_be_sent, PrivateKey)
	# print(type(encrypted_hash_to_be_sent))
	# encrypted_hash_to_be_sent = str.encode(encrypted_hash_to_be_sent)
	# encrypted_hash_to_be_sent = key.encrypt(hash_to_be_sent, 32)

	# byte_message = str.encode(encrypted_hash_to_be_sent+"||"+message)
	# byte_message += listOfPublicKeys[B_ID].exportKey("PEM") + str.encode("||") 
	# byte_message += PublicKey.exportKey("PEM")

	# print(byte_message)
	# print("---------")
	# print(PublicKey.exportKey("PEM"))

	c.send(str.encode(encrypted_hash_to_be_sent+"||"+message))
s.close()


