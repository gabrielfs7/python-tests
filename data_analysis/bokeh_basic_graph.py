# Import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# Prepare output file
output_file("Line.html")

# Create a figure object
f = figure()

# Create a line plot. We can also use "triangle" or "circle" instead of "line"
f.line(x, y)

show(f)