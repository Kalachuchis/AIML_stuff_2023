import cv2 as cv
import numpy as np
from itertools import cycle
from matplotlib import pyplot as plt

B_CIRCLE = [
    (0, -3),
    (1, -3),
    (2, -2),
    (3, -1),
    (3, 0),
    (3, 1),
    (2, 2),
    (1, 3),
    (0, 3),
    (-1, 3),
    (-2, 2),
    (-3, 1),
    (-3, 0),
    (-3, -1),
    (-2, -2),
    (-1, -3),

]


def compare_pixel_values(cont_pixels, center_pixel, thresh, n):
    extended = np.array(cont_pixels[:] + cont_pixels[:n])
    light = extended - center_pixel > thresh
    dark = center_pixel - extended > thresh

    for index, i in enumerate(extended[:-n]):
        contigous_light = light[index:index+n]
        contigous_dark = dark[index:index+n]
        if np.all(contigous_light) or np.all(contigous_dark):
            return True


def fast_algo(img, thresh, n):
    radius = 3
    pixels = []
    width, height = img.shape
    keypoints = []

    for (x, y), pixel in np.ndenumerate(img[radius:-radius, radius:-radius]):
        '''
        if x <=3 or y <=3:
            continue
        elif x > width - radius or y > height -radius:
            continue
        '''
        center_x, center_y = x+radius, y+radius
        pixels = [int(img[(center_x) + i, (center_y) + j])
                  for i, j in B_CIRCLE]
        if compare_pixel_values(pixels, img[center_x, center_y], thresh, n):
            keypoints.append((center_x, center_y))
            print([center_x, center_y])

    return [cv.KeyPoint(y, x, 10) for x, y in keypoints]


if __name__ == "__main__":
    sample_array = np.array([
        [10, 20, 30, 40, 50, 60, 70],
        [11, 21, 31, 41, 51, 61, 71],
        [12, 22, 32, 42, 52, 62, 72],
        [13, 23, 33, 43, 53, 63, 73],
        [14, 24, 34, 44, 54, 64, 74],
        [15, 25, 35, 45, 55, 65, 75],
        [16, 26, 36, 46, 56, 66, 76],
    ]
    )
    path = "./box.png"
    img = cv.imread(path, 0)
    thresh = 100
    candidates = 12

    keypoints = fast_algo(img, thresh, candidates)
    print(len(keypoints))

    copy = img.copy()
    copy = cv.drawKeypoints(img, keypoints, copy, color=(0, 255, 0),
                            flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(copy, cmap='gray'), plt.title("Image 1")
    plt.xticks([]), plt.yticks([])

    plt.show()
