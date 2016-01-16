[![Build Status](https://travis-ci.org/matthieuchoplin/pycity.svg?branch=master)](https://travis-ci.org/matthieuchoplin/pycity)

The programs of these repositories have been written for **python3**.

It is recommended to use a *virtual environment* for running the programs.

## If the computer is running **python3** by default

You can use the [pyvenv](https://docs.python.org/3/library/venv.html) command.
### On UNIX systems (Linux and OSX), the command is:

`pyvenv venv`

### On WINDOWS system, the command is:

`c:\Temp>c:\Python35\python -m venv myenv`

Once created, you need to activate it:
 
 `source venv/bin/activate`
 
 to deactivate it:
 
 `deactivate`

## Or if the computer is running **python2** by default

You will have to use the program  [virtualenv](https://pypi.python.org/pypi/virtualenv)

You can install virtualenv with pip.

`pip install virtualenv`

Pip is a package manager program installed by default with Python 2 >=2.7.9 or Python 3 >=3.4.
Else, you can install pip by downloading the script [get-pip.py](https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py) and running `python get-pip.py`

### On UNIX systems (Linux and OSX):
To create a *virtual environment* using virtualenv with a python3 interpreter (that we precise with the option -p):

`virtualenv -p /usr/bin/python3.4 venv`

 and activate it with:
 
 `source venv/bin/activate`
 
 to deactivate it:
 
 `deactivate`
 
### On WINDOWS system:
To create a *virtual environment* using virtualenv with a python3 interpreter (that we precise with the option -p):

`virtualenv -p /path/to/python3.exe venv`

 the equivalent *activate* script is in the Scripts folder:
 
 `\path\to\env\Scripts\activate`
 
 to deactivate it:
 
 `deactivate`
 
 NB: To create a virtualenv under a path with spaces in it on Windows, you’ll need the [win32api](http://sourceforge.net/projects/pywin32/) library installed.
