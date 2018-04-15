"""

1. Capture camera image
2. Resize image and show
3. Add information for image
3. Detect the face and draw an rectangle around it

IMPORTANT: If camera fail on MacOS, type "sudo killall VDCAssistant" in the terminal

"""

import cv2
from VideoCapture import VideoCapture

video_capture = VideoCapture()

while True:
    video_capture.read()

    cv2.imshow('Capturing from camera', video_capture.get_numpay_frame())

    # Wait for 100 milliseconds to capture the image
    pressed_key = cv2.waitKey(100)

    # Break the loop if q is pressed
    if pressed_key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()