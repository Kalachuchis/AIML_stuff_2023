import cv2
import numpy as np
from matplotlib import pyplot as plt


def exer_1():
    '''
    Isolate line annd notes using morphological operations
    '''
    img = cv2.imread('./Morphological Transformation/exer_1.png')
    row, column, _ = (img.shape)
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    # dilate horizontally to remove scale
    kernel = np.ones((5, 2), np.uint8)

    notes = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    plt.subplot(1, 3, 2), plt.imshow(notes, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    # dilate vertically to remove notes
    kernel2 = np.ones((1, int(row)), np.uint8)
    partial_lines = cv2.dilate(img, kernel2, iterations=1)

    extend_lines = cv2.erode(partial_lines, kernel2, iterations=3)

    plt.subplot(1, 3, 3), plt.imshow(
        extend_lines, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.imwrite("./output/exer_1_notes.jpg", notes)
    cv2.imwrite("./output/exer_1_lines.jpg", extend_lines)


def exer_2():
    '''
    Obtain the general outline/ shape of the telephone
    '''
    img = cv2.imread('./Morphological Transformation/exer_2.png')
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    # transform image to black and white
    (thresh, bw_img) = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

    plt.subplot(1, 3, 2), plt.imshow(bw_img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    kernel = np.ones((7, 7), np.uint8)
    eroded = cv2.erode(bw_img, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)

    # get morphological gradient to retrieve outline
    gradient = dilated - eroded
    (thresh, outline) = cv2.threshold(gradient, 125, 255, cv2.THRESH_BINARY_INV)
    plt.subplot(1, 3, 3), plt.imshow(
        outline, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.imwrite("./output/exer_2.jpg", outline)


def exer_3():
    '''
    Remove the salt and pepper noise
    '''
    img = cv2.imread('./Morphological Transformation/exer_3.png')
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    kernel = np.ones((3, 3), np.uint8)
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)

    plt.subplot(1, 3, 2), plt.imshow(close, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.imwrite("./output/exer_3.jpg", close)


def exer_4():
    '''
    separate countable coins
    '''

    img = cv2.imread('./Morphological Transformation/exer_4.png')
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    (thresh, bw_img) = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)

    plt.subplot(1, 3, 2), plt.imshow(bw_img, cmap='gray'), plt.title("image 1")
    plt.xticks([]), plt.yticks([])

    # kernel = np.ones((20, 20), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
    erode = cv2.erode(bw_img, kernel, iterations=1)

    plt.subplot(1, 3, 3), plt.imshow(
        erode, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.imwrite("./output/exer_4.jpg", erode)


if __name__ == "__main__":

    exer_1()
