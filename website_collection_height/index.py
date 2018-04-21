from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from email.mime.text import MIMEText
import smtplib

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@127.0.0.1/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def send_mail(email, height):
    from_email = "XXXX@gmail.com"
    from_pass = "XXXXX"

    subject = "Height data"
    message = "Hello, you sent us your email %s and height %s." % (email, height)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pass)
    gmail.send_message()


class Data(db.Model):
    """
    Database model structure

    To initiate the database, create table, etc, please run it before in terminal:

    python3.6
    >> from index import db
    >> db.create_all()

    """
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)  # Max 120 chars
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route('/', methods=['POST', 'GET'])
def home():
    form_success = False
    form_email_repeated = False
    form_email = ''
    form_height = ''

    if request.method == 'POST':
        form_email = request.form['email']
        form_height = request.form['height']
        form_email_repeated = True

        # Save data to database, if e-mail does not exists
        if db.session.query(Data).filter(Data.email == form_email).count() != 1:
            data = Data(form_email, form_height)
            db.session.add(data)
            db.session.commit()

            send_mail(form_email, form_height)

            form_success = True
            form_email_repeated = False

    return render_template(
        "index.html",
        form_email=form_email,
        form_height=form_height,
        form_success=form_success,
        form_email_repeated=form_email_repeated
    )


@app.route('/results')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)