import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import hashlib
import random

'''
https://stackoverflow.com/a/49786230
'''

def hash_string(s):
	hashed_string = hashlib.sha256(s.encode()).hexdigest()
	return hashed_string

def checkIntegrity(hashed_string, s):
	if hashed_string == hashlib.sha256(s.encode()).hexdigest():
		return True
	return False

def encrypt(s, key):
	pass

def decrypt(s, key):
	pass

def generateKey():
	random_generator = Random.new().read
	return RSA.generate(1024, random_generator) 

class Client:
	ID = -1
	PrivateKey = -1
	PublicKey = -1
	Server = 0

	def addToServer(self):
		self.Server.addClient(self.ID, self.PublicKey)

	def __init__(self, Server):
		self.ID = random.randint(1, int(1e9))
		key = generateKey()
		self.PublicKey = key.publickey()
		self.PrivateKey = key
		self.Server = Server
		self.addToServer()

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
