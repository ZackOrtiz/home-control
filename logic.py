def presence_state(distance):
    if distance < 100:  # movement detected
        return "movement"
    return "no_movement"

def environment_state(temp, humidity):
    if temp is None or humidity is None:
        return "unknown"

    if temp > 28:
        return "hot"
    elif temp < 18:
        return "cold"
    else:
        return "comfortable"
