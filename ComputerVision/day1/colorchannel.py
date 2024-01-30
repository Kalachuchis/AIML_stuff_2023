import numpy as np
import cv2 as cv
from itertools import repeat

# Read image
img = cv.imread("./images .jpg")

# Split the color channels of the image
b, g, r = cv.split(img)


print(b.shape[1])
print(g.shape)
print(r.shape)
# zeros = np.zeros(b.shape,dtype=np.uint)
image = []
image2 = []
image3 = []
blue = []
green = []
red = []
for index, i in enumerate(b):
    zeros = [0] * len(b[index])
    print(zeros)
    pixel = [list(x) for x in zip(b[index], g[index], r[index])]
    pixel1 = [list(x) for x in zip(g[index], r[index], b[index])]
    pixel2 = [list(x) for x in zip(r[index], b[index], g[index])]
    bluep = [list(x) for x in zip(b[index], zeros, zeros)]
    greenp = [list(x) for x in zip(zeros, g[index], zeros)]
    redp = [list(x) for x in zip(zeros, zeros, r[index])]
    image.append(pixel)
    image2.append(pixel1)
    image3.append(pixel2)
    blue.append(bluep)
    green.append(greenp)
    red.append(redp)

cv.imshow("image", np.array(image))
cv.imshow("image2", np.array(image2))
cv.imshow("image3", np.array(image3))
cv.imshow("blue", np.array(blue).astype(np.uint8))
cv.imshow("green", np.array(green).astype(np.uint8))
cv.imshow("red", np.array(red).astype(np.uint8))
cv.waitKey(0)

cv.destroyAllWindows()
