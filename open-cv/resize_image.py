"""

The main goal is to teach how to resize images

"""
import cv2
from ImageResizer import ImageResizer

with_color = 1

resizer = ImageResizer()

new_image_path = resizer.resize('images/galaxy.jpg', 100, 100)

# Show image before resize
cv2.imshow('Galaxy', new_image_path)

# Close window when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()