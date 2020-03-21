from methods import Client, TSAserver
import pickle

Server = TSAserver()
A = Client(Server)
B = Client(Server)

with open('initialsetup.pkl', 'wb') as output:
	pickle.dump(Server, output, pickle.HIGHEST_PROTOCOL)
	pickle.dump(A, output, pickle.HIGHEST_PROTOCOL)
	pickle.dump(B, output, pickle.HIGHEST_PROTOCOL)

