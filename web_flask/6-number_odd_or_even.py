#!/usr/bin/python3
""" Flask web application: HBNB """


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Method that display hello HBNH in web flask
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    Method that display HBNH in web flask
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_IsFun(text):
    """
    Method that when passing arguments shows the
    passed name and character "_" is changed by spaces
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_Is_Cool(text="is cool"):
    """
    Method that when passing arguments shows the
    passed name and character "_" is changed by spaces
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_Number(n):
    """
    Method that when passing arguments in the number route
    validates if it is an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_Template(n):
    """
    Method that when passing arguments in the number_template
    route a number is displayed in an html structure
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Method that when passing arguments in the route number_odd_or_even a
    number shows if it is even o odd"
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
