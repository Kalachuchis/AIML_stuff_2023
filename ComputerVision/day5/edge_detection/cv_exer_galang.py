import cv2
import numpy as np
from matplotlib import pyplot as plt


def exer_1():
    '''
    image 1
    '''
    img = cv2.imread('./edge_exer_1.png')
    row, column, _ = (img.shape)
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title("image 1")
    plt.xticks([]), plt.yticks([])

    _, bw_img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    open = cv2.morphologyEx(bw_img, cv2.MORPH_OPEN, kernel)
    close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)

    plt.subplot(1, 3, 2), plt.imshow(
        open, cmap='gray'), plt.title("image 1")
    plt.xticks([]), plt.yticks([])

    sobel = cv2.Sobel(bw_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3)
    abs_sobel_xy = np.absolute(sobel)
    noble_8u = np.uint8(abs_sobel_xy)

    plt.subplot(1, 3, 2), plt.imshow(
        noble_8u, cmap='gray'), plt.title("sobel")
    plt.xticks([]), plt.yticks([])

    # plt.subplot(2, 3, 4), plt.imshow(img, cmap='gray'), plt.title("image 1")
    # plt.xticks([]), plt.yticks([])

    # close = cv2.dilate(img, kernel, iterations=1)
    # close = cv2.erode(close, kernel, iterations=1)
    close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    canny = cv2.Canny(close, threshold1=110, threshold2=250,
                      apertureSize=3, L2gradient=False)

    plt.subplot(1, 3, 3), plt.imshow(
        canny, cmap='gray'), plt.title("canny")
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.imwrite("./output/exer_1_sobel.png", noble_8u)
    cv2.imwrite("./output/exer_1_canny.png", canny)


def exer_2():
    '''
    obtain the general outline/ shape of the telephone
    '''
    img = cv2.imread('./edge_exer_2.png')
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title("image 1")
    plt.xticks([]), plt.yticks([])

    # transform image to black and white
    (thresh, bw_img) = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((7, 7), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    erode = cv2.erode(bw_img, kernel, iterations=2)

    # get morphological gradient to retrieve outline
    plt.subplot(2, 2, 2), plt.imshow(
        erode, cmap='gray'), plt.title("image 1")
    plt.xticks([]), plt.yticks([])

    sobel = cv2.Sobel(erode, ddepth=cv2.CV_16U, dx=1, dy=1, ksize=7)
    print(sobel)
    abs_sobel_xy = np.absolute(sobel)
    noble_8u = np.uint8(abs_sobel_xy)

    plt.subplot(2, 2, 3), plt.imshow(
        noble_8u, cmap='gray'), plt.title("sobel")
    plt.xticks([]), plt.yticks([])

    canny = cv2.Canny(erode, threshold1=110, threshold2=295,
                      apertureSize=5, L2gradient=False)

    plt.subplot(2, 2, 4), plt.imshow(
        canny, cmap='gray'), plt.title("canny")
    plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.imwrite("./output/exer_2_sobel.png", noble_8u)
    cv2.imwrite("./output/exer_2_canny.png", canny)


def exer_3():
    '''
    remove the salt and pepper noise
    '''
    img = cv2.imread('./edge_exer_3.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title("image 1")
    plt.xticks([]), plt.yticks([])

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    (thresh, bw_img) = cv2.threshold(gray_img, 155, 255, cv2.THRESH_BINARY_INV)

    plt.subplot(2, 2, 2), plt.imshow(
        bw_img, cmap='gray'), plt.title("Black and white image")
    plt.xticks([]), plt.yticks([])

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # erode = cv2.dilate(bw_img, kernel, iterations=1)
    erode = cv2.morphologyEx(bw_img, cv2.MORPH_OPEN, kernel)

    sobel = cv2.Sobel(erode, ddepth=cv2.CV_16U, dx=2, dy=1, ksize=3)
    abs_sobel_xy = np.absolute(sobel)
    noble_8u = np.uint8(abs_sobel_xy)

    plt.subplot(2, 2, 3), plt.imshow(
        noble_8u, cmap='gray'), plt.title("sobel")
    plt.xticks([]), plt.yticks([])

    canny = cv2.Canny(erode, threshold1=190, threshold2=300,
                      apertureSize=5, L2gradient=True)

    plt.subplot(2, 2, 4), plt.imshow(
        canny, cmap='gray'), plt.title("canny")
    plt.xticks([]), plt.yticks([])
    cv2.imwrite("./output/exer_3_sobel.png", noble_8u)
    cv2.imwrite("./output/exer_3_canny.png", canny)

    plt.show()


if __name__ == "__main__":

    exer_3()
