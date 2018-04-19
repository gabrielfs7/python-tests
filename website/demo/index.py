from flask import Flask, render_template
import stock_analysis

app=Flask(__name__)


@app.route('/')
def home():
    return render_template(
        "home.html",
        candlestick_html=stock_analysis.candlestick_html,
        candlestick_javascript=stock_analysis.candlestick_javascript,
        candlestick_cdn_javascript=stock_analysis.candlestick_cdn_javascript,
        candlestick_cdn_css=stock_analysis.candlestick_cdn_css
    )


@app.route('/about')
def about():
    return render_template("about.html")


"""

If we run this script directly, so __name__ will be "__main__".

If this is script is run by different file, so __name__ will be "index.py".     

"""
if __name__ == "__main__":
    app.run(debug=True)