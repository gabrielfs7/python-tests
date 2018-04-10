"""

The main goal is to teach how to resize images

"""
import cv2

with_color = 1

# This is a numpay array containing the pixel matrix for the image
image = cv2.imread('sample-images/galaxy.jpg', with_color)

# Show image before resize
cv2.imshow('Galaxy', image)

# Resize image
image_width = image.shape[0]
image_height = image.shape[1]

new_image_with = int(image_width / 5)
new_image_height = int(image_height / 5)

new_image = cv2.resize(image, (new_image_height, new_image_with))

# Show resized image
cv2.imshow('Galaxy resized', new_image)

# Save resized image
cv2.imwrite('sample-images/galaxy2.jpg', new_image)

# Keep images on the screen for 5 seconds
cv2.waitKey(5000)
cv2.destroyAllWindows()