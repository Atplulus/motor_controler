import Jetson.GPIO as GPIO
import time

# Define Jetson Nano pins
ENA = 33
IN1 = 35
IN2 = 37
ENB = 32
IN3 = 40
IN4 = 38

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to set motor speed
def set_motor_speed(speed):
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
    pwm_period = 0.1  # PWM period in seconds (adjust as needed)
    pwm_value = speed / 100.0

    while True:
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(ENB, GPIO.HIGH)
        time.sleep(pwm_period * pwm_value)

        GPIO.output(ENA, GPIO.LOW)
        GPIO.output(ENB, GPIO.LOW)
        time.sleep(pwm_period * (1 - pwm_value))

# Main function
def main():
    try:
        while True:
            # Set motor speed to 50% for 1 second
            #set_motor_speed(50)
            #time.sleep(5)

            # Set motor speed to 75% for 1 second
            #set_motor_speed(75)
            #time.sleep(5)

            # Set motor speed to 25% for 1 second
            set_motor_speed(10)
            time.sleep(1)
    except KeyboardInterrupt:
        # Clean up GPIO when program is terminated
        GPIO.cleanup()

if __name__ == "__main__":
    main()
