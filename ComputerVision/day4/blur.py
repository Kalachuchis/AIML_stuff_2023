import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    path = "./images/noisy.png"
    image = cv.imread(path)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    blur1 = cv.blur(image, (15, 15))
    blur2 = cv.GaussianBlur(image, (15, 15), 1)
    blur3 = cv.bilateralFilter(image, 15, 75, 75)

    plt.subplot(2, 3, 1), plt.imshow(image), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 2), plt.imshow(blur1), plt.title('Average Blurred Image')
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 3), plt.imshow(
        blur2), plt.title('Gaussian Blurred Image')
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 5), plt.imshow(
        blur3), plt.title('Bilateral Blurred Image')
    plt.xticks([]), plt.yticks([])

    plt.show()
