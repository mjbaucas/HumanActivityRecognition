from numpy import mean, std, dstack, array, vstack
from pandas import read_csv, DataFrame

from tensorflow.keras.utils import to_categorical

def load_file(filepath):
    dataframe = read_csv(filepath, header=None, delim_whitespace=True)
    return dataframe.values

def load_group(filenames, prefix=''):
    loaded = list()
    for name in filenames:
        data = load_file(prefix + name)
        loaded.append(data)
    loaded = dstack(loaded)
    return loaded

def load_dataset_group(group, prefix=''):
    filepath = prefix + group + '/Inertial Signals/'
    filenames = list()
    filenames += ['total_acc_x_' + group + '.txt', 'total_acc_y_' + group + '.txt', 'total_acc_z_' + group + '.txt']
    filenames += ['body_acc_x_' + group + '.txt', 'body_acc_y_' + group + '.txt', 'body_acc_z_' + group + '.txt']
    filenames += ['body_gyro_x_' + group + '.txt', 'body_gyro_y_' + group + '.txt', 'body_gyro_z_' + group + '.txt']
    X = load_group(filenames, filepath)
    Y = load_file(prefix + group + '/y_' + group + '.txt')
    return X, Y 

def load_dataset(prefix=''):
    trainX, trainY = load_dataset_group('train', prefix + 'UCI HAR Dataset/')
    testX, testY = load_dataset_group('test', prefix + 'UCI HAR Dataset/')
    trainY = trainY - 1
    testY = testY - 1
    print(trainX.shape, trainY.shape, testX.shape, testY.shape)
    return trainX, trainY, testX, testY

def class_breakdown(data):
    df = DataFrame(data)
    counts = df.groupby(0).size()
    counts = counts.values

    for i in range(len(counts)):
        percent = counts[i] / len(df) * 100
        print('Class=%d, total=%d, percentage=%.3f' % (i, counts[i], percent))
