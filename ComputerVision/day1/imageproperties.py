import numpy as np
import cv2 as cv

# Read image
img = cv.imread("./images .jpg")

# Print pixel values
print("Pixel Values: \n", img)

# Print shape
print("Image Shape: ", img.shape)
