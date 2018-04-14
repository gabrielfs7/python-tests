"""

1. Detect faces in images using opencv
2. Draw rectangles on the found faces
3. Show image with the rectangles

"""

import cv2


class FaceDetector:
    def __init__(self):
        self.__face_cascade = cv2.CascadeClassifier('faces/haarcascade_frontalface_default.xml');

    def get_face_coordinates(self, image):
        """
        Return Numpy array with coordinates for faces:
            x_coordinate,
            y_coordinate,
            face_width,
            face_height

        :param image:
        :return:
        """

        # Convert RGB to gray color
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return self.__face_cascade.detectMultiScale(
            gray_image,
            scaleFactor=1.05,  # Decreases the "face search" in 5 percent every time
            minNeighbors=5  # Number of neighbors to find around image
        )

    def draw_rectangle_by_array(self, image_array):
        """
        Draw a rectangle in an image when detect a face.

        :param npyarray image_array:
        :return:
        """

        faces = self.get_face_coordinates(image_array)

        # Draw the rectangles
        for x_coordinate, y_coordinate, face_width, face_height in faces:
            rectangle_bgr_color = (0, 255, 0)
            rectangle_width = 3

            image_array = cv2.rectangle(
                image_array,
                (x_coordinate, y_coordinate),
                (
                    x_coordinate + face_width,
                    y_coordinate + face_height
                ),
                rectangle_bgr_color,
                rectangle_width
            )

        return image_array

    def draw_rectangle_on_face(self, image_path):
        """
        Draw a rectangle in an image when detect a face.

        :param string image_path:
        :return:
        """
        # Load original image
        image_array = cv2.imread(image_path)

        return self.draw_rectangle_by_array(image_array)
