import cv2 as cv
import numpy as np

img = cv.imread("./watermark.jpg")


def scaling(img, scale):
    cv.imshow("img", img)
    height, width, c = img.shape
    matrix = np.float32([[scale, 0, 0], [0, scale, 0]])
    transformed = cv.warpAffine(img, matrix, (width * scale, height * scale))

    cv.imshow("transformed", transformed)


def rotation(img, angle):
    cv.imshow("img", img)
    height, width, c = img.shape
    cos = np.cos(np.radians(angle))
    sin = np.sin(np.radians(angle))
    # center_x =
    new_width = height * sin + width * cos
    new_height = height * cos + width * sin
    translate_matrix = np.float32(
        [[1, 0, (new_width - width) / 2], [0, 1, (new_height - height) / 2]]
    )
    transformed = cv.warpAffine(
        img, translate_matrix, (int(new_width), int(new_height))
    )
    t_h, t_w, t_c = transformed.shape
    print(new_width, new_height)
    print(transformed.shape)

    rotate = cv.getRotationMatrix2D((int(t_w / 2), int(t_h / 2)), angle, 1)
    transformed = cv.warpAffine(transformed, rotate, (t_w, t_h))

    cv.imshow("transformed", transformed)


def reflection(img, angle):
    cv.imshow("img", img)
    height, width, c = img.shape
    sin = np.sin(np.radians(angle))
    print(angle)
    matrix = 0
    if 180 == angle or angle == 0:
        matrix = np.float32([[1, 0, 0], [0, -1, height]])
    if 90 == angle:
        matrix = np.float32([[-1, 0, width], [0, 1, 0]])
    else:
        origin = [width / 2, height / 2]
        x_point = 1 / np.cos(np.radians(angle))
        y_point = 1 / np.sin(np.radians(angle))
        print(x_point)
        print(y_point)
        original = np.float32([origin, [x_point, 0], [0, y_point]])
        reflected = np.float32([origin, [0, y_point], [x_point, 0]])
        matrix = cv.getAffineTransform(original, reflected)

        # matrix = np.float32([[y_point, 0, width], [x_point, 0, 0]])

    transformed = cv.warpAffine(img, matrix, (width * 2, height * 2))

    cv.imshow("transformed", transformed)


def translate(img, point):
    cv.imshow("img", img)
    height, width, c = img.shape
    matrix = np.float32([[1, 0, point[0]], [0, 1, point[1]]])
    transformed = cv.warpAffine(img, matrix, (width, height))
    cv.imshow("transformed", transformed)


def shear(img, parameter):
    cv.imshow("img", img)
    height, width, c = img.shape
    factor = np.tan(np.radians(parameter))
    a = np.sin(np.radians(parameter))
    b = np.cos(np.radians(parameter))
    matrix = np.float32([[1, 0, 0], [factor, 1, 0]])
    transformed = cv.warpAffine(img, matrix, (width * 2, height * 2))
    t_h, t_w, t_c = transformed.shape

    rotate_matrix = cv.getRotationMatrix2D((0, 0), parameter, 1)

    fixed_transformed = cv.warpAffine(transformed, rotate_matrix, (t_w, height))

    cv.imshow("transformed", transformed)
    cv.imshow("fixed_transformed", fixed_transformed)


def applyAffineTransformation(image, transfromation, parameter):
    match transfromation:
        case "scaling":
            scaling(image, parameter)
        case "rotate":
            rotation(image, parameter)
        case "reflect":
            reflection(image, parameter)
        case "translate":
            translate(image, parameter)
        case "shear":
            shear(image, parameter)
    cv.waitKey(0)
    cv.destroyAllWindows()


applyAffineTransformation(img, "shear", 60)
