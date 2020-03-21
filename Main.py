import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import hashlib
import random

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
	myID = -1
	myPrivateKey = -1
	myPublicKey = -1

	def __init__(self):
		self.myID = random.randint(1, int(1e9))
		key = generateKey()
		self.myPublicKey = key.publickey()
		self.myPrivateKey = key.privatekey()

class TSAserver:
	myID = -1
	myPrivateKey = -1
	myPublicKey = -1
	listOfIDs = {}

	def __init__(self):
		self.myID = random.randint(1, int(1e9))
		key = generateKey()
		self.myPublicKey = key.publickey()
		self.myPrivateKey = key.privatekey()
