#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """prints C followed by the value of the text variable"""
    return 'c {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """display Python followed by the value of the text"""
    return 'python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """display n is a number only if n is an integer"""
    return '{} is number'.format(n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
