import pickle
import methods

TSA = 0

with open('initialsetup.pkl', 'rb') as input:
	TSA = pickle.load(input)

print (TSA.ID)
	
