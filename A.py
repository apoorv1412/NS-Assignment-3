# import hashlib


# def hash_string(s):
# 	hashed_string = hashlib.sha256(s.encode()).hexdigest()
# 	return hashed_string


# a = 'The little brown fox jumped'
# b = hash_string(a)
# if b == hash_string(a):
# 	print ('OK')
# else:
# 	print ('NO')

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('encrypt this message', 32)
#message to encrypt is in the above line 'encrypt this message'

print ('encrypted message:', encrypted) #ciphertext