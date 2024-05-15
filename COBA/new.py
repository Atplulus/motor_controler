import Jetson.GPIO as GPIO 

MOTOR_PINS = {
    'MOTOR_A': {
        'ENA': 33,
        'IN1': 35,
        'IN2': 37
    },
    'MOTOR_B': {
        'ENB': 32,
        'IN3': 40,
        'IN4': 38
    },
    # Add more motors as needed
}
GPIO.setmode(GPIO.BOARD)
def setup_motor_pins():
    for motor, pins in MOTOR_PINS.items():
        for pin in pins.values():
            GPIO.setup(pin, GPIO.OUT)

# Define a function to move forward with 100% duty cycle
def move_forward():
    # Set motor A pins
    GPIO.output(MOTOR_PINS['MOTOR_A']['IN1'], GPIO.HIGH)
    GPIO.output(MOTOR_PINS['MOTOR_A']['IN2'], GPIO.LOW)
    # Set motor B pins
    GPIO.output(MOTOR_PINS['MOTOR_B']['IN3'], GPIO.HIGH)
    GPIO.output(MOTOR_PINS['MOTOR_B']['IN4'], GPIO.LOW)
    # Set motor speed to 100% duty cycle
    GPIO.output(MOTOR_PINS['MOTOR_A']['ENA'], GPIO.HIGH)
    GPIO.output(MOTOR_PINS['MOTOR_B']['ENB'], GPIO.HIGH)

# Set up motor pins
setup_motor_pins()

# Move forward with 100% duty cycle
move_forward()
GPIO.cleanup()