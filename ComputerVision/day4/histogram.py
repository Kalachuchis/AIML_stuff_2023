import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def something():
    path1 = "./images/hist_img1.jpg"
    path2 = "./images/hist_img2.jpg"

    image1 = cv.imread(path1)
    image1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
    image2 = cv.imread(path2)
    image2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)

    hist1 = cv.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv.calcHist([image2], [0], None, [256], [0, 256])

    plt.subplot(1, 4, 1), plt.imshow(image1, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 4, 2), plt.plot(
        hist1, color='k'), plt.title('Image 1 Histogram')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.subplot(1, 4, 3), plt.imshow(image2, cmap='gray'), plt.title("Image 2")
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 4, 4), plt.plot(
        hist2, color='k'), plt.title('Image 2 Histogram')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.show()


def something_else():
    path1 = "./images/hist_img1.jpg"

    image1 = cv.imread(path1)
    image1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)

    eq_img = cv.equalizeHist(image1)

    hist1 = cv.calcHist([image1], [0], None, [256], [0, 256])
    eq_img_hist = cv.calcHist([eq_img], [0], None, [256], [0, 256])

    plt.subplot(1, 4, 1), plt.imshow(image1, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 4, 2), plt.plot(
        hist1, color='k'), plt.title('Image 1 Histogram')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.subplot(1, 4, 3), plt.imshow(eq_img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 4, 4), plt.plot(
        eq_img_hist, color='k'), plt.title('Image 1 Histogram')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.show()


if __name__ == "__main__":
    path1 = "images/hist_img3.jpg"
    image1 = cv.imread(path1)
    image1 = cv.cvtColor(image1, cv.COLOR_BGR2RGB)

    plt.subplot(1, 3, 1), plt.imshow(image1, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2)
    for i, color in enumerate(["r", "g", "b"]):
        hist = cv.calcHist([image1], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)

    channels = cv.split(image1)
    eq_channels = []

    plt.show()
