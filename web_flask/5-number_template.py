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
    """Prints C is fun"""
    text = unquote(text)
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>',  strict_slashes=False)
def python_is_cool(text):
    """Prints Python is cool"""
    text = unquote(text)
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numberiscool(n):
    """Prints number only if it is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>',  strict_slashes=False)
def number_template(n):
    """PRints number only if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number_template.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
