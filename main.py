from dht22 import read_dht22
from ultrasonic import movement_detected
from button import button_pressed
import time

mode = "STANDBY"
led = False

while True:
    temp, hum = read_dht22()
    move = movement_detected()
    btn = button_pressed()

    print(f"Temperature: {temp}°C | Humidity: {hum}%")

    if move:
        print("Movement detected!")
        mode = "ACTIVE"
        led = True

    if btn:
        print("Button pressed — toggling mode.")
        mode = "STANDBY" if mode == "ACTIVE" else "ACTIVE"
        led = not led

    print(f"Mode: {mode} | LED: {'ON' if led else 'OFF'}")
    print("-" * 40)

    time.sleep(2)
