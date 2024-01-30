import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def thresh_trunc(path, thresh):
    img = cv.imread(path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    print(img_gray)

    img_gray[img_gray > thresh] =  thresh
    print(img_gray)

    return img_gray

def thresh_tozero(path, thresh):
    img = cv.imread(path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print(img_gray)
    
    img_gray[img_gray < thresh] =  0
    print(img_gray)

    return img_gray



if __name__ == "__main__":
    path = "./images/watermark.jpg"
    img = cv.imread(path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    image = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    thresh = int(input("Enter threshhold value: " ))
    print("Enter threshhold technique: " )
    print("[1] trunc")
    print("[2] zero")
    technique = input("Choice: " )

    image_copy = thresh_tozero(path, thresh) if int(technique) == 2 else thresh_trunc(path, thresh)
    
    plt.subplot(2,3,1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2,3,3)
    plt.imshow(img_gray, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2,3,5)
    plt.imshow(image_copy, cmap="gray")
    plt.title("Thresholded Grayscale Image")
    plt.xticks([])
    plt.yticks([])

    plt.show()
        
        