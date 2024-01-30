import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def simple_thresh():
    path = "./images/dog.jpg"
    img = cv.imread(path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    thresh = 125
    image_copy = np.copy(img_gray)

    # for i in np.ndindex(img_gray.shape):
    #     old_value =img_gray[i]
    #     if old_value < thresh:
    #         new_val = 0
    #     else:
    #         new_val = 255
    #     image_copy[i] = new_val

    image_copy[image_copy < thresh] = 0
    image_copy[image_copy >= thresh] = 255

    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.imshow(image_copy, cmap="gray")
    plt.title("Thresholded Grayscale Image")
    plt.xticks([])
    plt.yticks([])

    plt.show()


def gaussian_kernel():
    # gaussian function
    kernel_size = 3
    sigma = 1

    ax = np.linspace(-(kernel_size - 1) / 2.0,
                     (kernel_size - 1) / 2.0, kernel_size)

    gauss_ax = np.exp(-0.5 * np.square(ax) / np.square(sigma))

    print(gauss_ax)


if __name__ == "__main__":
    pass
