
# This code used to take readings of temperature from the thermal sensor
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

def read_temperature():
    temp_celsius = sensor.get_temperature()
    return round(temp_celsius, 2)