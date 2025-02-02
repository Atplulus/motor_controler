import Jetson.GPIO as GPIO
import time
from serial import Serial

# Set GPIO pins for motor control
ENA = 33
IN1 = 35
IN2 = 37
ENB = 32
IN3 = 40
IN4 = 38

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup([ENA, IN1, IN2, ENB, IN3, IN4], GPIO.OUT)

# Set direction of motors to forward
def set_motor_direction(direction):
    if direction == "forward":
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
    elif direction == "backward":
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
    elif direction == "stop":
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)

# Initialize Serial Port for RFID
rfid_serial = Serial('/dev/ttyUSB0', 115200, timeout=0.1)

# Function to send RFID command and read response
def send_rfid_cmd(cmd):
    data = bytes.fromhex(cmd)
    rfid_serial.write(data)
    response = rfid_serial.read(512)
    response_hex = response.hex().upper()
    hex_list = [response_hex[i:i+2] for i in range(0, len(response_hex), 2)]
    hex_space = ' '.join(hex_list)
    return hex_space

# Initial speed before detecting any tag
last_speed = 100

try:
    while True:
        # Read RFID tag
        tag_data = send_rfid_cmd('BB 00 22 00 00 22 7E')
        # Convert RFID response to detected tag
        if '6C DC B9 33' in tag_data:  # Tag 1
            last_speed = 30
        elif '88 DD 43 D1' in tag_data:  # Tag 2
            last_speed = 10
        elif 'E8 DC 42 5E' in tag_data:  # Tag 3
            last_speed = 0
        
        # Set the motor speed and direction
        if last_speed > 0:
            set_motor_direction("forward")
            # Set motor speed using PWM (adjust duty cycle based on last_speed)
            pwm_ena = GPIO.PWM(ENA, 100)  # Initialize PWM on ENA pin at 100Hz frequency
            pwm_enb = GPIO.PWM(ENB, 100)  # Initialize PWM on ENB pin at 100Hz frequency
            pwm_ena.start(last_speed)  # Start PWM with last_speed
            pwm_enb.start(last_speed)  # Start PWM with last_speed
        else:
            set_motor_direction("stop")

except KeyboardInterrupt:
    # Clean up GPIO pins when the program stops
    GPIO.cleanup()
