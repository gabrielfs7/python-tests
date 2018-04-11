import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

# Load original image
image = cv2.imread("face.jpg") # You can replace to news.jpg

# Convert RGB to gray collor
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Numpy array with x_coordinate, y_coordinate, face_width, face_height for faces:
faces = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.05, # Decreases the "face search" in 5 percent every time
    minNeighbors=5 # Number of neighbors to find around image
)

for x_coordinate, y_coordinate, face_width, face_height in faces:
    rectangle_bgr_color = (0, 255, 0)
    rectangle_width = 3

    image = cv2.rectangle(
        image,
        (x_coordinate, y_coordinate),
        (
            x_coordinate + face_width,
            y_coordinate + face_height
        ),
        rectangle_bgr_color,
        rectangle_width
    )


# Display images
cv2.imshow('Gray image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()