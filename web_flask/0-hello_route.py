#!/usr/bin/python3
"""Import the required module"""
from flask import Flask


app = Flask(__name__)


@app.route('0.0.0.0', strict_slashes=False)
def hello():
    """define a function that prints HEllo HBNB"""
    name = request.args.get("name",  "HBNB")
    return f'Hello, {escape(name)}!'


if __name__ == "__main__":
    app.run()
