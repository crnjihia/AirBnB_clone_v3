#!/usr/bin/python3
"""
Flask web application that displays a list of states and details about a
specific state.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display an HTML page with a list of all states.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
    Display an HTML page with details about a specific state and its cities.
    """
    state = storage.get(State, id)
    if state:
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        return render_template(
            '9-states.html',
            state=state,
            cities=sorted_cities
        )
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
