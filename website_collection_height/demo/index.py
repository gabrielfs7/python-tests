from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from email.mime.text import MIMEText
from sqlalchemy.sql import func
from werkzeug import secure_filename
import smtplib

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@127.0.0.1/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://orauhbhhnkcojk:c12dbc0485914eee2cf3cbc9b1901c229faf075678c9c535f9c016d3dfc03b9f@ec2-54-235-193-34.compute-1.amazonaws.com:5432/dak32a6lbkctfl?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def send_mail(email, height):
    """
    Send e-mail for user

    :param email:
    :param height:
    :return:
    """
    from_email = "XXXX@gmail.com"
    from_pass = "XXXXX"

    subject = "Height data"
    body = "Hello, you sent us your email %s and height %s." % (email, height)

    message = MIMEText(body, 'html')
    message['Subject'] = subject
    message['To'] = email
    message['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pass)
    gmail.send_message(message)


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
    average_height = 0
    total_people  = 0

    if request.method == 'POST':
        form_email = request.form['email']
        form_height = request.form['height']
        form_email_repeated = True

        # Save data to database, if e-mail does not exists
        if db.session.query(Data).filter(Data.email == form_email).count() != 1:
            data = Data(form_email, form_height)
            db.session.add(data)
            db.session.commit()

            # Uncomment this line if you want to send e-mail
            """
            send_mail(form_email, form_height) 
            """
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height)
            total_people = db.session.query(Data.height).count()
            form_success = True
            form_email_repeated = False

    return render_template(
        "index.html",
        form_email=form_email,
        form_height=form_height,
        form_success=form_success,
        form_email_repeated=form_email_repeated,
        average_height=average_height,
        total_people=total_people
    )


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    """
    Example how to upload file:

    :return:
    """
    success=False
    file_name = ''

    if request.method == 'POST':
        uploaded_file = request.files['file']
        uploaded_file_content = uploaded_file.read()

        file_name = "uploaded" + uploaded_file.filename

        uploaded_file.save(secure_filename(file_name))

        success = True

    return render_template(
        "upload.html",
        success=success,
        file_name=file_name
    )


@app.route('/download')
def download():
    """
    Example how to download file:

    :return:
    """
    return send_file(
        "../../README.md",
        attachment_filename='README.md',
        as_attachment=True
    )

if __name__ == "__main__":
    app.debug = True
    app.run()