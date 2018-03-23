import numpy
import cv2
import pprint

image = cv2.imread('smallgray.png', 0)
pprint.pprint(image)

# Slice from row 0 to 2. Slice from colum 2 to 4 in the sliced rows
pprint.pprint(image[0:2, 2:4])

# Show number of rows, columns\n",
pprint.pprint(image.shape)

# Get value from y=2 and x=4\n",
pprint.pprint(image[2, 4])

# Iterate normal array
for i in image:
    print(i)

# Exchange columns to row to iterate
for i in image.T:
    print (i)

# Iterate a unidimensional array
for i in image.flat:
    print(i)

# Concatenate arrays by merging line by line (or horizontally)
image_stack = numpy.hstack((image, image, image))
pprint.pprint(image_stack)

# Split array in 3 arrays horizontally
pprint.pprint(numpy.hsplit(image_stack, 3))

# Split array vertically
pprint.pprint(numpy.vsplit(image_stack, 3))

# Concatenate array by adding more lines (or vertically)\n",
image_stack = numpy.vstack((image, image, image))
pprint.pprint(image_stack)
