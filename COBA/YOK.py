import Jetson.GPIO as GPIO
import time

# Pin configurations
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

class MotorController:
    def __init__(self, motor_name):
        self.motor_name = motor_name
        self.pins = MOTOR_PINS[motor_name]
        self.setup_pins()

    def setup_pins(self):
        # Set up the GPIO pins as outputs
        for pin in self.pins.values():
            GPIO.setup(pin, GPIO.OUT)

    def set_speed(self, speed):
        # Set the speed of the motor using PWM for more precise control
        if self.motor_name == 'MOTOR_A':
            GPIO.output(self.pins['ENA'], GPIO.HIGH if speed > 0 else GPIO.LOW)
        elif self.motor_name == 'MOTOR_B':
            GPIO.output(self.pins['ENB'], GPIO.HIGH if speed > 0 else GPIO.LOW)
        print(f"{self.motor_name} speed set to {speed}%")

    def forward(self):
        # Set the direction of the motor using the IN1/IN2 pins
        if self.motor_name == 'MOTOR_A':
            GPIO.output(self.pins['IN1'], GPIO.HIGH)
            GPIO.output(self.pins['IN2'], GPIO.LOW)
        elif self.motor_name == 'MOTOR_B':
            GPIO.output(self.pins['IN3'], GPIO.HIGH)
            GPIO.output(self.pins['IN4'], GPIO.LOW)
        print(f"{self.motor_name} moving forward")

    def stop(self):
        # Stop the motor
        if self.motor_name == 'MOTOR_A':
            GPIO.output(self.pins['ENA'], GPIO.LOW)
        elif self.motor_name == 'MOTOR_B':
            GPIO.output(self.pins['ENB'], GPIO.LOW)
        print(f"{self.motor_name} stopped")

# Initialize the GPIO library
GPIO.setmode(GPIO.BOARD)

# Create motor controllers
motor_a = MotorController('MOTOR_A')
motor_b = MotorController('MOTOR_B')

# Example usage
try:
    motor_a.set_speed(100)  # Set speed to 100%
    motor_a.forward()  # Move forward
    time.sleep(2)  # Wait for 2 seconds
    motor_a.stop()  # Stop the motor

    motor_b.set_speed(100)  # Set speed to 100%
    motor_b.forward()  # Move forward
    time.sleep(2)  # Wait for 2 seconds
    motor_b.stop()  # Stop the motor

finally:
    # Clean up GPIO
    GPIO.cleanup()
