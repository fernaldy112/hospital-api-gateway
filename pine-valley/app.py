from flask import Flask, request
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
def getHelp():
    return {"name": "pine-valley"}


@app.route("/appointment", methods=["POST"])
def createAppointment():
    doctor = choice(doctors)
    hour = choice(hours)
    minute = choice(minutes)
    time = f"{hour:02}:{minute:02}"
    data = {
        "hospital": "Pine Valley",
        "doctor": doctor,
        "time": time,
    }
    return data
