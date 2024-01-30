import numpy as np


def filter_by_stdev(data, threshold):
    mean = np.mean(data)
    stdev = np.std(data)
    filtered = data[abs(data) <= (mean + threshold * stdev)]
    return filtered


def filter_by_zscore(data, threshold):
    mean = np.mean(data)
    stdev = np.std(data)
    filtered = data[abs((data - mean) / stdev) <= threshold]
    return filtered
