# This code used to take vibration data from the machine.
import smbus2
import math
import time

MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

bus = smbus2.SMBus(1)  # I2C bus 1

# Wake up MPU6050
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr + 1)
    value = (high << 8) + low
    if value > 32767:
        value -= 65536
    return value

def read_vibration():
    ax = read_raw_data(ACCEL_XOUT_H) / 16384.0
    ay = read_raw_data(ACCEL_XOUT_H + 2) / 16384.0
    az = read_raw_data(ACCEL_XOUT_H + 4) / 16384.0
    vibration = math.sqrt(ax**2 + ay**2 + az**2)
    return round(vibration, 3)
