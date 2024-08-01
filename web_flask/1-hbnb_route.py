#!/usr/bin/python3

"""
module contains flask applications
"""

from flask import Flask

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


if __name__ == "__main__":
    """runs app"""
    # app.run(host, port)
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
