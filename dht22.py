# dht22.py — simulated DHT22 sensor with static temperature

import random

STATIC_TEMP = 24.5        # constant room temperature
current_humidity = 52.0   # starting humidity

def read_dht22():
    global current_humidity

    # Humidity drifts slowly like a real environment
    drift = random.uniform(-0.2, 0.2)
    current_humidity = max(40.0, min(60.0, current_humidity + drift))

    temp = STATIC_TEMP
    hum = round(current_humidity, 1)

    return temp, hum
