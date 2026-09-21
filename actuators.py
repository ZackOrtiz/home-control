import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
BUTTON_PIN = 22

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def solid():
    GPIO.output(LED_PIN, GPIO.HIGH)

def off():
    GPIO.output(LED_PIN, GPIO.LOW)

def slow_blink():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

def fast_blink():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)

def double_blink():
    for _ in range(2):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
    time.sleep(0.3)

def button_pressed():
    return GPIO.input(BUTTON_PIN) == GPIO.LOW
