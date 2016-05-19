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
# 9 READMISSION REDUCTION

# Training Example Labels: 
# Hospital General Information.csv

# y:
# Medicare Hospital Spending Per Patient.csv

# Output: 
# Three files: training_set.csv, labels.csv, hospital_ids.csv

path_to_files = '../data/'

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
                if val == 'Not Available':
                    val = ''
            else:
                val = ''
            X[i, j] = val
    return X

def main(args):
    print args
    training_example_ids = read_data_file(path_to_files + 'Hospital General Information.csv', 1, (0, 1))
    training_example_ids = training_example_ids[:, 0]
    for i, val in enumerate(training_example_ids):
        training_example_ids[i] = val.strip('"')
    print len(training_example_ids)
    measure_ids = set()
    dataset_map = initialize_map(training_example_ids)
    print training_example_ids
    
    read_data_file(path_to_files + 'Complications - Hospital.csv', 1, (0, 9, 12), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Structural Measures - Hospital.csv', 1, (0, 9, 10), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Timely and Effective Care - Hospital.csv', 1, (0, 9, 11), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Healthcare Associated Infections - Hospital.csv', 1, (0, 9, 11), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Outpatient Imaging Efficiency - Hospital.csv', 1, (0, 8, 10), dataset_map, measure_ids)
    read_data_file(path_to_files + 'Readmissions and Deaths - Hospital.csv', 1, (0, 9, 12), dataset_map, measure_ids)
    read_data_file(path_to_files + 'READMISSION REDUCTION.csv', 1, (1, 3, 6), dataset_map, measure_ids)

    measure_ids = sorted(list(measure_ids))
    print measure_ids
    print len(measure_ids)
    X = assemble_matrix(dataset_map, training_example_ids, measure_ids)
    print X
    # save all data to the appropriate files
    np.savetxt('training_set.txt', X, fmt='%s', delimiter=';')
    np.savetxt('feature_labels.txt', measure_ids, fmt='%s', delimiter=';')
    np.savetxt('hospital_ids.txt', training_example_ids, fmt='%s', delimiter=';')

if __name__ == '__main__':
    main(sys.argv[1:])