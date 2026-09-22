from flask import Flask, render_template, request
import sensors
import logic
import actuators

app = Flask(__name__)

@app.route("/")
def home():
    temp, humidity = sensors.read_temperature_humidity()
    distance = sensors.read_distance()

    presence = logic.presence_state(distance)
    env = logic.environment_state(temp, humidity)

    return {
        "presence": presence,
        "temperature": temp,
        "humidity": humidity,
        "environment": env
    }

@app.route("/light/on")
def light_on():
    actuators.solid()
    return "Light turned ON"

@app.route("/light/off")
def light_off():
    actuators.off()
    return "Light turned OFF"

@app.route("/log")
def log():
    return "Log triggered"
