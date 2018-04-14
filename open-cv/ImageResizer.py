"""

The main goal is to teach how to resize images

"""
import cv2


class ImageResizer:
    def resize(self, image_path, new_image_width, new_image_height):
        with_color = 1

        # This is a numpay array containing the pixel matrix for the image
        image = cv2.imread(image_path, with_color)

        new_image = cv2.resize(image, (new_image_height, new_image_width))

        if "-small" in image_path:
            return image_path

        new_image_path = image_path.replace('.jpg', '-small.jpg')

        # Save new image
        cv2.imwrite(new_image_path, new_image)

        return cv2.imread(new_image_path)
