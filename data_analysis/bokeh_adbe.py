import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Read csv file
data_frame = pandas.read_csv("bokeh_adbe.csv", parse_dates=["Date"])

# Create the figure object
f = figure(plot_height=200, plot_width=500, x_axis_type='datetime', sizing_mode='scale_width')
f.title.text = "Adb"
f.title.text_color = "gray"
f.title.text_font = "verdana"
f.title.text_font_style = "bold"
f.xaxis.minor_tick_line_color = "yellow"
f.yaxis.minor_tick_line_color = "red"
f.xaxis.axis_label = "Date"
f.yaxis.axis_label = "Close"

# Draw graph
f.line(data_frame['Date'], data_frame['Open'], line_width=2, color="green", alpha=0.5)
f.line(data_frame['Date'], data_frame['Close'], line_width=2, color="red", alpha=0.5)
f.circle(data_frame['Date'], data_frame['High'], size=3, color="blue", alpha=0.5)
f.circle(data_frame['Date'], data_frame['Low'], size=3, color="yellow", alpha=0.5)

# Set output file to draw the graph
output_file('line_from_adpe.html')

# Show graph
show(f)
