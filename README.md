# Python Tests

A simple repository for my personal python learning tests...


### Install dependency pip libraries:

```bash
pip3.6 install glob2
pip3.6 install pandas
pip3.6 install numpy
pip3.6 install ipython
pip3.6 install xlrd
pip3.6 install jupyter
pip3.6 install geopy
pip3.6 install folium
pip3.6 install flask
pip3.6 install virtualenv
pip3.6 install psycopg2
pip3.6 install psycopg2-binary
pip3.6 install pyinstaller
pip3.6 install bokeh
pip3.6 install bs4
pip3.6 install fix_yahoo_finance
pip3.6 install pandas_datareader
pip3.6 install Flask-SQLAlchemy
```

install opencv to MAC

```bash
pip3.6 install opencv-python==3.3.0.10
brew install gtk+
brew install opencv
```

### Create an executable to your application

```bash
cd tkinter/books
pyinstaller --onefile --windowed frontend.py
```


### Troubleshooting

I need to know available versions of a pip module? I.e. `opencv-python`:

```bash
pip3.6 install opencv-python==
```

### Access website

Create the virtual environment, so specific python modules will be inside.

`That is good to isolate your application environment.`

```bash
cd website
python3.6 -m venv virtual
./virtual/bin/pip3.6 install flask
./virtual/bin/pip3.6 install gunicorn
./virtual/bin/pip3.6 install bokeh
./virtual/bin/pip3.6 install bs4
./virtual/bin/pip3.6 install fix_yahoo_finance
./virtual/bin/pip3.6 install pandas_datareader
./virtual/bin/python3.6 demo/index.py
```


##### Deploy Heroku

1. Create a Heroku account: https://www.heroku.com/
2. Download Heroku TollBelt: https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Obs: Please, replace YOUR_APP_NAME to your chosen app name.

```bash
cd website/demo
heroku login
heroku create YOUR_APP_NAME
```

3. Create necessary python dependencies file for Heroku:

```bash
cd website/demo
./../virtual/bin/pip3.6 freeze > requirements.txt
```

**IMPORTANT**: Check supported python runtime for runtime.txt: https://devcenter.heroku.com/articles/python-runtimes#supported-python-runtimes


4. Set remote git Heroku


```bash
cd website/demo
git init
git add .
git commit -m 'my first commit'
heroku git:remote --app YOUR_APP_NAME
git push heroku master
heroku open
```

5. Get application info:

```bash
heroku info
```
or more config info:

```bash
heroku config --app YOUR_APP_NAME
```

6. Create heroku database.

```bash
heroku addons:create heroku-postgresql:hobby-dev --app YOUR_APP_NAME
``` 

7. To run programs in heroku:

```bash
heroku run python
```

or to run bash:

```bash
heroku run bash
```

### Execute Jupyter notebook on MAC OS

For data analysis I am using Jupyter. You can find more information here:

http://jupyter.org

To open Jupyter files on MAC type:

```bash
cd PROJECT_DIR
/Library/Frameworks/Python.framework/Versions/3.6/bin/jupyter notebook
```

Then go to the files tree and select the jupyter (.ipynb) file to edit. 