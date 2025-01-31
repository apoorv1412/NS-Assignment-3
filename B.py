import pickle
import methods
import socket
import datetime

port1 = 3009

key = []
A_ID = -1
TSA_ID = -1
Public_Key_TSA = -1
Public_Key_A = -1


with open('initialsetup.pkl', 'rb') as input:
	TSA_ID = pickle.load(input)
	Public_Key_TSA = pickle.load(input)[0]
	A_ID = int(pickle.load(input))
	Public_Key_A = pickle.load(input)[0]
	B_ID = int(pickle.load(input))
	key = pickle.load(input)

'''
Communication between A and B
'''
s = socket.socket()          
port = port1
s.bind(('', port))           
s.listen()      
print ("socket is listening")      

while True:
	c, addr = s.accept()      
	print ('Connected to A')
	message_from_A = c.recv(2048).decode() 
	# c.recv()
	# print(message_from_A)

	splitted_message = message_from_A.split("||")

	encrypted_file = splitted_message[0]
	encrypted_certificate = splitted_message[1]
	hashed_file = splitted_message[2]
	time = splitted_message[5]
	expiry = splitted_message[6]

	time_now = datetime.datetime.now();

	decrypted_certificate = ""

	for i in range(2,6):
		decrypted_certificate += splitted_message[i] + "||"

	decrypted_certificate += splitted_message[6]

	if methods.decrypt(encrypted_certificate, Public_Key_TSA) != methods.hash_string(decrypted_certificate):
		print("Invalid Certificate")
		continue
	file = methods.decrypt(encrypted_file, key[1])
	if hashed_file != methods.hash_string(file):
		print("File Incorrect")
		continue

	if datetime.datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S.%f') < time_now:
		print("Expiry Certificate")
		continue
	else:
		print("Expiry Time", datetime.datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S.%f'))
		print("Current Time", time_now)

	print(file)
s.close()

