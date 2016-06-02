import sys
import numpy as np
import util
from sklearn import preprocessing
from sklearn.lda import LDA
from sklearn.cross_validation import KFold




def quartiles(y):
	sort= np.sort(y)
	q1 = sort[len(sort) * 1/4]
	q2 = sort[len(sort) * 2/4]
	q3 = sort[len(sort) * 3/4]
	#q4 = sort[len(sort) * 4/10]
	#q5 = sort[len(sort) * 5/10]
	#q6 = sort[len(sort) * 6/10]
	#q7 = sort[len(sort) * 7/10]
	#q8 = sort[len(sort) * 8/10]
	#q9 = sort[len(sort) * 9/10]
	


	for i,label in enumerate(y):
		if label <= q1:
			y[i] = 1
		elif label <= q2:
			y[i] = 2
		elif label <= q3:
			y[i] = 3
		else:
			y[i] = 4
		#elif label <= q5:
		#	y[i] = 5
		#elif label <= q6:
		#	y[i] = 6
		#elif label <= q7:
		#	y[i] = 7
		#elif label <= q8:
		#	y[i] = 8
		#elif label <= q9:
		#	y[i] = 9
		#else:
		#	y[i] = 10
	return y


def main(args):
	X = np.genfromtxt(args[0], delimiter = ',')
	y = np.genfromtxt(args[1], delimiter = ',')

	X = util.process_X(X)
	X = util.fill_mean2(X)
	X = preprocessing.scale(X)


	y = quartiles(y) 

	kfolds = False
	if len(args) >= 3: 
		kfolds = True
	if kfolds:
		kf = KFold(len(X), n_folds=int(args[2]))
		for train_index, test_index in kf:
			x_train, y_train = X[train_index], y[train_index]
			x_test,y_test = X[test_index], y[test_index]
			clf = LDA()
			clf.fit(x_train,y_train)
			
			correct = 0
			incorrect = 0
			total = 0
			quartile_bad = np.empty((0))
			for i,example in enumerate(x_train):
				pred = clf.predict(example)
				if pred == y_train[i]:
					correct +=1
					total+=1
					#print("Match! Percent Correct = {}".format(float(correct)/float(total)))
				else:
					incorrect += 1
					total +=1
					quartile_bad = np.append(quartile_bad,abs(pred-y_train[i]))

					#print("Incorrect :(  Percent Correct = {}".format(float(correct)/float(total)))
			print("Percent Correct = {}".format(float(correct)/float(total)))
			print(quartile_bad)
			print(np.median(quartile_bad))
	else:
		cutoff = int(len(X)*.7)
		x_train, y_train = X[:cutoff], y[:cutoff]
		x_test,y_test = X[(cutoff+1):], y[(cutoff+1):]
		
		clf = LDA()
		clf.fit(x_train,y_train)

		correct = 0
		incorrect = 0
		total = 0
		quartile_bad = np.empty((0))
		for i,example in enumerate(x_train):
			pred = clf.predict(example)
			if pred == y_train[i]:
				correct +=1
				total+=1
				#print("Match! Percent Correct = {}".format(float(correct)/float(total)))
			else:
				incorrect += 1
				total +=1
				quartile_bad = np.append(quartile_bad,abs(pred-y_train[i]))
				#print("Incorrect :(  Percent Correct = {}".format(float(correct)/float(total)))

		print("Percent Correct = {}".format(float(correct)/float(total)))
		print(quartile_bad)
		print(np.mean(quartile_bad))

	return












if __name__ == "__main__":
	main(sys.argv[1:])





