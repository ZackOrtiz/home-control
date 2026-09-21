import time
import sensors
import logic
import actuators
import cloud
import notify

no_presence_timer = 0
ALERT_THRESHOLD = 900  # 15 minutes

while True:
    temp, humidity = sensors.read_temperature_humidity()
    distance = sensors.read_distance()

    presence = logic.presence_state(distance)
    env = logic.environment_state(temp, humidity)

    # LED patterns
    if presence == "movement":
        actuators.solid()
        no_presence_timer = 0
        led_state = "solid"
    else:
        no_presence_timer += 1
        actuators.slow_blink()
        led_state = "slow_blink"

    # Email/Slack alert
    if no_presence_timer > ALERT_THRESHOLD:
        notify.send_alert("No presence detected for 15 minutes.")
        no_presence_timer = 0

    # Button → cloud logging
    if actuators.button_pressed():
        data = {
            "presence": presence,
            "temperature": temp,
            "humidity": humidity,
            "led_state": led_state
        }
        cloud.send_log(data)

    time.sleep(1)
