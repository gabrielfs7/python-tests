import numpy
import cv2

"""

Create a 3D array from a predefined array

"""
n = numpy.arange(27)

print(n)

n = n.reshape(3, 3, 3)

print(n)

"""

Convert array to "numpy.ndarray"

"""
a = [[1, 2, 3], [4, 5, 5], [6, 7, 8]]

n = numpy.asarray(a)

print(n)


"""

Read a gray scale image and save as GBR 

"""
img_from_gray_scale_to_bgr = cv2.imread('numpy/smallgray.png', 1)

print(img_from_gray_scale_to_bgr)

img_bgr = cv2.imwrite("numpy/smallbgr.png", img_from_gray_scale_to_bgr)