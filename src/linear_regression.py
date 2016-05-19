import sys
from sklearn import linear_model
from sklearn import datasets
from sklearn import preprocessing
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
import numpy as np


def main(args):
	if len(sys.argv) < 1:
		print("USAGE: python linear_regression.py [hrr_data_total3.csv] [hrr_data_labels.csv]")
		exit(0)
	X = np.genfromtxt(args[0], delimiter=',')
	X = process_X(X)
	X = preprocessing.scale(X)
	Y = parse_Y(sys.argv[2],len(X))
	X_train = X[:215]
	Y_train = Y[:215]
	X_test = X[215:]
	Y_test = Y[215:]
	regr = linear_model.LinearRegression()
	regr.fit(X_train,Y_train)
	print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(X_test) - Y_test) ** 2))
	pred = regr.predict(X_test)
	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.8f' % regr.score(X_test, Y_test))

	return

def parse_Y(Y_f,num):
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







if __name__ == "__main__":
	main(sys.argv[1:])

