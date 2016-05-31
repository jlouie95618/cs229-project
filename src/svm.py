import sys
import numpy as np
import util
from sklearn.svm import SVR
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
from sklearn import preprocessing

def main(args):
    if len(args) < 2:
        print("USAGE python svm.py [X_data] [Y_data]")
        exit(0)
    X = np.genfromtxt(args[0], delimiter = ',')
    Y = np.genfromtxt(args[1], delimiter = ',')
    X = util.fill_mean(X)
    X = preprocessing.scale(X)
    cutoff = int(len(X)*.7)
    x_train,y_train = X[:cutoff], Y[:cutoff]
    x_test, y_test = X[(cutoff+1):],Y[(cutoff+1):]

    clf = SVR(kernel='rbf',C=1e4,degree=3)
    
    clf.fit(x_train,y_train)
    pred = clf.predict(x_test)
    print("Residual sum of squares: %.5f"
      % np.mean((clf.predict(x_test) - y_test) ** 2))
    pred = clf.predict(x_test)

    # Explained variance score: 1 is perfect prediction
    print("R^2 score: %.8f" % r2_score(y_test,pred))
    print('explained variance score: %.8f' %explained_variance_score(y_test,pred))
    return



if __name__ == "__main__":
    main(sys.argv[1:])

