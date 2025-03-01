#!/usr/bin/python3
'''Defines RESTful API actions for State objects.'''
from flask import jsonify, request, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'])
@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def handle_states(state_id=None):
    '''Handles all default RESTful API actions for State objects.

    Args:
        state_id (str, optional): The ID of the State. Defaults to None.

    Returns:
        Response: JSON response or error message.
    '''
    if request.method == 'GET':
        return get_state(state_id) if state_id else get_all_states()
    elif request.method == 'DELETE':
        return delete_state(state_id)
    elif request.method == 'POST':
        return create_state()
    elif request.method == 'PUT':
        return update_state(state_id)
    else:
        abort(405)  # Method Not Allowed


def get_all_states():
    '''Retrieves a list of all State objects.

    Returns:
        Response: JSON list of all State objects.
    '''
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


def get_state(state_id):
    '''Retrieves a specific State object by ID.

    Args:
        state_id (str): The ID of the State.

    Returns:
        Response: JSON representation of the State or 404 error.
    '''
    state = storage.get(State, state_id)
    if not state:
        abort(404, description="State not found")
    return jsonify(state.to_dict())


def delete_state(state_id):
    '''Deletes a specific State object by ID.

    Args:
        state_id (str): The ID of the State.

    Returns:
        Response: Empty dictionary with status code 200 or 404 error.
    '''
    state = storage.get(State, state_id)
    if not state:
        abort(404, description="State not found")
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


def create_state():
    '''Creates a new State object.

    Returns:
        Response: JSON representation of the new State with status code 201.
    '''
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


def update_state(state_id):
    '''Updates a specific State object by ID.

    Args:
        state_id (str): The ID of the State.

    Returns:
        Response: JSON representation of the updated State or 404 error.
    '''
    state = storage.get(State, state_id)
    if not state:
        abort(404, description="State not found")
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
