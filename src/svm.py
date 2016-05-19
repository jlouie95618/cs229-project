import sys
import numpy as np
from sklearn.svm import SVR
from sklearn.metrics import explained_variance_score
from sklearn import preprocessing

def main(args):
	if len(args) < 2:
		print("USAGE python svm.py [X_data] [Y_data]")
		exit(0)
	X = np.genfromtxt(args[0], delimiter=',')
	X = preprocessing.scale(X)
	X = process_X(X)
	Y = parse_Y(args[1])
	cutoff = int(len(X)*.7)
	X_train = X[:cutoff]
	Y_train = Y[:cutoff]
	X_test = X[(cutoff+1):]
	Y_test = Y[(cutoff+1):]
	clf = SVR(kernel='rbf',C=1e4,degree=3)
	clf.fit(X_train,Y_train)
	pred = clf.predict(X_test)
	print("Residual sum of squares: %.2f"
      % np.mean((clf.predict(X_test) - Y_test) ** 2))
	pred = clf.predict(X_test)
	# Explained variance score: 1 is perfect prediction
	print("Variance Score: %.4f" % explained_variance_score(Y_test,pred,multioutput='uniform_average'))
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


if __name__ == "__main__":
	main(sys.argv[1:])

