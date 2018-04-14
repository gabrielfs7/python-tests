"""

Resize all images from a given directory

"""
import cv2
import glob2
from ImageResizer import ImageResizer

resizer = ImageResizer()

for image_path in glob2.glob("images/*.jpg"):
    if "-small" in image_path:
        continue

    new_image = resizer.resize(image_path, 100, 100)

    # Display each image for 1 second
    cv2.imshow("New image", new_image)
    cv2.waitKey(1000)

cv2.destroyAllWindows()
