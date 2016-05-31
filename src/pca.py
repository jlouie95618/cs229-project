import sys
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize


def main(args):
    print args
    if (len(args) < 1): return
    X = np.genfromtxt(args[0], delimiter=',')
    X.transpose()
    pca = PCA()
    pca.fit(X)
    print pca.explained_variance_ratio_
    print pca.n_components_



if __name__ == '__main__':
    main(sys.argv[1:])


# Example:
# >>> import numpy as np
# >>> from sklearn.decomposition import PCA
# >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# >>> pca = PCA(n_components=2)
# >>> pca.fit(X)
# PCA(copy=True, n_components=2, whiten=False)
# >>> print(pca.explained_variance_ratio_) 
# [ 0.99244...  0.00755...]