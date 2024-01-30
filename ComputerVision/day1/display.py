import numpy as np
import cv2 as cv

# Read image
img = cv.imread('./images .jpg')

# Display the image
cv.imshow("sample image", img)

# Wait for the user to press any key
cv.waitKey(0)

# Close all open windows
cv.destroyAllWindows()
