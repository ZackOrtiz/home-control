import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

def read_dht22():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return round(temperature, 1), round(humidity, 1)
    return None, None
