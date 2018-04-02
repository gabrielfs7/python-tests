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
```

install opencv to MAC

```bash
pip3.6 install opencv-python==3.3.0.10
brew install gtk+
brew install opencv
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
python3.6 -m venv virtual
cd website
./virtual/bin/pip3.6 install flask
./virtual/bin/pip3.6 install gunicorn
./virtual/bin/python3.6 demo/index.py
```


##### Deploy Heroku

1. Create a Heroku account: https://www.heroku.com/
2. Download Heroku TollBelt: https://devcenter.heroku.com/articles/heroku-cli#download-and-install

```bash
cd website/demo
heroku login
heroku create <<YOUR_APP_NAME>>
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
heroku git:remote --app py-app-gfs7
git push heroku master
heroku open
```

5. Get application info:

```bash
heroku info
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