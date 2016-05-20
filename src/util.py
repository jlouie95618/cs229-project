import sys
import numpy as np
import math


def parse_Y(Y_f):
	'''
	Input:  Y_f is a text file containing data labels
	Return: numpy array containing data labels

	Parses the Y label txt file into a numpy array
	Use for 'old' dataset
	'''
	Y_arr = np.empty((0))
	Y_file = open(Y_f,'r')
	for line in Y_file:
		data = line.split()
	for label in data:
		Y_arr = np.append(Y_arr,int(label))
	return Y_arr


def process_X(X):
	'''
	Input:  X is a numpy feature array
	Return: trimmed numpy feature array

	Gets rid of the first two features (hrr_id and size).
	Use only for 'old' dataset
	'''
	X_new = np.delete(X,0,1)
	X_new = np.delete(X_new,0,1)
	return X_new 



def fill_mean(features):
	'''
	Input: features is a 2-D numpy feature array
	Return: 2-D numpy array with '-1' replaced with feature means

	Replaces the '-1' values with the mean of feature
	Allows us to fill in missing data
	'''
	averages = np.empty((0))
	for i,feature in enumerate(features.T):
		observed = np.asarray([f for f in feature if f!=-1])
		if(len(observed)==0):
			averages = np.append(averages,0)
			continue
		mean = np.mean(observed)
		averages = np.append(averages,mean)

	
	for j,feature in enumerate(features):
		for k,f in enumerate(feature):
			if f==-1:
				feature[k] = averages[k]

	#np.savetxt('temp.csv',features,fmt='%f',delimiter=',')
	return features







