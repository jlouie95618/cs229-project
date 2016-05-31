import sys
import numpy as np
import util
from sklearn.svm import LinearSVC
from sklearn.svm import SVR
from sklearn.feature_selection import SelectFromModel
from sklearn import linear_model
from sklearn import datasets
from sklearn import preprocessing
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn import ensemble
from sklearn import datasets
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def main(args):
	X = np.genfromtxt(args[0], delimiter = ',')
	y = np.genfromtxt(args[1], delimiter = ',')
	#y = util.parse_Y(args[1])

	X = util.process_X(X)
	X = util.fill_mean(X)
	X = preprocessing.scale(X)
	lvsc = LogisticRegression(C=0.1,dual=False).fit(X,y)
	model = SelectFromModel(lvsc,prefit=True)
	X_new = model.transform(X)

	linear_regression(X_new,y)
	svm(X_new,y)
	boosting(X_new,y)

	return


def linear_regression(X,Y):
	X = preprocessing.scale(X)
	cutoff = int(len(X)*.7)
	x_train, y_train = X[:cutoff], Y[:cutoff]
	x_test,y_test = X[(cutoff+1):], Y[(cutoff+1):]
	regr = linear_model.LinearRegression()
	regr.fit(x_train,y_train)
	print("Residual sum of squares: %.5f"
      % np.mean((regr.predict(x_test) - y_test) ** 2))
	pred = regr.predict(x_test)
	

	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.8f' % regr.score(x_test, y_test))
	print('R^2 score: %.8f' % r2_score(y_test, pred))
	print('explained variance score: %.8f' %explained_variance_score(y_test,pred))

	return

def svm(X,Y):
    cutoff = int(len(X)*.7)
    x_train,y_train = X[:cutoff], Y[:cutoff]
    x_test, y_test = X[(cutoff+1):],Y[(cutoff+1):]

    clf = SVR(kernel='rbf',C=1e6,degree=4)
    
    clf.fit(x_train,y_train)
    pred = clf.predict(x_test)
    print("Residual sum of squares: %.5f"
      % np.mean((clf.predict(x_test) - y_test) ** 2))
    pred = clf.predict(x_test)

    # Explained variance score: 1 is perfect prediction
    print('R^2 score: %.8f' % r2_score(y_test, pred))
    print('explained variance score: %.8f' %explained_variance_score(y_test,pred))
    return


def boosting(X,Y):
	Z = np.arange(0,len(X[0]))
	cutoff = int(len(X)*.7)
	x_train, y_train = X[:cutoff], Y[:cutoff]
	x_test, y_test = X[(cutoff+1):], Y[(cutoff+1):]

	params = {'n_estimators': 1000, 'max_depth': 5, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
	clf = ensemble.GradientBoostingRegressor(**params)
	clf.fit(x_train, y_train)
	mse = mean_squared_error(y_test, clf.predict(x_test))
	print("MSE: %.4f" % mse)
	pred = clf.predict(x_test)
	# Explained variance score: 1 is perfect prediction
	print("Variance Score: %.8f" % explained_variance_score(y_test,pred,multioutput='uniform_average'))
	print('R^2 score: %.8f' % r2_score(y_test, pred))


	# compute test set deviance
	test_score = np.zeros((params['n_estimators'],), dtype=np.float64)

	for i, y_pred in enumerate(clf.staged_predict(x_test)):
	    test_score[i] = clf.loss_(y_test, y_pred)

	plt.figure(figsize=(12, 6))
	plt.subplot(1, 2, 1)
	plt.title('Deviance')
	plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',
	         label='Training Set Deviance')
	plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
	         label='Test Set Deviance')
	plt.legend(loc='upper right')
	plt.xlabel('Boosting Iterations')
	plt.ylabel('Deviance')



	feature_importance = clf.feature_importances_
	# make importances relative to max importance
	feature_importance = 100.0 * (feature_importance / feature_importance.max())
	sorted_idx = np.argsort(feature_importance)
	sorted_idx = sorted_idx[0:20]
	pos = np.arange(sorted_idx.shape[0]) + .5
	plt.subplot(1, 2, 2)
	plt.barh(pos, feature_importance[sorted_idx], align='center')
	plt.yticks(pos, Z[sorted_idx])
	plt.xlabel('Relative Importance')
	plt.title('Variable Importance')
	plt.show()

	return




if __name__ == "__main__":
	main(sys.argv[1:])


