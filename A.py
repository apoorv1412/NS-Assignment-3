import pickle
import methods

A = 0

with open('initialsetup.pkl', 'rb') as input:
	pickle.load(input)
	A = pickle.load(input)

print (A.ID)
	
