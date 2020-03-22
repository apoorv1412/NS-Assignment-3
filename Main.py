import pickle
import methods
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import hashlib
import random

TSA_ID = random.randint(1, int(1e9))
TSA_key = methods.generateKey()

A_ID = random.randint(1, int(1e9))
A_key = methods.generateKey()

B_ID = random.randint(1, int(1e9))
B_key = methods.generateKey()


with open('initialsetup.pkl', 'wb') as output:
	pickle.dump(TSA_ID, output, pickle.HIGHEST_PROTOCOL)
	pickle.dump(TSA_key, output, pickle.HIGHEST_PROTOCOL)
	
	pickle.dump(A_ID, output, pickle.HIGHEST_PROTOCOL)
	pickle.dump(A_key, output, pickle.HIGHEST_PROTOCOL)

	pickle.dump(B_ID, output, pickle.HIGHEST_PROTOCOL)
	pickle.dump(B_key, output, pickle.HIGHEST_PROTOCOL)

