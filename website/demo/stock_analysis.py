"""

Draw a candlestick chart using bokeh and pandas_datareader

"""
from pandas_datareader import data
import fix_yahoo_finance as yf
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

# Data interval for stock search
start = datetime.datetime(2016, 2, 1)
end = datetime.datetime(2016, 3, 11)

# Example for Google here: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#google-finance
yf.pdr_override()
df = data.get_data_yahoo(tickers="GOOG", start=start, end=end)


def price_status_description(close_price, open_price):
    if close_price > open_price:
        return "Increase"

    if close_price < open_price:
        return "Decrease"

    return "Equal"


df["Status"] = [price_status_description(close_price, open_price) for close_price, open_price in zip(df.Close, df.Open)]
df["Height"] = abs(df.Open - df.Close)
df["Middle"] = (df.Open + df.Close) / 2

# Draw the figure
f = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_width')
f.grid.grid_line_alpha = 0.3

# Draw vertical lines
f.segment(df.index, df.High, df.index, df.Low, color="black")

# Draw rectangle
f.rect(
    df.index[df.Status == "Increase"],  # Get registries were Close > Open for x axis
    df.Middle[df.Status == "Increase"],  # Gent central axis of rectangles
    12 * 60 * 60 * 1000,  # x axis difference,
    df.Height[df.Status == "Increase"],  # Difference hight between top and bottom of rectangle.
    fill_color="green",
    line_color="black"
)

# Draw rectangle reversed
f.rect(
    df.index[df.Status == "Decrease"],  # Get registries were Close < Open for x axis,
    df.Middle[df.Status == "Decrease"],  # Gent central axis of rectangles
    12 * 60 * 60 * 1000,  # x axis difference
    df.Height[df.Status == "Decrease"],  # Difference hight between top and bottom of rectangle.
    fill_color="red",
    line_color="black"
)

"""

If you want to embed the graph in your website, you can do that

"""
candlestick_javascript, candlestick_html = components(f)  # Javascript and HTML content
candlestick_cdn_javascript = CDN.js_files[0]  # CDN js links
candlestick_cdn_css = CDN.css_files[0]  # CDN css links
