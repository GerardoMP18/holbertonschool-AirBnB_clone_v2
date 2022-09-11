#!/usr/bin/python3
""" Flask web application: HBNB """


from cgitb import text
from email.policy import default
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Function that display hello HBNH in web flask
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    Function that display HBNH in web flask
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_IsFun(text):
    """
    Function that when passing arguments shows the
    passed name and character "_" is changed by spaces
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_Is_Cool(text="is cool"):
    """
    Function that when passing arguments shows the
    passed name and character "_" is changed by spaces
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
