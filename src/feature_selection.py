import sys
import util
import numpy as np
from sklearn import preprocessing
from sklearn.feature_selection import VarianceThreshold

def variance_threshold(X, threshold_val=None):
    sel = VarianceThreshold()
    if threshold_val != None: 
        sel = VarianceThreshold(threshold_val)
    return sel.fit_transform(X)

def main(args):
    print args
    if len(args) < 1: return
    X = np.genfromtxt(args[0], delimiter=',')
    X = util.fill_mean(X)
    print X
    print len(X[0])
    if len(args) == 2: 
        X = variance_threshold(X, float(args[1]))
    else:
        X = variance_threshold(X)
    print len(X[0])

if __name__ == '__main__':
    main(sys.argv[1:])