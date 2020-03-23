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
	ID = int(pickle.load(input))
	key = pickle.load(input)
	B_ID = int(pickle.load(input))
	pickle.load(input) 

listOfID['B'] = B_ID
PrivateKey = key[0]
PublicKey = key[1]

port1 = 4009
port2 = 3009

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




time = 0
expiry = -1
message_from_tsa = -1

try:
	with open('certificate.pkl', 'rb') as input:
		message_from_tsa = pickle.load(input)
		splitted_message = message_from_tsa.split("||")
		expiry = splitted_message[5]
		if datetime.datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.now():
			time = -1
except:
	time = -1


if time == -1:
	while True:
		s = socket.socket()
		port = port1  
		s.connect(('127.0.0.1', port))

		print ('From A to TSA')
		s.send(str.encode(message))

		message_from_tsa = s.recv(2048)
		message_from_tsa = message_from_tsa.decode()

		with open('certificate.pkl', 'wb') as output:
			pickle.dump(message_from_tsa, output, pickle.HIGHEST_PROTOCOL)

		splitted_message = message_from_tsa.split("||")

		encrypted_hash = splitted_message[0]
		hashed_file = splitted_message[1]
		time = splitted_message[4]
		expiry = splitted_message[5]
		B_Public_Key = int(splitted_message[6])
		TSA_key = int(splitted_message[7])

		message_to_be_checked = ""
		for i in range(1, 7):
			message_to_be_checked += splitted_message[i] + "||"

		message_to_be_checked += splitted_message[7]


		decrypted_hash = methods.decrypt(encrypted_hash, TSA_key)
		s.close()


		if decrypted_hash==methods.hash_string(message_to_be_checked):
			break

else:
	splitted_message = message_from_tsa.split("||")
	encrypted_hash = splitted_message[0]
	hashed_file = splitted_message[1]
	time = splitted_message[4]
	expiry = splitted_message[5]
	B_Public_Key = int(splitted_message[6])
	TSA_key = int(splitted_message[7])

	message_to_be_checked = ""
	for i in range(1, 7):
		message_to_be_checked += splitted_message[i] + "||"
	message_to_be_checked += splitted_message[7]
	decrypted_hash = methods.decrypt(encrypted_hash, TSA_key)

	if decrypted_hash != methods.hash_string(message_to_be_checked):
		print("Integrity Failed")
		exit()



# # decrypted_hash = decrypted_hash.decode()
# # print(type(encrypted_hash))
# # encrypted_hash = encrypted_hash.decode()
# decrypted_hash = methods.decrypt(encrypted_hash, TSA_key)
# print(decrypted_hash)
# print(type(decrypted_hash))

# hash_to_be_checked = ""

# for i in range(1,8):
# 	hash_to_be_checked += splitted_message[i].decode()

# print(decrypted_hash==methods.hash_string(hash_to_be_checked))








#####################################################################################

'''
Communication between A and B
'''

s = socket.socket()
port = port2 
s.connect(('127.0.0.1', port))
# time_now = datetime.datetime.now()
encrypted_file = methods.encrypt(file, B_Public_Key)
message = encrypted_file + "||" + message_from_tsa
# message = 'from A to B' + '||' + str(time_now)
s.send(str.encode(message))
s.close()





