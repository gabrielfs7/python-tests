"""

1. Capture camera image
2. Resize image and show
3. Add information for image
3. Detect the face and draw an rectangle around it

IMPORTANT: If camera fail on MacOS, type "sudo killall VDCAssistant" in the terminal

"""

import cv2
from datetime import datetime
from FaceDetector import FaceDetector


video = cv2.VideoCapture(0)

count_frames = 0
last_second = 0
total_frames = 0

detector = FaceDetector()

while True:
    # Get video status and numpay image array
    is_video_running, numpay_frame = video.read()

    # Resize the image
    image_width = numpay_frame.shape[0]
    image_height = numpay_frame.shape[1]

    image_new_width = int(image_width / 1.5)
    image_new_height = int(image_height / 1.5)

    numpay_frame = cv2.resize(numpay_frame, (image_new_height, image_new_width))

    # Calculate video FPS
    now = datetime.now()

    if now.second != last_second:
        total_frames = count_frames
        count_frames = 0

    last_second = now.second
    count_frames = count_frames + 1

    # Write current time and video FPS capture
    fontPositionTopLeftCorner = (20, 50)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.6
    fontColor = (255, 255, 255)
    lineType = 2

    numpay_frame = detector.draw_rectangle_by_array(numpay_frame)

    cv2.putText(
        numpay_frame,
        now.strftime('%Y/%m/%d %H:%M:%S') + ' - ' + str(total_frames) + 'fps',
        fontPositionTopLeftCorner,
        fontFace,
        fontScale,
        fontColor,
        lineType
    )

    cv2.imshow('Capturing from camera', numpay_frame)

    pressed_key = cv2.waitKey(100) # Wait for 100 milliseconds to capture the image

    # Break the loop if q is pressed
    if pressed_key == ord('q'):
        break

video.release()
cv2.destroyWindows()