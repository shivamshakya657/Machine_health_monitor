# Machine Health Monitor using Raspberry Pi

This project is a real-time machine health monitoring system built using a Raspberry Pi. It uses Python to collect data from two key sensors: an MPU6050 accelerometer (for vibration) and a DS18B20 temperature sensor. The system continuously reads and displays live data, and also plots the results dynamically using Matplotlib.

The goal is to track the physical condition of machines, such as motors or rotating equipment, to detect potential issues early based on temperature and vibration patterns. This is especially useful in predictive maintenance applications, reducing downtime and improving operational efficiency.

This project was developed as part of my learning in embedded systems, Python, and sensor integration. It’s structured to be simple, modular, and ready for future extension (e.g., logging data, sending to cloud, or using a Flask dashboard).

---

## 🔧 Features

- Real-time temperature monitoring using DS18B20 sensor
- Real-time vibration monitoring using MPU6050 (3-axis accelerometer)
- Live data visualization using Matplotlib
- Modular Python code structure
- Works fully on Raspberry Pi using Python 3

---

## 🖥️ Technologies Used

- Python 3
- Matplotlib – for live graph plotting
- smbus2 – for I2C communication with MPU6050
- w1thermsensor – for DS18B20 integration
- Raspberry Pi– as the main embedded computing platform
- VS Code + GitHub – for development and version control

---

## 📦 Hardware Components

- Raspberry Pi (any model with GPIO and Python support)
- MPU6050 accelerometer/gyroscope sensor
- DS18B20 digital temperature sensor with 4.7kΩ pull-up resistor
- Breadboard and jumper wires

---

## 📁 Project Structure

machine-health-monitor/
├── main.py # Main execution file
├── live_plot.py # Real-time graph plotting
├── requirements.txt # Required Python libraries
├── sensor/
│ ├── mpu6050.py # Vibration sensor script
│ └── temperature.py # Temperature sensor script


## 🚀 How to Run

1. Clone the repository:

   git clone https://github.com/shivamshakya657/machine-health-monitor.git
   cd machine-health-monitor

2. Install dependencies:

    pip3 install -r requirements.txt

3. Run the main pyhton file:

    python3 main.py


4. To visualize data:

    python3 live_plot.py

## Future Improvements
    Add CSV logging for historical data

    Send data to ThingSpeak or MQTT dashboard

    Create Flask-based live web dashboard

    Add threshold-based alert system

## Author

    Shivam(Master's student of Electrical and Microsystem Engineering)
    