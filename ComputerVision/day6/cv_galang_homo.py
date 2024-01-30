import numpy as np
import cv2
from matplotlib import pyplot as plt
import math


def deskew(M, skewed_image, orig_image):
    im_out = cv2.warpPerspective(skewed_image, np.linalg.inv(
        M), (orig_image.shape[1], orig_image.shape[0]))

    return im_out


if __name__ == "__main__":
    orig_image = cv2.imread("./id.jpg", 0)
    skewed_image = cv2.imread('./idskew.jpg')

    # Initiate SIFT detector
    sift = cv2.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(orig_image, None)
    kp2, des2 = sift.detectAndCompute(skewed_image, None)

    print(des1)
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    MIN_MATCH_COUNT = 10
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good
                              ]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good
                              ]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        print(mask)
        matchesMask = mask.ravel().tolist()

        draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                           singlePointColor=None,
                           matchesMask=matchesMask,  # draw only inliers
                           flags=2)
        img3 = cv2.drawMatches(orig_image, kp1, skewed_image,
                               kp2, good, None, **draw_params)

        deskewed = deskew(M, skewed_image, orig_image)

        plt.subplot(2, 2, 1), plt.imshow(
            img3, cmap='gray'), plt.title("deskewed")
        plt.xticks([]), plt.yticks([])

        plt.subplot(2, 2, 3), plt.imshow(
            skewed_image, cmap='gray'), plt.title("deskewed")
        plt.xticks([]), plt.yticks([])

        plt.subplot(2, 2, 4), plt.imshow(
            deskewed, cmap='gray'), plt.title("deskewed")
        plt.xticks([]), plt.yticks([])
        plt.show()

    else:
        print("Not  enough  matches are found   -   %d/%d" %
              (len(good), MIN_MATCH_COUNT))
        matchesMask = None
