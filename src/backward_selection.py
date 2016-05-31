import sys
import util

from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
import numpy as np


def main(args):
	X = np.genfromtxt(args[0], delimiter=',')
	#y = np.genfromtxt(args[1], delimiter=',')
	y = util.parse_Y(args[1])
	X = util.process_X(X)
	X = util.fill_mean(X)

	# Create the RFE object and rank each pixel
	svc = SVC(kernel="linear", C=1)
	rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
	rfe.fit(X, y)
	ranking = rfe.ranking_

	# Plot pixel ranking
	plt.matshow(ranking)
	plt.colorbar()
	plt.title("Ranking of pixels with RFE")
	plt.show()



if __name__ == "__main__":
    main(sys.argv[1:])