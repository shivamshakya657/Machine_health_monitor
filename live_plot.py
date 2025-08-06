# This code plot the live data of temperature and vibration sensor.
import matplotlib.pyplot as plt
from sensor.temperature import read_temperature
from sensor.mpu6050 import read_vibration
import time

# Data holders
temp_data = []
vibration_data = []
timestamps = []

plt.ion()  # Interactive mode on
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
fig.suptitle("Live Machine Health Monitor")

while True:
    try:
        temp = read_temperature()
        vibration = read_vibration()
        current_time = time.strftime("%H:%M:%S")

        # Add data
        timestamps.append(current_time)
        temp_data.append(temp)
        vibration_data.append(vibration)

        # Keep only last 20 points
        if len(timestamps) > 20:
            timestamps = timestamps[-20:]
            temp_data = temp_data[-20:]
            vibration_data = vibration_data[-20:]

        # Clear and plot
        ax1.clear()
        ax2.clear()

        ax1.plot(timestamps, temp_data, marker='o', color='r')
        ax1.set_title("Temperature (°C)")
        ax1.set_ylabel("°C")
        ax1.grid(True)

        ax2.plot(timestamps, vibration_data, marker='x', color='b')
        ax2.set_title("Vibration (g)")
        ax2.set_ylabel("g")
        ax2.set_xlabel("Time")
        ax2.grid(True)

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(1)

        print(f"[{current_time}] Temp: {temp} °C | Vib: {vibration} g")

    except Exception as e:
        print("Error:", e)
        time.sleep(2)
