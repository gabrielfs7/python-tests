"""

1. Capture camera image
2. Resize image and show
3. Add information for image
3. Detect the face and draw an rectangle around it

IMPORTANT: If camera fail on MacOS, type "sudo killall VDCAssistant" in the terminal

"""

import cv2
import pandas
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

video_capture = cv2.VideoCapture(0)
first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=['Start', 'End'])

while True:

    # Default is not activity
    status = 0
    check, frame = video_capture.read()

    # Make image gray
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Make blur to make easier to detect threshold difference
    gray_frame - cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Necessary to get first image without no movement
    if first_frame is None:
        first_frame = gray_frame

        continue

    # Get absolute difference between images
    delta_frame = cv2.absdiff(first_frame, gray_frame)

    # Make black and white contrast as threshold. Second item returned is the new Numpy array
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    # Find image contours
    (_, contours, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Only consider areas where contours are higher than 1000px and draw a rectangle
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        status = 1

    # Append current status activity
    status_list.append(status)

    # Make list be only last to registries to avoid memory problems
    status_list = status_list[-2:]

    # Save movements detection interval
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())

    # Save movements detection interval
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Display images
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Normal Frame", frame)

    # Break the loop if q is pressed
    if cv2.waitKey(100) == ord('q'):
        if status == 1:
            times.append(datetime.now())

        break

# Iterate times jumping by 2 steps
start = 0
stop = len(times)
step= 2

# Save movement detections to a CSV file
for i in range(start, stop, step):
    df = df.append({"Start" : times[i], "End" : times[i + 1]}, ignore_index=True)

df.to_csv("times.csv")

# Close the video and destroy windows
video_capture.release()
cv2.destroyAllWindows()

"""

Generate graph

"""
# Format date to HoverTool
df['Start_format'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%s")
df['End_format'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%s")

# Necessary for hover
cds = ColumnDataSource(df)

# Create figure
f = figure(x_axis_type="datetime", height=80, width=500, sizing_mode='scale_width', title="Movement Capture")

# Remove Y axis interval marker
f.yaxis.minor_tick_line_color = None

# Eliminate graph grid
f.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_format"), ("End", "@End_format")])
f.add_tools(hover)

# left and right point to cds indexes
q = f.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)

# Output graph
output_file("quad_from_capture_movement.html")

# Show graph
show(f)
