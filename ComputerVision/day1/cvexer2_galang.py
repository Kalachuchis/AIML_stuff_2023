import numpy as np
import cv2 as cv

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
    pixel = [list(x) for x in zip(b[index], g[index], r[index])]
    pixel1 = [list(x) for x in zip(g[index], r[index], b[index])]
    pixel2 = [list(x) for x in zip(r[index], b[index], g[index])]
    bluep = [list(x) for x in zip(b[index], zeros, zeros)]
    greenp = [list(x) for x in zip(zeros, g[index], zeros)]
    redp = [list(x) for x in zip(zeros, zeros, r[index])]
    pixel1.extend(pixel)
    pixel1.extend(pixel2)
    pixel1.extend(bluep)
    pixel1.extend(redp)
    pixel1.extend(greenp)
    image.append(pixel1)

cv.imshow("image", np.array(image).astype(np.uint8))
# cv.imshow("image2", np.array(image2))
# cv.imshow("image3", np.array(image3))
# cv.imshow("blue", np.array(blue).astype(np.uint8))
# cv.imshow("green", np.array(green).astype(np.uint8))
# cv.imshow("red", np.array(red).astype(np.uint8))
cv.waitKey(0)

cv.destroyAllWindows()
