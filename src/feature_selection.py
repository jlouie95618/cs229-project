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
from sklearn.cross_validation import KFold


def main(args):
	print args
	X = np.genfromtxt(args[0], delimiter = ',')
	y = np.genfromtxt(args[1], delimiter = ',')
	#y = util.parse_Y(args[1])

	X = util.process_X(X)
	X = util.fill_mean2(X)
	#X_new = util.variance_threshold(X,int(args[2]))
	#X = preprocessing.normalize(X)
	#nums = [i for i in range(0,1,.01)]
	#lvscs = [LogisticRegression(C=i,dual=False).fit(X,y) for i in xrange(0,1,0.1)]
	#models = [SelectFromModel(lvscs[j],prefit=True) for j in range(0,len(lvscs))]
	#lvsc = LogisticRegression(C=.1,dual=False).fit(X,y) 
	#model  = SelectFromModel(lvsc,prefit=True) 
	#for m,mod in enumerate(model):

	#X_new = model.transform(X)
	#print(len(X_new[0]))

		#print(X_new[0,:])
		#out_file = open('new_model.txt','w+')
		#for r in X_new[0,:]

		#print("i = {}".format(i))
	#linear_regression(X_new,y)
	#print("------------------------------")
	#svm(X_new,y)
	#print("------------------------------")
	#boosting(X_new,y)
	k= 0
	if len(args)>=3:
		k = int(args[2])
	linear_regression(X,y,k)
	print("-----------------------------")
	svm(X,y,k)
	print("-----------------------------")
	boosting(X,y,k)
	return


def linear_regression(X,Y,k):
	if k > 0:
		y = Y
		totalRSS = 0
		totalR_sq = 0
		totalev = 0
		kf = KFold(len(X), n_folds=k)
		for train_index, test_index in kf:
			x_train, y_train = X[train_index], y[train_index]
			x_test,y_test = X[test_index], y[test_index]
			regr = linear_model.LinearRegression()
			regr.fit(x_train,y_train)
			#print("Residual sum of squares: %.5f"
		     # % np.mean((regr.predict(x_test) - y_test) ** 2))
			pred = regr.predict(x_test)
			totalRSS += np.mean((regr.predict(x_test) - y_test) ** 2)
			totalR_sq += r2_score(y_test, pred)
			totalev += explained_variance_score(y_test,pred)

			
		print("Residual sum of squares: {}".format(float(totalRSS)/float(k)))
		print('R^2 score: {}'.format(float(totalR_sq)/float(k)))
		print('explained variance score: {}'.format(float(totalev)/float(k)))
	else:
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

def svm(X,Y,k):

	if k > 0:
		y = Y
		totalRSS = 0
		totalR_sq = 0
		totalev = 0

		kf = KFold(len(X), n_folds=k)
		for train_index, test_index in kf:
			x_train, y_train = X[train_index], y[train_index]
			x_test,y_test = X[test_index], y[test_index]
			clf = SVR(kernel='rbf',C=1e5,degree=5)

			clf.fit(x_train,y_train)
			pred = clf.predict(x_test)
			#print("Residual sum of squares: %.5f"
			  #% np.mean((clf.predict(x_test) - y_test) ** 2))
			
			pred = clf.predict(x_test)
			totalRSS += np.mean((clf.predict(x_test) - y_test) ** 2)
			
			totalR_sq += r2_score(y_test, pred)
			
			totalev += explained_variance_score(y_test,pred)
		print("Residual sum of squares: {}".format(float(totalRSS)/float(k)))
		print('R^2 score: {}'.format(float(totalR_sq)/float(k)))
		print('explained variance score: {}'.format(float(totalev)/float(k)))
			
	else:
		X = preprocessing.scale(X)
		cutoff = int(len(X)*.7)
		x_train,y_train = X[:cutoff], Y[:cutoff]
		x_test, y_test = X[(cutoff+1):],Y[(cutoff+1):]

		clf = SVR(kernel='rbf',C=1e5,degree=5)

		clf.fit(x_train,y_train)
		pred = clf.predict(x_test)
		print("Residual sum of squares: %.5f"
		  % np.mean((clf.predict(x_test) - y_test) ** 2))
		pred = clf.predict(x_test)

		# Explained variance score: 1 is perfect prediction
		print('R^2 score: %.8f' % r2_score(y_test, pred))
		print('explained variance score: %.8f' %explained_variance_score(y_test,pred))

	return


def boosting(X,Y,k):
	if k > 0:
		y = Y
		totalRSS = 0
		totalR_sq = 0
		totalev = 0
		kf = KFold(len(X), n_folds=k)
		for train_index, test_index in kf:
			x_train, y_train = X[train_index], y[train_index]
			x_test,y_test = X[test_index], y[test_index]
			params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
	          'learning_rate': 0.01, 'loss': 'ls'}
			clf = ensemble.GradientBoostingRegressor(**params)
			clf.fit(x_train, y_train)
			mse = mean_squared_error(y_test, clf.predict(x_test))
			#print("MSE: %.4f" % mse)
			pred = clf.predict(x_test)
			# Explained variance score: 1 is perfect prediction
			#print("Variance Score: %.8f" % explained_variance_score(y_test,pred,multioutput='uniform_average'))
			#print('R^2 score: %.8f' % r2_score(y_test, pred))
			totalRSS += np.mean((clf.predict(x_test) - y_test) ** 2)
			totalR_sq += r2_score(y_test, pred)
			totalev += explained_variance_score(y_test,pred)
			print("Residual sum of squares: {}".format(float(totalRSS)/float(k)))
			print('R^2 score: {}'.format(float(totalR_sq)/float(k)))
			print('explained variance score: {}'.format(float(totalev)/float(k)))
	else:
		Z = np.arange(0,len(X[0]))
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
	#sorted_idx = sorted_idx[0:20]
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
