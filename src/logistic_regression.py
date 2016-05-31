import sys
import numpy as np
from sklearn import linear_model
import util
import feature_selection
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import KFold


def main(args):
    print args
    if len(sys.argv) < 2:
        print("USAGE: python logistic_regression.py [feature matrix] [values]")
        exit(0)
    X = np.genfromtxt(args[0], delimiter=',')
    y = np.genfromtxt(args[1], delimiter=',')
    y[y >= 1] = 1
    y[y < 1] = 0
    # X = util.item_item_collab_filtering(X, 100, -1)
    X = util.fill_mean(X, -1)
    print X
    print y
    print X.shape
    print y.shape
    X = feature_selection.variance_threshold(X, 1)
    X = preprocessing.normalize(X)

    results = []

    kfolds = False
    if len(args) >= 3: 
        kfolds = True
    if kfolds:
        kf = KFold(len(X), n_folds=int(args[2]))
        for train_index, test_index in kf:
            X_train, y_train = X[train_index], y[train_index]
            X_test,y_test = X[test_index], y[test_index]
            logreg = linear_model.LogisticRegression()
            logreg.fit(X_train, y_train)
            accuracy = accuracy_score(y_test, logreg.predict(X_test))
            print accuracy
            results.append(accuracy)
            print '\n'
    else:
        cutoff = int(len(X)*.7)
        X_train, y_train = X[:cutoff], y[:cutoff]
        X_test, y_test = X[cutoff + 1:], y[cutoff + 1:]
        logreg = linear_model.LogisticRegression()
        logreg.fit(X_train, y_train)
        accuracy = accuracy_score(y_test, logreg.predict(X_test))
        results.append(accuracy)
        print accuracy

    print 'mean: %s' % np.mean(results)

if __name__ == '__main__':
    main(sys.argv[1:])