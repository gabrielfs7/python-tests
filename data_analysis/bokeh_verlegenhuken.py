import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Read info from XLSX file and make a DataFrame
# Columns in file: ..., Year, Month, Day, Hour, Temperature, Pressure
data_frame = pandas.read_excel("bokeh_verlegenhuken.xlsx")

# Divide Pressure and Temperature by 10 for each line, because they are in scale of 10
data_frame['Temperature'] = data_frame['Temperature'] / 10
data_frame['Pressure'] = data_frame['Pressure'] / 10

# Set columns to figure based on the grath
x = data_frame['Temperature']
y = data_frame['Pressure']

# Create the figure object
f = figure(plot_height=500, plot_width=500, tools='pan', logo=None)
f.title.text = "Temperature and Air Pressure"
f.title.text_color = "gray"
f.title.text_font = "verdana"
f.title.text_font_style = "bold"
f.xaxis.minor_tick_line_color = "yellow"
f.yaxis.minor_tick_line_color = "red"
f.xaxis.axis_label = "Temperature (˚C)"
f.yaxis.axis_label = "Pressure (hPa)"

# Draw graph
f.circle(x, y, size=0.5, color="red", alpha=0.5)

# Set output file to draw the graph
output_file('circle_from_verlegenhuken.html')

# Show graph
show(f)