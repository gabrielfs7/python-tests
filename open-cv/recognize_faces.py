"""

1. Detect faces in images using opencv
2. Draw rectangles on the found faces
3. Show image with the rectangles

"""

import cv2
from FaceDetector import FaceDetector

# Display images
detector = FaceDetector()
image = detector.draw_rectangle_on_face('faces/face.jpg')

cv2.imshow('Gray image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()