# Temperature and Humidity Monitoring System using ESP-01

## Overview

This project provides an interactive guide for setting up a Temperature and Humidity Monitoring System using an ESP-01 module (ESP8266) and an 8-bit MCU (AVR/PIC/ARM/RISC-V). The guide includes step-by-step instructions, protocols, principles, interactive practice sections, quizzes, and example code.

## Features

- Detailed step-by-step guide for setting up the system
- Protocols and principles to ensure proper setup and operation
- Interactive practice section to reinforce learning
- Quiz section to test your knowledge
- Example code for both MCU and ESP-01 module
- Interactive user interface with colorful text for better user experience
- Connect additional sensors or devices using I2C or UART
- Run the system on a standalone battery
- Implement low power modes using deep sleep to conserve battery life

## Components

- ESP-01 module (ESP8266)
- 8-bit MCU (e.g., AVR like ATmega328P, PIC like PIC16F877A, ARM like STM32F103, RISC-V like GD32VF103)
- Temperature and Humidity Sensor (e.g., DHT11, DHT22)
- Breadboard and Jumper wires
- Power supply (3.3V for ESP-01 and appropriate supply for MCU)
- USB-to-Serial adapter for programming ESP-01
- Resistors (10kΩ for pull-up, others as needed)
- Capacitors (decoupling capacitors, if necessary)
- Battery (e.g., 18650 Li-ion) and battery holder
- Voltage regulator (e.g., AMS1117) for 3.3V output

## Requirements

- Python 3.x
- `colorama` library (for colored text)
- `requests` library (for HTTP requests)

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required Python libraries using pip:
    ```bash
    pip install colorama requests
    ```

## Usage

1. Clone this repository or download the script.
    ```bash
    git clone https://github.com/Enthernetcode/TemperatureHumidityMonitorForBeginners
    ```
2. Run the script using Python:
    ```bash
    python start.py
    ```
3. Follow the on-screen instructions to navigate through the guide, take the quiz, and practice the steps interactively.

## Interactive Guide Steps

1. **Gather Components**
    - Collect all required components listed above.
2. **Set Up ESP-01 Module**
    - Flash MicroPython firmware and configure Wi-Fi settings.
3. **Interface with 8-bit MCU**
    - Connect ESP-01 to the MCU and configure communication protocols.
4. **Connect Temperature and Humidity Sensor**
    - Interface the DHT11/DHT22 sensor with the MCU and ESP-01.
5. **Program the MCU**
    - Write and upload code to read sensor data and send it to ESP-01.
6. **Establish Communication Between ESP-01 and MCU**
    - Implement and test communication between the MCU and ESP-01.
7. **Test the System**
    - Verify that the system is reading and transmitting data correctly.

## Protocols

1. Ensure proper power supply connections.
2. Use appropriate pull-up resistors where necessary.
3. Avoid electrostatic discharge when handling components.
4. Follow the pin configurations and datasheets strictly.

## Principles

1. Understand the functionality of each component.
2. Maintain a clean and organized workspace.
3. Double-check connections before powering the circuit.
4. Test individual components before integrating them.

## Example Code

### MCU (AVR, using Arduino IDE)

Here's an example of how to set up your MCU (e.g., ATmega328P) using the Arduino IDE to read data from a DHT11 sensor and send it over the serial port:

```cpp
#include <DHT.h>

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.println(F("°C "));
}



This code initializes the DHT sensor, reads the humidity and temperature, and prints the values to the serial monitor every 2 seconds.

### ESP-01 (ESP8266, using MicroPython)

Here's an example of how to set up your ESP-01 module using MicroPython to read data from a DHT11 sensor and send it to a web server:

```python
import machine
import dht
import network
import urequests
import time

# Wi-Fi Configuration
ssid = 'your-ssid'
password = 'your-password'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('Connection successful')
print(wlan.ifconfig())

# Sensor Setup
sensor = dht.DHT11(machine.Pin(2))

# Data Reading and Transmission
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    data = {'temperature': temp, 'humidity': hum}
    response = urequests.post('http://your-api-endpoint', json=data)
    print(response.text)
    response.close()
    time.sleep(10)

# Implementing Low Power Mode
def deep_sleep():
    print('Going to sleep...')
    machine.deepsleep(10 * 60 * 1000)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    data = {'temperature': temp, 'humidity': hum}
    response = urequests.post('http://your-api-endpoint', json=data)
    print(response.text)
    response.close()
    time.sleep(10)
    deep_sleep()
```

This code connects to a Wi-Fi network, reads data from a DHT11 sensor, sends the data to a specified endpoint, and then puts the ESP-01 into deep sleep mode to conserve power.

## Interactive Practice

Follow the interactive practice steps in the script and confirm each step before proceeding. Use the example code provided to program your MCU and ESP-01.

## Quiz

Test your knowledge with the quiz section in the script. Answer multiple-choice questions to assess your understanding of the system setup and operation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or additions.

## Troubleshooting

If you encounter any issues during the setup, here are a few tips:

1. **Check Connections**: Ensure all wires and components are connected correctly according to the guide.
2. **Power Supply**: Verify that your power supply is adequate and stable.
3. **Serial Communication**: Make sure your serial communication settings are correct and your USB-to-Serial adapter is functioning properly.
4. **Sensor Calibration**: Some sensors might require calibration before providing accurate readings.

If you need further assistance, please open an issue in this repository or refer to the documentation of the components you're using.

## Contact

For any queries or support, you can reach out via the Issues section on GitHub or contact the repository maintainer.

## Acknowledgments

- Thanks to the contributors of the `colorama` and `requests` libraries.
- Special thanks to the community members who provide continuous support and improvements.

Enjoy building your Temperature and Humidity Monitoring System!

