import sys
from sklearn.cluster import KMeans

def main(args):
    print args
    if len(args) < 1: return

if __name__ == '__main__':
    main(sys.argv[1:])