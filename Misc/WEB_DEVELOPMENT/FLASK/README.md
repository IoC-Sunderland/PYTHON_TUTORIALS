# Introduction to Flask
**Flask** is a Python web framework designed to help with creating web applications.

We will be using **Flask** to create our web applications.

As Flask is not part of the Python standard library (it doesn't come with Python itself) we need to install it first.

We can do this using **pip** which is the Python package manager.

```
pip install Flask
```
For this command to work successfully we need an internet connection as ***pip*** will go and retrieve the ***Flask*** package from **PyPi - The Python Package Index.**

**PyPi** is like an online hub that stores all packages we might install with pip.

An example of the output we would expect  below:
```
Collecting Flask
  Using cached Flask-2.0.2-py3-none-any.whl (95 kB)
Collecting itsdangerous>=2.0
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting Werkzeug>=2.0
  Using cached Werkzeug-2.0.2-py3-none-any.whl (288 kB)
Collecting click>=7.1.2
  Using cached click-8.0.3-py3-none-any.whl (97 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.3-py3-none-any.whl (133 kB)
Collecting importlib-metadata
  Downloading importlib_metadata-4.10.0-py3-none-any.whl (17 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.0.1-cp37-cp37m-macosx_10_9_x86_64.whl (13 kB)
Collecting typing-extensions>=3.6.4
  Downloading typing_extensions-4.0.1-py3-none-any.whl (22 kB)
Collecting zipp>=0.5
  Downloading zipp-3.7.0-py3-none-any.whl (5.3 kB)
Installing collected packages: zipp, typing-extensions, MarkupSafe, importlib-metadata, Werkzeug, Jinja2, itsdangerous, click, Flask
Successfully installed Flask-2.0.2 Jinja2-3.0.3 MarkupSafe-2.0.1 Werkzeug-2.0.2 click-8.0.3 importlib-metadata-4.10.0 itsdangerous-2.0.1 typing-extensions-4.0.1 zipp-3.7.0
```
To check if installation has been completed successfully:

Launch interpreter:

```
$ python
```
```
>>> from flask import Flask
>>> help(Flask)
```

Result should be:
```
Help on class Flask in module flask.app:
...
```



