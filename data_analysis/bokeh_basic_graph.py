# Import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# Create a DataFrame based on CSV file
data_frame = pandas.read_csv("bokeh_basic_graph.csv")

# prepare some data
x = data_frame['X']
y = data_frame['Y']

# Prepare output file
output_file("line_from_csv.html")

# Create a figure object
f = figure()

# Create a line plot. We can also use "triangle" or "circle" instead of "line"
f.line(x, y)

show(f)