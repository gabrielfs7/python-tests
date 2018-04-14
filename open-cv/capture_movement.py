"""

1. Capture camera image
2. Resize image and show
3. Add information for image
3. Detect the face and draw an rectangle around it

IMPORTANT: If camera fail on MacOS, type "sudo killall VDCAssistant" in the terminal

"""

import cv2

video_capture = cv2.VideoCapture(0)
first_frame = None

while True:

    check, frame = video_capture.read()

    # Make image gray
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Make blur to make easier to detect threshold difference
    gray_frame - cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Necessary to get first image without no movement
    if first_frame is None:
        first_frame = gray_frame

        continue

    # Get absolute difference between images
    delta_frame = cv2.absdiff(first_frame, gray_frame)

    # Make black and white contrast as threshold. Second item returned is the new Numpy array
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    # Find image contours
    (_, contours, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Only consider areas where contours are higher than 1000px and draw a rectangle
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Display images
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Threshold Frame", frame)

    # Break the loop if q is pressed
    if cv2.waitKey(100) == ord('q'):
        break

video_capture.release()
cv2.destroyWindows()