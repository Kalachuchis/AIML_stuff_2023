import cv2 as cv


img = cv.imread("./images .jpg")
watermark = cv.imread("./watermark.jpg")


def addWatermarkToImage(img, watermark):
    h_img, w_img, c = img.shape
    half = cv.resize(watermark, (int(w_img / 2), int(h_img / 2)))
    h_wm, w_wm, c_wm = half.shape
    print(watermark.shape)
    print(img.shape)
    print(half.shape)
    # center of image
    center_y = int(h_img / 2)
    center_x = int(w_img / 2)

    # calculate position
    top = center_y - int(h_wm / 2)
    bottom = top + int(h_wm)
    left = center_x - int(w_wm / 2)
    right = left + int(w_wm)

    # get pixels of image where watermark will be placed
    position = img[top:bottom, left:right]
    result = cv.addWeighted(position, 1, half, 0.5, 0)

    img[top:bottom, left:right] = result

    cv.imshow("img", img)

    cv.waitKey(0)

    cv.destroyAllWindows()


addWatermarkToImage(img, watermark)
