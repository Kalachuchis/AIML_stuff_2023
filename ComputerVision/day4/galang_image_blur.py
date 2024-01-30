import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def reflect_array(array, kernel):
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

    right = new_array[:, -2:-pad-1:-1]
    left = new_array[:, pad - 1:0:-1]

    return np.concatenate([left, new_array, left], axis=1)

    # for i in new_array:
    #     arr = np.pad(i, (pad, pad), 'symmetric')
    #     arr = np.delete(arr, [pad, -pad])
    #     final_array.append(arr)

    # return np.array(final_array)


def median_blur(arr, k):
    padded_array = reflect_array(arr, k)

    arr_copy = arr.copy()

    for (x, y), pixel in np.ndenumerate(arr):
        sub_arr = padded_array[x:x+k, y:y+k]
        sub_arr_mean = np.mean(sub_arr)
        arr_copy[x, y] = math.floor(sub_arr_mean)

    return (arr_copy)


if __name__ == '__main__':
    sample_array = np.array([
        [10, 20, 30, 40, 50],
        [11, 21, 31, 41, 51],
        [12, 22, 32, 42, 52],
        [13, 23, 33, 43, 53],
        [14, 24, 34, 44, 54]
    ]
    )
    path = "./images/noisy.png"

    img = cv.imread(path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    blur = median_blur(gray, 15)

    plt.subplot(2, 3, 1), plt.imshow(
        img), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 2), plt.imshow(
        blur, cmap='gray'), plt.title('Average Blurred Image')
    plt.xticks([]), plt.yticks([])

    plt.show()
