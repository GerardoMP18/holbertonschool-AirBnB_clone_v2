#!/usr/bin/python3
""" Flask web application: HBNB """

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def session_close(exception):
    """
    method to close the session of the db
    """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def States_and_State(id=None):
    """
    Method that shows when passing all states as state route,
    route id shows all states with their respective city
    """
    states = storage.all(State)
    if id is not None:
        id = "State." + id
    return render_template("9-states.html", states=states, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
