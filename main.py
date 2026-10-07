import RPi.GPIO as GPIO
import time
from ultrasonic import movement_detected
from dht22 import read_dht22

GPIO.setmode(GPIO.BCM)

LED = 18
BUTTON = 17

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ACTIVE = 1
STANDBY = 0

mode = ACTIVE
last_movement_time = time.time()
TIMEOUT = 20  # seconds

def set_led(active):
    GPIO.output(LED, GPIO.HIGH if active else GPIO.LOW)

def toggle_mode(channel):
    global mode
    mode = ACTIVE if mode == STANDBY else STANDBY
    print(f"Mode changed to: {'ACTIVE' if mode == ACTIVE else 'STANDBY'}")

GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=toggle_mode, bouncetime=300)

try:
    while True:
        temp, hum = read_dht22()
        if temp is not None:
            print(f"Temp: {temp}°C  Humidity: {hum}%")

        if movement_detected():
            last_movement_time = time.time()
            if mode == STANDBY:
                print("Movement detected → Waking system")
                mode = ACTIVE

        if mode == ACTIVE:
            set_led(True)
        else:
            set_led(False)

        if mode == ACTIVE and (time.time() - last_movement_time > TIMEOUT):
            print("No movement → Switching to Standby")
            mode = STANDBY

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
