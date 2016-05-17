import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main(args):
    print args
    if len(args) < 1: return
    X = np.loadtxt(args[0])


if __name__ == '__main__':
    main(sys.argv[1:])