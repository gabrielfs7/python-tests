import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Read info from CSV file and make a DataFrame
data_frame = pandas.read_csv("bokeh_bachelors.csv")

# Set columns to figure based on the grath
x = data_frame['Year']
y = data_frame['Engineering']

output_file('line_from_bachelors.html')

# Create the figure object
f = figure()

# Draw graph
f.line(x, y)

# Show graph
show(f)