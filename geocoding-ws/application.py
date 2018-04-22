from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
from geopy.geocoders import Nominatim
import pandas

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    form_success = False
    form_error = False
    global file_name
    global file_path
    csv_lines = []

    if request.method == 'POST':
        try:
            file = request.files['file']
            file_name = secure_filename(file.filename)
            file_path = "downloads/processed-" + file_name
            file.save(file_path)

            df = pandas.read_csv(file_name)

            nominatim = Nominatim(scheme="http")

            df['Coordinates'] = df['Address']
            df['Coordinates'] = df['Coordinates'].apply(nominatim.geocode)
            df['Latitude'] = df['Coordinates'].apply(
                lambda column_value: column_value.latitude if column_value != None else ''
            )
            df['Longitude'] = df['Coordinates'].apply(
                lambda column_value: column_value.longitude if column_value != None else ''
            )

            # Remove temp column
            df = df.drop('Coordinates', 1)

            # Avoid save index to CSV
            df.to_csv(file_path, index=False)

            csv_lines = df.iterrows()

            form_success = True
        except:
            form_error = True

    return render_template(
        "index.html",
        form_success=form_success,
        csv_lines=csv_lines,
        form_error=form_error

    )


@app.route('/download')
def download():
    return send_file(
        file_path,
        attachment_filename=file_name,
        as_attachment=True
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
