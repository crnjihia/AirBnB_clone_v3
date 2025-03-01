#!/usr/bin/python3
"""
Flask web application that displays a page with filters
for states, cities, amenities, and places.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display a HTML page with filters for states, cities, amenities, and places.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    places = storage.all(Place).values()
    sorted_places = sorted(places, key=lambda place: place.name)
    return render_template('100-hbnb.html',
                           states=sorted_states,
                           amenities=sorted_amenities,
                           places=sorted_places)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
