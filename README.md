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
./virtual/bin/python3.6 demo/script1.py
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