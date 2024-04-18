#!/usr/bin/python3
"""Import the required module"""
from flask import Flask
from urllib.parse import unquote


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """define a function that prints HEllo HBNB"""
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Prints HBNB"""
    text = unquote(text)
    return f'C {}'.format(text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>',  strict_slashes=False)
def pythoniscool(text):
    """Prints Python is cool"""
    text = unquote(text)
    return f'Python {}'.format(text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
