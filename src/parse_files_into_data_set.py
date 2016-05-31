import sys
import numpy as np

# np.set_printoptions(threshold=np.nan)

# Order of files being read:
# X:
# 1 Structural Measures DONE!!! 
# 2 Timely and Effective Care DONE!!!
# 3 Payment and Value of Care SKIP!!!
# 4 Complications DONE!!!
# 5 Healthcare Associated Infections DONE!!!
# 6 Outpatient Imaging Efficiency DONE!!!
# 7 Readmission and Deaths DONE!!!
# 8 HCAPHS SKIP!!!
# 9 READMISSION REDUCTION DONE!!!

# CATEGORICAL VARIABLES TO ACCOMODATE:
# ALL "Not avaialble" should be converted to the EMPTY STRING
#   - To be filled in with clustering later
# Measure Response
#   - "Does not have ..." should be converted to 0
#   - "No" or "N" should be converted to 0
#   - "Yes" or "Y" should be converted to 1
# EDV in Timely and Effective Care
#   - "Very High" --> 70000
#   - "High" --> 50000
#   - "Medium" --> 30000
#   - "Low" --> 10000


# Training Example Labels: 
# Hospital General Information.csv

# y:
# Medicare Hospital Spending Per Patient.csv

# Output: 
# Three files: training_set.csv, labels.csv, hospital_ids.csv

path_to_files = '../data/2015_data/'

def read_data_file(filename, rows_skip, cols, dataset_map=None, measure_ids=None):
    if dataset_map == None:
        return np.genfromtxt(filename, dtype=str, usecols=cols,
            skip_header=rows_skip, delimiter='","')
    else:
        X = np.genfromtxt(filename, dtype=str, usecols=cols,
            skip_header=rows_skip, delimiter='","')
        for line in X:
            measure_ids.add(line[1])
            if line[0].strip('"') in dataset_map:
                dataset_map[line[0].strip('"')][line[1]] = line[2]
            else:
                dataset_map[line[0].strip('"')] = {}

def initialize_map(ids):
    data = {}
    for id_val in ids:
        data[id_val] = {}
    return data

def assemble_matrix(dataset_map, e_ids, m_ids):
    X = np.empty(shape=(len(e_ids), len(m_ids)), dtype=object)
    for i, e_id in enumerate(e_ids):
        for j, m_id in enumerate(m_ids):
            hospital = dataset_map[e_id]
            if m_id in hospital:
                val = hospital[m_id]
                if m_id == 'EDV':
                    if 'Very High' in val: # Very High
                        val = '70000'
                    elif 'High' in val: # High
                        val = '50000'
                    elif 'Medium' in val: # Medium
                        val = '30000'
                    elif 'Low' in val: # Low
                        val = '10000'
                elif m_id == 'OP_12' or \
                    m_id == 'OP_17' or \
                    m_id == 'OP_25':
                    if val == "Yes":
                        val = '1'
                    else:
                        val = '0'
                elif m_id == 'SM_PART_CARD' or \
                    m_id == 'SM_PART_GEN_SURG' or \
                    m_id == 'SM_PART_NURSE' or \
                    m_id == 'SM_SS_CHECK' or \
                    m_id == 'ACS_REGISTRY' or \
                    m_id == 'SM_PART_STROKE':
                    if val == 'Y':
                        val = '1'
                    else:
                        val = '0'
                if val == '-':
                    val = '-1'
                if 'Not Available' in val:
                    val = '-1'
            else:
                val = '-1'
            X[i, j] = val
    return X

def main(args):
    print args
    if len(args) < 1: return
    if len(args) >= 2: 
        if '2015' in args[1]: 
            path_to_files = '../data/2015_data/'
        if '2014' in args[1]: 
            path_to_files = '../data/2014_data/'
    threshold = float(args[0])
    y_labels = read_data_file(path_to_files + 'Medicare Hospital Spending per Patient - Hospital.csv', 1, (0, 10))
    y_labels = y_labels[y_labels[:,0].argsort()]
    y_labels = y_labels[y_labels[:, 1] != 'Not Available']
    training_example_ids = y_labels[:, 0]
    for i, val in enumerate(training_example_ids):
        training_example_ids[i] = val.strip('"')
    y_labels = y_labels[:, 1]
    print len(y_labels)
    measure_ids = set()
    dataset_map = initialize_map(training_example_ids)
    print y_labels
    print training_example_ids
    
    
    read_data_file(path_to_files + 'Structural Measures - Hospital.csv', 1, (0, 9, 10), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Timely and Effective Care - Hospital.csv', 1, (0, 9, 11), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Healthcare Associated Infections - Hospital.csv', 1, (0, 9, 11), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Outpatient Imaging Efficiency - Hospital.csv', 1, (0, 8, 10), dataset_map, measure_ids)
    read_data_file(path_to_files + 'READMISSION REDUCTION.csv', 1, (1, 3, 6), dataset_map, measure_ids)
    if '2014' in path_to_files:
        read_data_file(path_to_files + 'Readmissions Complications and Deaths - Hospital.csv', 1, (0, 9, 12), dataset_map, measure_ids)
    elif '2015' in path_to_files:
        read_data_file(path_to_files + 'Complications - Hospital.csv', 1, (0, 9, 12), dataset_map, measure_ids)
        read_data_file(path_to_files + 'Readmissions and Deaths - Hospital.csv', 1, (0, 9, 12), dataset_map, measure_ids)

    if len(args) == 3 and 'combined' in args[2]: 
        measure_ids_2014 = set(read_data_file('./2014/feature_labels_2014.csv', 0, (0,)))
        measure_ids_2015 = set(read_data_file('./2015/feature_labels_2015.csv', 0, (0,)))
        measure_ids = measure_ids_2015.union(measure_ids_2014)
    measure_ids = sorted(list(measure_ids))
    print measure_ids
    print len(measure_ids)
    X = assemble_matrix(dataset_map, training_example_ids, measure_ids)
    print X

    rows_to_delete = []
    for i in xrange(0, len(X)):
        neg_one_count = 0
        for j in xrange(0, len(X[0])):
            if X[i, j] == '-1': neg_one_count += 1
        if (float(neg_one_count) / float(len(measure_ids))) > threshold:
            rows_to_delete.append(i)
    print 'before: %d' % len(y_labels)
    print rows_to_delete
    X = np.delete(X, rows_to_delete, 0)
    y_labels = np.delete(y_labels, rows_to_delete, 0)
    training_example_ids = np.delete(training_example_ids, rows_to_delete, 0)
    print 'after: %d' % len(y_labels)
    # save all data to the appropriate files
    tag = ''
    if len(args) >= 2: tag = str(args[1])
    np.savetxt('training_set' + tag + '.txt', X, fmt='%s', delimiter=';')
    np.savetxt('feature_labels' + tag + '.txt', measure_ids, fmt='%s', delimiter=';')
    np.savetxt('hospital_ids' + tag + '.txt', training_example_ids, fmt='%s', delimiter=';')
    np.savetxt('labels' + tag + '.txt', y_labels, fmt='%s', delimiter=';')

    np.savetxt('training_set' + tag + '.csv', X, fmt='%s', delimiter=',')
    np.savetxt('feature_labels' + tag + '.csv', measure_ids, fmt='%s', delimiter=',')
    np.savetxt('hospital_ids' + tag + '.csv', training_example_ids, fmt='%s', delimiter=',')
    np.savetxt('labels' + tag + '.csv', y_labels, fmt='%s', delimiter=',')

if __name__ == '__main__':
    main(sys.argv[1:])