import RPi.GPIO as GPIO
import time
from sensors import read_distance, read_dht

GPIO.setmode(GPIO.BCM)

# LED pin (final wiring)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

# Button pin (final wiring)
BUTTON_PIN = 27
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    try:
        while True:
            # Button logic
            button_pressed = GPIO.input(BUTTON_PIN) == GPIO.LOW

            # Sensor readings
            distance = read_distance()
            temp, hum = read_dht()

            # LED logic (example: turn on if object < 40cm)
            if distance < 40:
                GPIO.output(LED_PIN, True)
            else:
                GPIO.output(LED_PIN, False)

            print(f"Distance: {distance} cm | Temp: {temp}°C | Humidity: {hum}% | Button: {button_pressed}")

            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
