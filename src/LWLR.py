import sys
import numpy as np 
import math
from sklearn import preprocessing

def main(args):
	if len(sys.argv) < 2:
		print("USAGE: python linear_regression.py [hrr_data_total3.csv] [hrr_data_labels.csv]")
		exit(0)
	X = np.genfromtxt(args[0], delimiter=',')
	X = process_X(X)
	X = preprocessing.scale(X)
	Y = parse_Y(sys.argv[2])
	cutoff = int(len(X)*.7)
	x_train,y_train = X[:cutoff],Y[:cutoff]
	x_test,y_test = X[(cutoff+1):],Y[(cutoff+1):]
	
	x_train = x_train.tolist()
	y_train = y_train.tolist()

	tau = 1
	theta = np.empty((0))
	
	num = len(x_train)
	for j in range(0,num):
		W = np.empty([num,num])
		for m in range(0,num):
			x()
			#W[m,m] = math.exp(((X_train[])))
			break
	
	return


def parse_Y(Y_f):
	Y_arr = np.empty((0))
	Y_file = open(Y_f,'r')
	for line in Y_file:
		data = line.split()
	for label in data:
		Y_arr = np.append(Y_arr,int(label))
	return Y_arr

def process_X(X):
	X_new = np.delete(X,0,1)
	X_new = np.delete(X_new,0,1)
	return X_new












if __name__=="__main__":
	main(sys.argv[1:])


