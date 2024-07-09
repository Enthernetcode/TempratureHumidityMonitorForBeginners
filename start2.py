import time
from colorama import Fore, Style, init
import machine
import network
import dht
import urequests

init()

def slow_print(text, color=Fore.WHITE, delay=0.1):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def pause():
    input("\nPress Enter to continue...")

class TempHumidityMonitoringSystem:
    def __init__(self):
        self.quiz_questions = [
            {
                "question": "1. What is the default baud rate for ESP-01 module?",
                "options": ["A. 9600", "B. 115200", "C. 57600", "D. 4800"],
                "answer": "B"
            },
            {
                "question": "2. Which GPIO pins are available on the ESP-01 module?",
                "options": ["A. GPIO0 and GPIO2", "B. GPIO1 and GPIO3", "C. GPIO4 and GPIO5", "D. GPIO6 and GPIO7"],
                "answer": "A"
            }
        ]
        self.ssid = 'your-ssid'
        self.password = 'your-password'
        self.api_endpoint = 'http://your-api-endpoint'

    def guide_user(self):
        slow_print("Temperature and Humidity Monitoring System using ESP-01", Fore.CYAN)
        slow_print("\nStep 1: Gather Components", Fore.GREEN)
        instructions = [
            "You will need the following components:",
            "- ESP-01 module (ESP8266)",
            "- DHT11 or DHT22 temperature and humidity sensor",
            "- Battery (e.g., 18650 Li-ion)",
            "- Battery holder",
            "- Voltage regulator (e.g., AMS1117) for 3.3V output",
            "- Additional sensors or devices as required"
        ]
        for instruction in instructions:
            slow_print(instruction)
        pause()

        slow_print("\nStep 2: Set Up ESP-01", Fore.GREEN)
        instructions = [
            "1. Connect the ESP-01 to your computer using a USB-to-serial adapter.",
            "2. Flash the MicroPython firmware onto the ESP-01.",
            "3. Connect the DHT sensor to the ESP-01:",
            "   - VCC to 3.3V",
            "   - GND to GND",
            "   - Data to GPIO2",
            "4. Connect additional devices or sensors using I2C or UART as needed."
        ]
        for instruction in instructions:
            slow_print(instruction)
        pause()

        slow_print("\nStep 3: Configure Wi-Fi", Fore.GREEN)
        slow_print("Ensure the ESP-01 module connects to your Wi-Fi network.", Fore.GREEN)
        slow_print("Code Example:", Fore.GREEN)
        slow_print("""
        import network

        ssid = 'your-ssid'
        password = 'your-password'

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            pass

        print('Connection successful')
        print(wlan.ifconfig())
        """)
        pause()

        slow_print("\nStep 4: Reading from DHT Sensor", Fore.GREEN)
        slow_print("Write a Python script to read data from the DHT sensor.", Fore.GREEN)
        slow_print("Code Example:", Fore.GREEN)
        slow_print("""
        import dht
        import machine
        import time

        sensor = dht.DHT11(machine.Pin(2))

        while True:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            print('Temperature: {} C'.format(temp))
            print('Humidity: {} %'.format(hum))
            time.sleep(2)
        """)
        pause()

        slow_print("\nStep 5: Sending Data to Server", Fore.GREEN)
        slow_print("Write a Python script to send sensor data to a server.", Fore.GREEN)
        slow_print("Code Example:", Fore.GREEN)
        slow_print("""
        import urequests

        while True:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            data = {'temperature': temp, 'humidity': hum}
            response = urequests.post('http://your-api-endpoint', json=data)
            print(response.text)
            response.close()
            time.sleep(10)
        """)
        pause()

        slow_print("\nStep 6: Implementing Low Power Mode", Fore.GREEN)
        slow_print("Utilize ESP-01's deep sleep mode to save power.", Fore.GREEN)
        slow_print("Code Example:", Fore.GREEN)
        slow_print("""
        import machine

        # Deep sleep for 10 minutes
        deep_sleep_time = 10 * 60 * 1000

        def deep_sleep():
            print('Going to sleep...')
            machine.deepsleep(deep_sleep_time)

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
        """)
        pause()

    def take_quiz(self):
        slow_print("Temperature and Humidity Monitoring System Quiz", Fore.CYAN)
        correct_answers = 0
        for question in self.quiz_questions:
            slow_print("\n" + question["question"], Fore.BLUE)
            for option in question["options"]:
                slow_print(option, Fore.BLUE)
            answer = input("Your answer: ").strip().upper()
            if answer == question["answer"]:
                slow_print("Correct!", Fore.GREEN)
                correct_answers += 1
            else:
                slow_print(f"Incorrect! The correct answer was {question['answer']}.", Fore.RED)
        slow_print(f"\nYou got {correct_answers} out of {len(self.quiz_questions)} correct!", Fore.CYAN)

    def interactive_practice(self):
        slow_print("Interactive Practice Section", Fore.CYAN)
        slow_print("Follow the steps and confirm each step before proceeding.\n", Fore.CYAN)
        
        practice_steps = [
            ("Step 1: Gather Components", 
             "You will need the following components:\n"
             "- ESP-01 module (ESP8266)\n"
             "- DHT11 or DHT22 temperature and humidity sensor\n"
             "- Battery (e.g., 18650 Li-ion)\n"
             "- Battery holder\n"
             "- Voltage regulator (e.g., AMS1117) for 3.3V output\n"
             "- Additional sensors or devices as required"),
            ("Step 2: Set Up ESP-01", 
             "1. Connect the ESP-01 to your computer using a USB-to-serial adapter.\n"
             "2. Flash the MicroPython firmware onto the ESP-01.\n"
             "3. Connect the DHT sensor to the ESP-01:\n"
             "   - VCC to 3.3V\n"
             "   - GND to GND\n"
             "   - Data to GPIO2\n"
             "4. Connect additional devices or sensors using I2C or UART as needed."),
            ("Step 3: Configure Wi-Fi", 
             "Ensure the ESP-01 module connects to your Wi-Fi network.\n"
             "Code Example:\n"
             "```python\n"
             "import network\n\n"
             "ssid = 'your-ssid'\n"
             "password = 'your-password'\n\n"
             "wlan = network.WLAN(network.STA_IF)\n"
             "wlan.active(True)\n"
             "wlan.connect(ssid, password)\n\n"
             "while not wlan.isconnected():\n"
             "    pass\n\n"
             "print('Connection successful')\n"
             "print(wlan.ifconfig())\n"
             "```"),
            ("Step 4: Reading from DHT Sensor", 
             "Write a Python script to read data from the DHT sensor.\n"
             "Code Example:\n"
             "```python\n"
             "import dht\n"
             "import machine\n"
             "import time\n\n"
             "sensor = dht.DHT11(machine.Pin(2))\n\n"
             "while True:\n"
             "    sensor.measure()\n"
             "    temp = sensor.temperature()\n"
             "    hum = sensor.humidity()\n"
             "    print('Temperature: {} C'.format(temp))\n"
             "    print('Humidity: {} %'.format(hum))\n"
             "    time.sleep(2)\n"
             "```"),
            ("Step 5: Sending Data to Server", 
             "Write a Python script to send sensor data to a server.\n"
             "Code Example:\n"
             "```python\n"
             "import urequests\n\n"
             "while True:\n"
             "    sensor.measure()\n"
             "    temp = sensor.temperature()\n"
             "    hum = sensor.humidity()\n"
             "    data = {'temperature': temp, 'humidity': hum}\n"
             "    response = urequests.post('http://your-api-endpoint', json=data)\n"
             "    print(response.text)\n"
             "    response.close()\n"
             "    time.sleep(10)\n"
             "```"),
            ("Step 6: Implementing Low Power Mode", 
             "Utilize ESP-01's deep sleep mode to save power.\n"
             "Code Example:\n"
             "```python\n"
             "import machine\n\n"
             "# Deep sleep for 10 minutes\n"
             "deep_sleep_time = 10 * 60 * 1000\n\n"
             "def deep_sleep():\n"
             "    print('Going to sleep...')\n"
             "    machine.deepsleep(deep_sleep_time)\n\n"
             "while True:\n"
             "    sensor.measure()\n"
             "    temp = sensor.temperature()\n"
             "    hum = sensor.humidity()\n"
             "    data = {'temperature': temp, 'humidity': hum}\n"
             "    response = urequests.post('http://your-api-endpoint', json=data)\n"
             "    print(response.text)\n"
             "    response.close()\n"
             "    time.sleep(10)\n"
             "    deep_sleep()\n"
             "```")
        ]

        for step, instruction in practice_steps:
            slow_print(f"\n{step}", Fore.GREEN)
            slow_print(instruction, Fore.WHITE)
            complete = input("\nDid you complete this step? (yes/no): ").strip().lower()
            if complete != "yes":
                slow_print("Please complete the step before proceeding.", Fore.RED)
                pause()
            else:
                slow_print("Great! Let's move to the next step.", Fore.GREEN)
                pause()

if __name__ == "__main__":
    system = TempHumidityMonitoringSystem()
    system.guide_user()
    system.interactive_practice()
    system.take_quiz()
