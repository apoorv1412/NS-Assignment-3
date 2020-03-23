import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import hashlib
import random

'''
https://stackoverflow.com/a/49786230
'''

block_size = 30
p = 45293
q = 45389
phi = (p-1)*(q-1)
n = 2055803977

primes = [2345699, 2345713, 2345729, 2345731, 2345743, 2345753, 2345803, 2345807, 2345809, 2345831]

def hash_string(s):
	hashed_string = hashlib.sha256(s.encode()).hexdigest()
	return hashed_string

def checkIntegrity(hashed_string, s):
	if hashed_string == hashlib.sha256(s.encode()).hexdigest():
		return True
	return False

def encrypt(message, e):
	binary_string = ''
	for a in message:
		b = bin(ord(a))[2:]
		b = '0'*(8-len(b)) + b
		binary_string += b
	rem = len(binary_string) % block_size
	binary_string += '1'
	binary_string += (block_size-rem-1)*'0'

	encrypted_string = ''

	num_blocks = len(binary_string) // block_size
	for i in range(num_blocks):
		curr = binary_string[i * block_size : (i + 1) * block_size]
		curr = int(curr,2)
		curr = pow(curr,e,n)
		encrypted_string += str(curr)
		encrypted_string += ' '
	return encrypted_string

def decrypt(message, d):
	binary_string = ''
	message = message.rstrip(' ')
	message = list(map(int, message.split()))
	for a in message:
		curr = a
		curr = pow(curr,d,n)
		curr = bin(curr)[2:]
		curr = '0' * (block_size - len(curr)) + curr
		binary_string += curr

	y = binary_string

	binary_string = binary_string.rstrip('0')
	binary_string = binary_string[:len(binary_string) - 1]
	
	decrypted_string = ''
	num_chars = len(binary_string) // 8

	for i in range(num_chars):
		curr = binary_string[i * 8 : (i + 1) * 8]
		curr = int(curr,2)
		decrypted_string += chr(curr)

	return decrypted_string

def modInverse(a, m) : 
	m0 = m 
	y = 0
	x = 1
	if (m == 1) : 
		return 0
	while (a > 1) : 
		q = a // m 
		t = m 
		m = a % m 
		a = t 
		t = y
		y = x - q * y 
		x = t
	if (x < 0) : 
		x = x + m0 
	return x

def generateKey():
	random_prime =  random.randint(0,len(primes)-1)
	key1 = primes[random_prime]
	primes.pop(random_prime)
	key2 = modInverse(key1, phi)
	return [key1, key2]

class Client:
	ID = -1
	PrivateKey = -1
	PublicKey = -1
	ListOfID = {}

	def addToServer(self):
		self.Server.addClient(self.ID, self.PublicKey)

	def __init__(self, Server):
		self.ID = random.randint(1, int(1e9))
		key = generateKey()
		self.PublicKey = key.publickey()
		self.PrivateKey = key

	def addID(self, client, clientID):
		print (client, clientID)
		self.ListOfID[client] = clientID

class TSAserver:
	ID = -1
	PrivateKey = -1
	PublicKey = -1
	listOfPublicKeys = {}

	def __init__(self):
		self.ID = random.randint(1, int(1e9))
		key = generateKey()
		self.PublicKey = key.publickey()
		self.PrivateKey = key

	def addClient(self, ID, Key):
		self.listOfPublicKeys[ID] = Key
