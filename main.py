# This is our main program which runs continously.
from sensor.temperature import read_temperature
from sensor.mpu6050 import read_vibration
import time

def main():
    print("Starting Machine Health Monitor...")
    while True:
        try:
            temp = read_temperature()
            vibration = read_vibration()

            print(f"Temperature: {temp} °C | Vibration: {vibration} g")


        except Exception as e:
            print("Error:", e)

        time.sleep(5)  # Delay between readings

if __name__ == "__main__":
    main()