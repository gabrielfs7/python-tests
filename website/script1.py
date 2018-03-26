from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/test')
def test():
    return 'My website home TEST'


"""

If we run this script directly, so __name__ will be "__main__".

If this is script is run by different file, so __name__ will be "script1.py".     

"""
if __name__ == "__main__":
    app.run(debug=True)