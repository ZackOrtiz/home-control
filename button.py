# button.py — simulated button input

import random

def button_pressed():
    # 10% chance the button is "pressed"
    return random.choice([True] + [False]*9)
