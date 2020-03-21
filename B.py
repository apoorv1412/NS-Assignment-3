import pickle
import methods

B = 0

with open('initialsetup.pkl', 'rb') as input:
	pickle.load(input)
	pickle.load(input)
	B = pickle.load(input)

print (B.ID)