import sys
import util
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV



def compute_scores(X,n_features):
	n_components = np.arange(0, n_features, 5)

	pca = PCA()
	fa = FactorAnalysis()

	pca_scores, fa_scores = [], []
	for n in n_components:
		pca.n_components = n
		fa.n_components = n
		pca_scores.append(np.mean(cross_val_score(pca, X)))
		fa_scores.append(np.mean(cross_val_score(fa, X)))

	return pca_scores, fa_scores



def main(args):
	X = np.genfromtxt(args[0], delimiter=',')
	Y = np.genfromtxt(args[1], delimiter=',')
	X = util.process_X(X)
	X = util.fill_mean(X)
	print(compute_scores(X,len(X[0])))
	return












if __name__ == "__main__":
	main(sys.argv[1:])



