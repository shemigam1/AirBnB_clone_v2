#!/usr/bin/python3

"""
module contains flask applications
"""

from flask import Flask
from flask import render_template
# from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False
# host = "0.0.0.0"
# port = 5000


@app.route("/")
def hello_world():
    """returns text string"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def hello_c(text):
    """returns varible text"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def hello_python(text):
    """returns varible text"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<int:n>")
def hello_n(n):
    """return if n is int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def hello_template(n=None):
    """return if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """runs app"""
    # app.run(host, port)
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)