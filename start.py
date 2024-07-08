import time
from colorama import Fore, Style, init

# Initialize colorama
init()

class TemperatureHumidityMonitoringSystem:
    def __init__(self):
        self.steps = [
            "Step 1: Gather Components",
            "Step 2: Set Up ESP-01 Module",
            "Step 3: Interface with 8-bit MCU",
            "Step 4: Connect Temperature and Humidity Sensor",
            "Step 5: Program the MCU",
            "Step 6: Establish Communication Between ESP-01 and MCU",
            "Step 7: Test the System"
        ]
        self.protocols = [
            "Protocol 1: Ensure proper power supply connections.",
            "Protocol 2: Use appropriate pull-up resistors where necessary.",
            "Protocol 3: Avoid electrostatic discharge when handling components.",
            "Protocol 4: Follow the pin configurations and datasheets strictly."
        ]
        self.principles = [
            "Principle 1: Understand the functionality of each component.",
            "Principle 2: Maintain a clean and organized workspace.",
            "Principle 3: Double-check connections before powering the circuit.",
            "Principle 4: Test individual components before integrating them."
        ]
        self.quiz_questions = [
            {
                "question": "What is the purpose of the pull-up resistors in the circuit?",
                "options": ["A) To reduce noise", "B) To prevent floating pins", "C) To save power", "D) To increase signal strength"],
                "answer": "B"
            },
            {
                "question": "Which protocol should be followed to prevent damage from electrostatic discharge?",
                "options": ["A) Use gloves", "B) Work on a metal surface", "C) Avoid touching components directly", "D) Work in a humid environment"],
                "answer": "C"
            },
            {
                "question": "What should you double-check before powering the circuit?",
                "options": ["A) Connections", "B) Code", "C) Power supply", "D) All of the above"],
                "answer": "D"
            },
            {
                "question": "How can you verify communication between ESP-01 and MCU?",
                "options": ["A) By checking the voltage", "B) By using a serial monitor", "C) By using a multimeter", "D) By observing LED indicators"],
                "answer": "B"
            },
            {
                "question": "What is the voltage required for the ESP-01 module?",
                "options": ["A) 5V", "B) 3.3V", "C) 1.8V", "D) 12V"],
                "answer": "B"
            },
            {
                "question": "What should you do if the ESP-01 module is not responding?",
                "options": ["A) Check the power connections", "B) Verify the baud rate", "C) Check the TX/RX connections", "D) All of the above"],
                "answer": "D"
            },
            {
                "question": "Which sensor is commonly used for temperature and humidity measurements?",
                "options": ["A) BMP180", "B) DHT11", "C) MPU6050", "D) MQ-135"],
                "answer": "B"
            },
            {
                "question": "Why is it important to use a common ground between ESP-01 and MCU?",
                "options": ["A) For consistent voltage levels", "B) For reliable communication", "C) To prevent noise", "D) All of the above"],
                "answer": "D"
            }
        ]

    def slow_print(self, text, color=Fore.WHITE, delay=0.05):
        for char in text:
            print(color + char, end='', flush=True)
            time.sleep(delay)
        print(Style.RESET_ALL)

    def pause(self):
        input("\nPress Enter to continue...")

    def guide_user(self):
        self.slow_print("Welcome to the Temperature and Humidity Monitoring System Guide!", Fore.CYAN)
        self.slow_print("Here are the basic steps to set up your system:\n", Fore.CYAN)
        for step in self.steps:
            self.slow_print(step, Fore.GREEN)
        self.pause()
        self.slow_print("\nDetailed Instructions:\n", Fore.CYAN)
        self.detailed_steps()

        self.slow_print("\nProtocols to follow:\n", Fore.YELLOW)
        for protocol in self.protocols:
            self.slow_print(protocol, Fore.YELLOW)
        self.pause()

        self.slow_print("\nPrinciples to keep in mind:\n", Fore.MAGENTA)
        for principle in self.principles:
            self.slow_print(principle, Fore.MAGENTA)
        self.pause()

    def detailed_steps(self):
        self.slow_print("\nStep 1: Gather Components", Fore.GREEN)
        self.slow_print("You will need the following components:")
        components = [
            "- ESP-01 module (ESP8266)",
            "- 8-bit MCU (e.g., AVR like ATmega328P, PIC like PIC16F877A, ARM like STM32F103, RISC-V like GD32VF103)",
            "- Temperature and Humidity Sensor (e.g., DHT11, DHT22)",
            "- Breadboard and Jumper wires",
            "- Power supply (3.3V for ESP-01 and appropriate supply for MCU)",
            "- USB-to-Serial adapter for programming ESP-01",
            "- Resistors (10kΩ for pull-up, others as needed)",
            "- Capacitors (decoupling capacitors, if necessary)"
        ]
        for component in components:
            self.slow_print(component)
        self.pause()

        self.slow_print("\nStep 2: Set Up ESP-01 Module", Fore.GREEN)
        instructions = [
            "1. Connect the ESP-01 module to the USB-to-Serial adapter.",
            "   - GPIO0 to GND (for programming mode)",
            "   - TX of ESP-01 to RX of adapter",
            "   - RX of ESP-01 to TX of adapter",
            "   - VCC to 3.3V",
            "   - GND to GND",
            "2. Open your Arduino IDE or any other suitable software for programming.",
            "3. Load the appropriate firmware or program for your ESP-01 module.",
            "   - Example: ESP8266 basic example sketches for testing connectivity",
            "4. Verify and upload the code to the ESP-01 module.",
            "5. Disconnect GPIO0 from GND after programming to run the code."
        ]
        for instruction in instructions:
            self.slow_print(instruction)
        self.pause()

        self.slow_print("\nStep 3: Interface with 8-bit MCU", Fore.GREEN)
        instructions = [
            "1. Connect the TX pin of the ESP-01 to the RX pin of the MCU.",
            "2. Connect the RX pin of the ESP-01 to the TX pin of the MCU.",
            "3. Ensure common ground between ESP-01 and MCU.",
            "4. Connect VCC and GND of ESP-01 to 3.3V and GND of power supply.",
            "5. Add level shifters if your MCU operates at 5V logic."
        ]
        for instruction in instructions:
            self.slow_print(instruction)
        self.pause()

        self.slow_print("\nStep 4: Connect Temperature and Humidity Sensor", Fore.GREEN)
        instructions = [
            "1. Connect the VCC and GND of the sensor to the power supply.",
            "2. Connect the data pin of the sensor to one of the MCU's GPIO pins.",
            "3. Add a pull-up resistor (10kΩ) between the data pin and VCC if required by the sensor.",
            "4. Verify the sensor's datasheet for proper connections and requirements."
        ]
        for instruction in instructions:
            self.slow_print(instruction)
        self.pause()

        self.slow_print("\nStep 5: Program the MCU", Fore.GREEN)
        instructions = [
            "1. Open your preferred IDE for the MCU (e.g., MPLAB for PIC, Atmel Studio for AVR).",
            "2. Write or load a program to read data from the sensor and send it to the ESP-01 module.",
            "   - Example: Read temperature and humidity, send via UART to ESP-01",
            "3. Compile and upload the program to the MCU.",
            "4. Debug and test the program with a serial monitor to ensure proper data acquisition."
        ]
        code_example = """
        // Example code for AVR (ATmega328P) using Arduino IDE
        #include <DHT.h>
        #define DHTPIN 2
        #define DHTTYPE DHT11
        DHT dht(DHTPIN, DHTTYPE);

        void setup() {
            Serial.begin(9600);
            dht.begin();
        }

        void loop() {
            float h = dht.readHumidity();
            float t = dht.readTemperature();
            if (isnan(h) || isnan(t)) {
                Serial.println("Failed to read from DHT sensor!");
                return;
            }
            Serial.print("Humidity: ");
            Serial.print(h);
            Serial.print(" %\t");
            Serial.print("Temperature: ");
            Serial.print(t);
            Serial.println(" *C ");
            delay(2000);
        }
        """
        self.slow_print(code_example, Fore.CYAN)
        self.pause()

        self.slow_print("\nStep 6: Establish Communication Between ESP-01 and MCU", Fore.GREEN)
        instructions = [
            "1. Ensure that both the ESP-01 and MCU are correctly programmed.",
            "2. Verify the baud rate settings for serial communication.",
            "3. Test sending data from MCU to ESP-01 and vice versa.",
            "   - Example: Use AT commands to test ESP-01 responses",
            "4. Implement error-checking mechanisms to ensure reliable data transmission."
        ]
        code_example = """
        // Example code for ESP-01 (ESP8266) using Arduino IDE
        void setup() {
            Serial.begin(9600);
        }

        void loop() {
            if (Serial.available()) {
                String data = Serial.readString();
                Serial.print("Received: ");
                Serial.println(data);
            }
        }
        """
        self.slow_print(code_example, Fore.CYAN)
        for instruction in instructions:
            self.slow_print(instruction)
        self.pause()

        self.slow_print("\nStep 7: Test the System", Fore.GREEN)
        instructions = [
            "1. Power up the entire system and monitor the initial responses.",
            "2. Use a serial monitor to observe the data sent by the MCU and received by the ESP-01.",
            "3. Check the readings from the temperature and humidity sensor for accuracy.",
            "4. Verify that the data is correctly being transmitted to your desired endpoint (e.g., cloud service, local server).",
            "5. Troubleshoot any issues by checking connections, code, and configurations."
        ]
        for instruction in instructions:
            self.slow_print(instruction)
        self.pause()

    def take_quiz(self):
        self.slow_print("Temperature and Humidity Monitoring System Quiz", Fore.CYAN)
        correct_answers = 0
        for question in self.quiz_questions:
            self.slow_print("\n" + question["question"], Fore.BLUE)
            for option in question["options"]:
                self.slow_print(option, Fore.BLUE)
            answer = input("Your answer: ").strip().upper()
            if answer == question["answer"]:
                self.slow_print("Correct!", Fore.GREEN)
                correct_answers += 1
            else:
                self.slow_print(f"Incorrect! The correct answer was {question['answer']}.", Fore.RED)
        self.slow_print(f"\nYou got {correct_answers} out of {len(self.quiz_questions)} correct!", Fore.CYAN)

    def interactive_practice(self):
        self.slow_print("Interactive Practice Section", Fore.CYAN)
        self.slow_print("Follow the steps and confirm each step before proceeding.\n", Fore.CYAN)
        
        practice_steps = [
            ("Step 1: Gather Components", "You will need the following components:\n"
                                         "- ESP-01 module (ESP8266)\n"
                                         "- 8-bit MCU (e.g., AVR like ATmega328P, PIC like PIC16F877A, ARM like STM32F103, RISC-V like GD32VF103)\n"
                                         "- Temperature and Humidity Sensor (e.g., DHT11, DHT22)\n"
                                         "- Breadboard and Jumper wires\n"
                                         "- Power supply (3.3V for ESP-01 and appropriate supply for MCU)\n"
                                         "- USB-to-Serial adapter for programming ESP-01\n"
                                         "- Resistors (10kΩ for pull-up, others as needed)\n"
                                         "- Capacitors (decoupling capacitors, if necessary)"),
            ("Step 2: Set Up ESP-01 Module", "1. Connect the ESP-01 module to the USB-to-Serial adapter.\n"
                                            "   - GPIO0 to GND (for programming mode)\n"
                                            "   - TX of ESP-01 to RX of adapter\n"
                                            "   - RX of ESP-01 to TX of adapter\n"
                                            "   - VCC to 3.3V\n"
                                            "   - GND to GND\n"
                                            "2. Open your Arduino IDE or any other suitable software for programming.\n"
                                            "3. Load the appropriate firmware or program for your ESP-01 module.\n"
                                            "   - Example: ESP8266 basic example sketches for testing connectivity\n"
                                            "4. Verify and upload the code to the ESP-01 module.\n"
                                            "5. Disconnect GPIO0 from GND after programming to run the code."),
            ("Step 3: Interface with 8-bit MCU", "1. Connect the TX pin of the ESP-01 to the RX pin of the MCU.\n"
                                                "2. Connect the RX pin of the ESP-01 to the TX pin of the MCU.\n"
                                                "3. Ensure common ground between ESP-01 and MCU.\n"
                                                "4. Connect VCC and GND of ESP-01 to 3.3V and GND of power supply.\n"
                                                "5. Add level shifters if your MCU operates at 5V logic."),
            ("Step 4: Connect Temperature and Humidity Sensor", "1. Connect the VCC and GND of the sensor to the power supply.\n"
                                                                "2. Connect the data pin of the sensor to one of the MCU's GPIO pins.\n"
                                                                "3. Add a pull-up resistor (10kΩ) between the data pin and VCC if required by the sensor.\n"
                                                                "4. Verify the sensor's datasheet for proper connections and requirements."),
            ("Step 5: Program the MCU", "1. Open your preferred IDE for the MCU (e.g., MPLAB for PIC, Atmel Studio for AVR).\n"
                                        "2. Write or load a program to read data from the sensor and send it to the ESP-01 module.\n"
                                        "   - Example: Read temperature and humidity, send via UART to ESP-01\n"
                                        "3. Compile and upload the program to the MCU.\n"
                                        "4. Debug and test the program with a serial monitor to ensure proper data acquisition.\n"
                                        "Code Example:\n"
                                        "// Example code for AVR (ATmega328P) using Arduino IDE\n"
                                        "#include <DHT.h>\n"
                                        "#define DHTPIN 2\n"
                                        "#define DHTTYPE DHT11\n"
                                        "DHT dht(DHTPIN, DHTTYPE);\n\n"
                                        "void setup() {\n"
                                        "    Serial.begin(9600);\n"
                                        "    dht.begin();\n"
                                        "}\n\n"
                                        "void loop() {\n"
                                        "    float h = dht.readHumidity();\n"
                                        "    float t = dht.readTemperature();\n"
                                        "    if (isnan(h) || isnan(t)) {\n"
                                        "        Serial.println(\"Failed to read from DHT sensor!\");\n"
                                        "        return;\n"
                                        "    }\n"
                                        "    Serial.print(\"Humidity: \");\n"
                                        "    Serial.print(h);\n"
                                        "    Serial.print(\" %\t\");\n"
                                        "    Serial.print(\"Temperature: \");\n"
                                        "    Serial.print(t);\n"
                                        "    Serial.println(\" *C \");\n"
                                        "    delay(2000);\n"
                                        "}"),
            ("Step 6: Establish Communication Between ESP-01 and MCU", "1. Ensure that both the ESP-01 and MCU are correctly programmed.\n"
                                                                    "2. Verify the baud rate settings for serial communication.\n"
                                                                    "3. Test sending data from MCU to ESP-01 and vice versa.\n"
                                                                    "   - Example: Use AT commands to test ESP-01 responses\n"
                                                                    "4. Implement error-checking mechanisms to ensure reliable data transmission.\n"
                                                                    "Code Example:\n"
                                                                    "// Example code for ESP-01 (ESP8266) using Arduino IDE\n"
                                                                    "void setup() {\n"
                                                                    "    Serial.begin(9600);\n"
                                                                    "}\n\n"
                                                                    "void loop() {\n"
                                                                    "    if (Serial.available()) {\n"
                                                                    "        String data = Serial.readString();\n"
                                                                    "        Serial.print(\"Received: \");\n"
                                                                    "        Serial.println(data);\n"
                                                                    "    }\n"
                                                                    "}"),
            ("Step 7: Test the System", "1. Power up the entire system and monitor the initial responses.\n"
                                        "2. Use a serial monitor to observe the data sent by the MCU and received by the ESP-01.\n"
                                        "3. Check the readings from the temperature and humidity sensor for accuracy.\n"
                                        "4. Verify that the data is correctly being transmitted to your desired endpoint (e.g., cloud service, local server).\n"
                                        "5. Troubleshoot any issues by checking connections, code, and configurations.")
        ]

        for title, detail in practice_steps:
            self.slow_print(title, Fore.GREEN)
            self.slow_print(detail, Fore.WHITE)
            completed = input("Have you completed this step? (yes/no): ").strip().lower()
            if completed == 'yes':
                self.slow_print("Great! Moving to the next step.", Fore.GREEN)
            else:
                self.slow_print("Please complete the step before proceeding.", Fore.RED)
                self.pause()
            self.pause()

        self.slow_print("Practice section completed. Good job!", Fore.CYAN)

def main():
    print (Fore.BLUE + """
____               __  __               __
   / __ \___ _   __   / / / /__  ____ _____/ /
  / / / / _ \ | / /  / /_/ / _ \/ __ `/ __  / 
 / /_/ /  __/ |/ /  / __  /  __/ /_/ / /_/ /  
/_____/\___/|___/  /_/ /_/\___/\__,_/\__,_/   
                                              
""" + Style.RESET_ALL +"\n"   +                  Fore.RED + "Enthernetcode")
    system = TemperatureHumidityMonitoringSystem()
    while True:
        print(Fore.CYAN + "\nMain Menu:" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Guide" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Quiz" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Interactive Practice" + Style.RESET_ALL)
        print(Fore.RED + "4. Exit" + Style.RESET_ALL)
        choice = input(Fore.CYAN + "Please select an option (1-4): " + Style.RESET_ALL).strip()
        
        if choice == '1':
            system.guide_user()
        elif choice == '2':
            system.take_quiz()
        elif choice == '3':
            system.interactive_practice()
        elif choice == '4':
            system.slow_print("Exiting the program. Goodbye!", Fore.CYAN)
            break
        else:
            system.slow_print("Invalid choice. Please try again.", Fore.RED)

if __name__ == "__main__":
    main()
