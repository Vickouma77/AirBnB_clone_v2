#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display html page with state listed in order"""
    states = sorted(list(storage.all("state").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
