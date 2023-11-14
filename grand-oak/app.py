from flask import Flask, request
from random import choice
app = Flask(__name__)

doctors = [
    'Rhys Hawkins',
    'Vilma Jarvi',
    'Ted Ellison',
    'Heath Atwood',
    'Kinslee Fink'
]

hours = list(range(8, 16))
minutes = [0, 15, 30, 45]


@app.route("/help", methods=["GET"])
def getHelp():
    return {"name": "grand-oak"}


@app.route("/appointment", methods=["POST"])
def createAppointment():
    doctor = choice(doctors)
    hour = choice(hours)
    minute = choice(minutes)
    time = f"{hour:02}:{minute:02}"
    data = {
        "hospital": "Grand Oak Hospital",
        "doctor": doctor,
        "time": time,
    }
    return data
