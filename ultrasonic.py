# ultrasonic.py — random movement for demonstration

import random

def movement_detected():
    # 33% chance of movement each loop
    return random.choice([True, False, False])
