import sys
import numpy as np
import matplotlib.pyplot as plt
import util
from sklearn import preprocessing
from sklearn.metrics import explained_variance_score
from sklearn import ensemble
from sklearn import datasets
from sklearn.metrics import mean_squared_error


def main(args):
	if(len(args)<2):
		print("USAGE: python gradient_boosting.py [training features] [training labels]")
	X = np.genfromtxt(args[0], delimiter=',')
	Y = np.genfromtxt(args[1], delimiter=',')
	X = preprocessing.scale(X)
	cutoff = int(len(X)*.7)
	x_train, y_train = X[:cutoff], Y[:cutoff]
	x_test, y_test = X[(cutoff+1):], Y[(cutoff+1):]

	params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
	clf = ensemble.GradientBoostingRegressor(**params)
	clf.fit(x_train, y_train)
	mse = mean_squared_error(y_test, clf.predict(x_test))
	print("MSE: %.4f" % mse)
	pred = clf.predict(x_test)
	# Explained variance score: 1 is perfect prediction
	print("Variance Score: %.4f" % explained_variance_score(y_test,pred,multioutput='uniform_average'))


	feature_importance = clf.feature_importances_
	# make importances relative to max importance
	feature_importance = 100.0 * (feature_importance / feature_importance.max())
	sorted_idx = np.argsort(feature_importance)
	pos = np.arange(sorted_idx.shape[0]) + .5
	plt.subplot(1, 2, 2)
	plt.barh(pos, feature_importance[sorted_idx], align='center')
	#plt.yticks(pos, boston.feature_names[sorted_idx])
	plt.xlabel('Relative Importance')
	plt.title('Variable Importance')
	plt.show()

	return





if __name__ == "__main__":
	main(sys.argv[1:])

