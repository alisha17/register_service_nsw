from app import app, db
from .models import User, Registration, Insurer, Vehicle
from flask import jsonify


@app.route("/")
def index():
    """
    Index page for the vehicle registration portal
    :return welcome message
    """
    return "Welcome to the Vehicle Registration Portal!"


@app.route("/registrations/<user_id>")
def get_registrations(user_id):
    """
    Endpoint to get vehicle registrations by user id
    :user_id The id of the user to get
    :return JSON returning all the vehicle registrations for a user id
    """
    query = (
        db.session.query(User, Vehicle, Registration, Insurer)
        .join(Registration, Vehicle.vin == Registration.vin)
        .join(Insurer, Vehicle.vin == Insurer.vin)
        .filter(User.user_id == user_id, User.user_id == Vehicle.user_id)
        .all()
    )

    format_query_op = dict(
        registrations=[
            dict(
                plate_number=vehicle.plate_number,
                registration=registration.serializable,
                vehicle=vehicle.serializable,
                insurer=insurer.serializable,
            )
            for user, vehicle, registration, insurer in query
        ]
    )

    resp = jsonify(format_query_op)

    return resp
