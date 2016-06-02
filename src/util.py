import sys
import numpy as np
import math
from scipy.stats import pearsonr
from copy import deepcopy
from sklearn.feature_selection import VarianceThreshold


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
    #X_new = np.delete(X_new,0,1)
    return X_new 



def fill_mean(features, sentinel_val):
    '''
    Input: features is a 2-D numpy feature array
    Return: 2-D numpy array with sentinel_val replaced with feature means

    Replaces the sentinel_val values with the mean of feature
    Allows us to fill in missing data
    '''
    averages = np.empty((0))
    for i,feature in enumerate(features.T):
        observed = np.asarray([f for f in feature if f!=sentinel_val])
        if(len(observed)==0):
            averages = np.append(averages,0)
            continue
        mean = np.mean(observed)
        averages = np.append(averages,mean)

    
    for j,feature in enumerate(features):
        for k,f in enumerate(feature):
            if f==sentinel_val:
                feature[k] = averages[k]

    #np.savetxt('temp.csv',features,fmt='%f',delimiter=',')
    return features


def __form_pearsonr_array(arr, sentinel_val):
    # keep track of all the entries with measured values
    observed = np.asarray([x for x in arr if x!=sentinel_val])
    mean = np.mean(observed)
    # zero out all the -1 entries (i.e. remove sentinel value)
    arr = arr - mean
    # assume that sentinel_val is a numeric value
    arr[arr == (-1 * mean + sentinel_val)] = 0
    return arr



def __indicies_to_fill(arr):
    result = []
    for i in xrange(len(arr)): 
        if arr[i] == -1: result.append(i)
    return result 



def item_item_collab_filtering(examples, num_nearest_neighbors, sentinel_val, name='iicf_output.csv'):
    examples_copy = deepcopy(examples)
    nearest_neighbors = []
    total = len(examples)
    for i, target in enumerate(examples):
        if i % 100 == 0:
            print "on %i of %i... only %f percent of the way through" % (i, total, (float(i) / total) * 100)
        x = __form_pearsonr_array(target, sentinel_val)
        for j, potential_neighbor in enumerate(examples):
            if i == j: continue
            y = __form_pearsonr_array(potential_neighbor, sentinel_val)
            (coefficient, p_val) = pearsonr(x, y)
            nearest_neighbors.append((coefficient, potential_neighbor, j))
        nearest_neighbors = sorted(nearest_neighbors, key=lambda tup: tup[0])
        nearest_neighbors.reverse()
        nearest_neighbors = nearest_neighbors[:num_nearest_neighbors]
        to_fill = __indicies_to_fill(target)
        for index in to_fill:
            numerator, denominator = 0.0, 0.0
            for nearest_neighbor in nearest_neighbors:
                val = nearest_neighbor[1][index] if nearest_neighbor[1][index] != -1 else 0.0
                numerator += nearest_neighbor[0] * val
                denominator += nearest_neighbor[0]
            examples_copy[i, index] = float(numerator) / float(denominator)
    np.savetxt(name, examples_copy, fmt='%s', delimiter=',')
    return examples_copy



def variance_threshold(X, threshold_val=None):
    sel = VarianceThreshold()
    if threshold_val != None: 
        sel = VarianceThreshold(threshold_val)
    return sel.fit_transform(X)


def fill_mean2(features):
    '''
    Input: features is a 2-D numpy feature array
    Return: 2-D numpy array with sentinel_val replaced with feature means

    Replaces the sentinel_val values with the mean of feature
    Allows us to fill in missing data
    '''
    averages = np.empty((0))
    for i,feature in enumerate(features.T):
        observed = np.asarray([f for f in feature if np.isnan(f)==False])
        if(len(observed)==0):
            averages = np.append(averages,0)
            continue
        mean = np.mean(observed)
        averages = np.append(averages,mean)

    
    for j,feature in enumerate(features):
        for k,f in enumerate(feature):
            if np.isnan(f):
                feature[k] = averages[k]

    #np.savetxt('temp.csv',features,fmt='%f',delimiter=',')
    #print(features)
    return features






