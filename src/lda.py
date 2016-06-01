import sys
import numpy as np
import util
from sklearn import preprocessing
from sklearn.lda import LDA




def quartiles(y):
	y= np.sort(y)
	q1 = y[len(y) * 1/4]
	q2 = y[len(y) * 2/4]
	q3 = y[len(y) * 3/4]
	
	return


def main(args):
	X = np.genfromtxt(args[0], delimiter = ',')
	y = np.genfromtxt(args[1], delimiter = ',')

	X = util.process_X(X)
	X = util.fill_mean2(X)
	X = preprocessing.scale(X)


	y = quartiles(y) 

	return












if __name__ == "__main__":
	main(sys.argv[1:])





