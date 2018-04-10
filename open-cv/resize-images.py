"""

Resize all images from a given directory

"""
import cv2
import glob2


def open_image_and_resize(path, new_image_height, new_image_with):
    with_color = 1

    image = cv2.imread(path, with_color)

    return cv2.resize(image, (new_image_height, new_image_with))


for image_path in glob2.glob("sample-images/*.jpg"):
    if "-small" in image_path:
        continue

    new_image_path = image_path.replace('.jpg', '-small.jpg')

    new_image = open_image_and_resize(image_path, 100, 100)

    cv2.imwrite(new_image_path, new_image)

    cv2.imshow("New image " + new_image_path, new_image)

    cv2.waitKey(1000)

cv2.destroyAllWindows()
