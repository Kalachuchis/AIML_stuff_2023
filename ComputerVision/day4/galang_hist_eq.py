import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def equalize(hist):
    cumulative_hist = []
    sum = 0
    for i in hist:
        sum = sum+i
        pixel_sum = sum
        cumulative_hist.append(pixel_sum)

    cum_hist = np.array(cumulative_hist)
    normalized_list = cum_hist * len(cum_hist) / cum_hist[-1]
    rounded = np.round(normalized_list)
    rounded[rounded > 255] = 255

    return rounded


def equalize_histogram(arr):
    r, g, b = cv.split(arr)

    colors = []
    for i, color in enumerate(["r", "g", "b"]):
        hist = cv.calcHist([arr], [i], None, [256], [0, 256])
        eq_hist = equalize(hist)
        colors.append(eq_hist)

    for i in reversed(range(0, 256)):
        r[r == i] = colors[0][i]
        g[g == i] = colors[1][i]
        b[b == i] = colors[2][i]
    return cv.merge([r, g, b])


if __name__ == "__main__":
    path1 = "images/hist_img1.jpg"
    image1 = cv.imread(path1)
    image1 = cv.cvtColor(image1, cv.COLOR_BGR2RGB)

    equalized = equalize_histogram(image1)

    plt.subplot(1, 3, 1), plt.imshow(image1), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(equalized), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.show()
'''
    plt.subplot(1, 3, 1), plt.imshow(image1), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2)
    for i, color in enumerate(["r", "g", "b"]):
        hist = cv.calcHist([image1], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)

    channels = cv.split(image1)
    eq_channels = []
    for ch in channels:
        eq_ch = cv.equalizeHist(ch)
        eq_channels.append(eq_ch)

    eq_img = cv.merge(eq_channels)
    plt.subplot(1, 3, 3), plt.imshow(eq_img), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.show()
'''
