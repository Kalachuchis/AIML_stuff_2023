import cv2 as cv
import math
import numpy as np
from typing import List


def gaussian_kernel(kernel):
    # gaussian function
    kernel_size = kernel
    sigma = 1

    ax = np.linspace(-(kernel_size - 1) / 2.0,
                     (kernel_size - 1) / 2.0, kernel_size)

    gauss_ax = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss_ax, gauss_ax)
    kernel = kernel / np.sum(kernel)

    return kernel


def reflect_array(array: List, kernel):
    pad = math.ceil(kernel/2)
    final_array = []
    padded_array = []

    top = (array[pad - 1:0:-1])
    bot = (array[-2:-pad-1:-1])

    new_array = np.append(top, array[:], axis=0)
    new_array = np.append(new_array, bot, axis=0)

    # for i in reversed(array[1:pad]):
    #     padded_array.append(i)

    # padded_array.extend(array)

    # for i in reversed(array[-pad:-1]):
    #     padded_array.append(i)

    for i in new_array:
        arr = np.pad(i, (pad, pad), 'symmetric')
        arr = np.delete(arr, [pad, -pad])
        final_array.append(arr)

    return np.array(final_array)


def gaussian_blur(padded_array, gaussian_filter, kernel_size):
    rows, columns = (padded_array.shape)
    filtered_list = []

    for row in range(0, rows-(kernel_size-1)):
        new_row = []
        for column in range(0, columns-(kernel_size-1)):
            kernel = padded_array[row: row+kernel_size,
                                  column: column+kernel_size]

            filtered_kernel = kernel * gaussian_filter

            new_value = np.sum(filtered_kernel)
            new_row.append(new_value)
        filtered_list.append(new_row)

    return (np.array(filtered_list))


if __name__ == "__main__":
    sample_array = np.array([
        [10, 20, 30, 40, 50],
        [11, 21, 31, 41, 51],
        [12, 22, 32, 42, 52],
        [13, 23, 33, 43, 53],
        [14, 24, 34, 44, 54]
    ]
    )
    copy = sample_array.copy()
    kernel_size = 3

    padded_array = reflect_array(sample_array, kernel_size)
    filter = gaussian_kernel(kernel_size)
    filtered_array = gaussian_blur(padded_array, filter, kernel_size)
    copy[filtered_array >= sample_array] = 255
    copy[filtered_array < sample_array] = 0

    print("ORIGINAL ARRAY")
    print(sample_array)
    print("PADDED ARRAY")
    print(padded_array)
    print("FILTERED WITH GAUSSIAN KERNEL")
    print(filtered_array)
    print("THRESH")
    print(copy)
