#!/usr/bin/python3
"""
A script that starts the flask web application
it must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space
/python/(<text>): display “Python ”, followed by the value
of the text variable (replace underscore _ symbols with a space
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
