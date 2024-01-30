import numpy as np
import cv2 as cv
from itertools import repeat


def linearly_transform_library(img, operation, scale):
    match operation:
        case "add":
            scaled_image = np.where(img > 255 - scale, 255, img + scale)
            return scaled_image
        case "sub":
            scaled_image = np.where(img < scale, 0, img - scale)
            return scaled_image
        case "div":
            scaled_image = img / scale
            return scaled_image.astype(np.uint8)
        case "mult":
            scaled_image = np.where(img > 255 / scale, 255, img * scale)
            return scaled_image.astype(np.uint8)


def inver_image(img):
    return 255 - img


value = 50
img = cv.imread("./images .jpg")
out = linearly_transform_library(img, "mult", 2)
flip = inver_image(img)
cv.imshow("image1", img)
cv.imshow("out", out)
cv.imshow("flip", flip)
# cv.imshow("image2", np.array(image2))
# cv.imshow("image3", np.array(image3))
# cv.imshow("blue", np.array(blue).astype(np.uint8))
# cv.imshow("green", np.array(green).astype(np.uint8))
# cv.imshow("red", np.array(red).astype(np.uint8))
cv.waitKey(0)

cv.destroyAllWindows()
