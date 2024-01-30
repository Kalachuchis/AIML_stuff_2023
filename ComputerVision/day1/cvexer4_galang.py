import cv2 as cv
import threading
from multiprocessing import Process
from time import sleep

# Define a video capture object
vid = cv.VideoCapture(0)


def append_to_list(amount, list_of_images, frame, interval):
    if len(list_of_images) <= amount:
        list_of_images.append(frame)

    else:
        list_of_images.pop(0)
        list_of_images.append(frame)
    sleep(interval)


def capture_images(amount, interval):
    list_of_images = []
    frame = []
    # task = Process(
    #     target=append_to_list, args=(amount, list_of_images, frame, interval)
    # )
    while True:

        # Capture the video frame by frame
        ret, frame = vid.read()
        task = threading.Thread(
            target=append_to_list, args=(amount, list_of_images, frame, interval)
        )
        task.daemon = True

        task.start()
        task.join()

        # if not task.is_alive():
        #     task.start()
        #     task.join()

        # Display each frame
        cv.imshow("frame", frame)

        # Terminate capturing when the 'Q' button is pressed
        if (cv.waitKey(1) & 0xFF == ord("q")) | len(list_of_images) >= amount:
            break
    return list_of_images


def average_image(list_of_images):
    average_image = list_of_images[0]
    for i in list_of_images[1:]:
        average_image = cv.addWeighted(i, 0.5, average_image, 0.5, 0)
    return average_image


image_list = capture_images(10, 0.2)

for index, i in enumerate(image_list):
    cv.imwrite(f"images/img_{index}.jpg", i)

blended_image = average_image(image_list)

cv.imwrite("./images/average.jpg", blended_image)


# Release the video capture object
vid.release()

# Destroy all the windows
cv.destroyAllWindows()
