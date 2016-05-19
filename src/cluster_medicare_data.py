import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main(args):
    print args
    if len(args) < 1: return
    X = np.genfromtxt(args[0], delimiter=',')
    print X 
    X = X[:, 1:]
    # for x in X:
    #     if np.isnan(np.sum(x)): print x
    # y = np.loadtxt(args[1])
    estimators = {'k_means_3': KMeans(n_clusters=3),
                    'k_means_4': KMeans(n_clusters=4),
                    'k_means_5': KMeans(n_clusters=5),
                    'k_means_6': KMeans(n_clusters=6),
                    'k_means_7': KMeans(n_clusters=7),
                    'k_means_8': KMeans(n_clusters=8) }

    for name, est in estimators.items():
        est.fit(X)
        values = est.cluster_centers_
        labels = est.labels_
        print name
        print values
        print labels
        for i in xrange(0, max(labels) + 1):
            count = 0
            for val in labels:
                if val == i: count += 1
            print str(i) + " : " + str(count) 



if __name__ == '__main__':
    main(sys.argv[1:])