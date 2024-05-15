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

# Create PWM objects
pwm_motorA = GPIO.PWM(ENA, 100)  # PWM frequency 100 Hz
pwm_motorB = GPIO.PWM(ENB, 100)

# Start PWM
pwm_motorA.start(0)  # Duty cycle: 0 (off)
pwm_motorB.start(0)

# Function to set motor speed
def set_motor_speed(speed):
    # Ensure speed value is within range -100 to 100
    speed = max(-100, min(100, speed))

    # Determine direction based on speed sign
    if speed > 0:
        # Forward direction
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
    elif speed < 0:
        # Reverse direction
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
    else:
        # Stop
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)

    # Set PWM duty cycle
    pwm_motorA.ChangeDutyCycle(abs(speed))
    pwm_motorB.ChangeDutyCycle(abs(speed))

# Main function
def main():
    try:
        while True:
            # Set motor speed to 50 for 3 seconds
            set_motor_speed(50)
            time.sleep(3)

            # Set motor speed to 20 for 5 seconds
            set_motor_speed(20)
            time.sleep(5)
    except KeyboardInterrupt:
        # Clean up GPIO when program is terminated
        pwm_motorA.stop()
        pwm_motorB.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
