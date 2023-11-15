from flask import Flask, request
import re
from random import choice
app = Flask(__name__)

doctors = [
    'Joshua Wilson',
    'Victoria Roach',
    'Ellis Schaefer',
    'Regan Rosen',
    'Daisy Morgan'
]

hours = list(range(8, 16))
minutes = [0, 15, 30, 45]


@app.route("/help", methods=["GET"])
def get_help():
    return {"name": "pine-valley"}


@app.route("/appointment", methods=["POST"])
def create_appointment():
    error = validate_request_body(request.form)
    if error is not None:
        return {
            "message": error
        }, 400

    doctor = choice(doctors)
    hour = choice(hours)
    minute = choice(minutes)
    time = f"{hour:02}:{minute:02}"
    data = {
        "hospital": "Pine Valley Hospital",
        "doctor": doctor,
        "time": time,
    }
    return data

def validate_request_body(body: dict):
    if "name" not in body:
        return "The field `name` is required."
    if "date" not in body:
        return "The field `date` is required."
    if not is_iso_date(body["date"]):
        return "Invalid date."

def is_iso_date(date: str) -> bool:
    return re.search("\\d{4}-((1[0-2])|(0[1-9]))-((31)|([12][0-9])|(0[1-9]))", date) is not None