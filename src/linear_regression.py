import sys
from sklearn import linear_model
from sklearn import datasets
from sklearn import preprocessing
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
import numpy as np
import util

def main(args):
	if len(sys.argv) < 2:
		print("USAGE: python linear_regression.py [feature matrix] [values]")
		exit(0)
	X = np.genfromtxt(args[0], delimiter=',')
	Y = np.genfromtxt(args[1], delimiter=',')
	#Y = util.parse_Y(args[1])
	X = util.process_X(X)
	X = util.fill_mean(X)
	print(X)
	print(Y)
	X = preprocessing.normalize(X)
	cutoff = int(len(X)*.7)
	x_train, y_train = X[:cutoff], Y[:cutoff]
	x_test,y_test = X[(cutoff+1):], Y[(cutoff+1):]
	regr = linear_model.LinearRegression()
	regr.fit(x_train,y_train)
	print("Residual sum of squares: %.5f"
      % np.mean((regr.predict(x_test) - y_test) ** 2))
	pred = regr.predict(x_test)
	

	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.8f' % regr.score(x_test, y_test))
	print('R^2 score: %.8f' % r2_score(y_test, pred))
	print('explained variance score: %.8f' %explained_variance_score(y_test,pred))

	return




if __name__ == "__main__":
	main(sys.argv[1:])

