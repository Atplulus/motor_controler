import Jetson.GPIO as GPIO
import time
from serial import Serial

# Define Jetson Nano pins
ENA = 33
IN1 = 35
IN2 = 37
ENB = 32
IN3 = 40
IN4 = 38

# Initialize GPIO
def initialize_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([ENA, IN1, IN2, ENB, IN3, IN4], GPIO.OUT)

# Initialize Serial Port for RFID
def initialize_serial():
    try:
        return Serial('/dev/ttyUSB0', 115200, timeout=0.1)
    except Exception as e:
        print("Error initializing serial port:", e)
        return None

# Function to send RFID command and read response
def send_rfid_cmd(serial_port, cmd):
    try:
        if serial_port is not None and serial_port.is_open:
            data = bytes.fromhex(cmd)
            serial_port.write(data)
            response = serial_port.read(512)
            if response:
                response_hex = response.hex().upper()
                hex_list = [response_hex[i:i+2] for i in range(0, len(response_hex), 2)]
                hex_space = ' '.join(hex_list)
                return hex_space
            else:
                return None
    except Exception as e:
        print("Error sending RFID command:", e)
        return None

# Function to set motor speed using PWM
def set_motor_speed_pwm(speed):
    # Ensure speed value is within range 0 to 100
    speed = max(0, min(100, speed))

    # Set motor A speed
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

    # Set motor B speed
    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    # Simulate PWM by toggling GPIO pins
    pwm_period = 0.01  # PWM period in seconds (adjust as needed)
    pwm_value = speed / 100.0

    # Calculate ON and OFF times
    on_time = pwm_period * pwm_value
    off_time = pwm_period * (1 - pwm_value)

    # Set GPIO pins
    while True:
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(ENB, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(ENA, GPIO.LOW)
        GPIO.output(ENB, GPIO.LOW)
        time.sleep(off_time)

# Function to set initial motor speed without PWM
def set_initial_motor_speed(speed):
    # Ensure speed value is within range 0 to 100
    speed = max(0, min(100, speed))

    # Set motor A speed
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH if speed > 0 else GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

    # Set motor B speed
    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH if speed > 0 else GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Main function
def main():
    try:
        initialize_gpio()
        rfid_serial = initialize_serial()
        if rfid_serial is None:
            return

        # Set initial motor speed without PWM
        set_initial_motor_speed(100)

        while True:
            # Read RFID tag
            tag_data = send_rfid_cmd(rfid_serial, 'BB 00 22 00 00 22 7E')
            if tag_data:
                # Convert RFID response to detected tag
                print("RFID tag data:", tag_data)  # Added for debugging
                if '6C DC B9 33' in tag_data:  # Tag 1
                    print("Tag 1 detected")
                    set_motor_speed_pwm(70)
                elif '88 DD 43 D1' in tag_data:  # Tag 2
                    print("Tag 2 detected")
                    set_motor_speed_pwm(30)
                elif 'E8 DC 42 5E' in tag_data:  # Tag 3
                    print("Tag 3 detected")
                    set_initial_motor_speed(0)
            time.sleep(0.1)  # Wait for 0.1 second before reading RFID again
    except KeyboardInterrupt:
        # Clean up GPIO when program is terminated
        GPIO.cleanup()
    except Exception as e:
        print("An error occurred:", e)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
