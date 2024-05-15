#!/usr/bin/env python

import Jetson.GPIO as GPIO
import time

# Define pin numbers
ENA = 32
IN1 = 35
IN2 = 37
ENB = 33
IN3 = 40
IN4 = 38

# Set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

try:
    # Initialize pins
    for pin in [ENA, IN1, IN2, ENB, IN3, IN4]:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    # Function to control motor speed
    def set_motor_speed(speed):
        # Adjust sleep time based on speed le 
        if speed == 1:# Fast speied
            print('kecepatan :  ',speed)
            delay = 0.01
        elif speed == 2: ) # Medium speed
            print('kecepatan :  ',speed) 
            delay = 0.02
        elif speed == 3:  # Slow speed
            print('kecepatan :  ',speed)
            delay = 0.03
        else:  # Default to medium speed
            delay = 1
        
        # Move motors
        for _ in range(100):
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)
            time.sleep(delay)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            time.sleep(delay)

    # Start motors at maximum speed
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)
    set_motor_speed(1)  # Fast speed
    
    # Move motors with different speeds
    set_motor_speed(2)  # Medium speed
    set_motor_speed(3)  # Slow speed

    # Stop motors
    GPIO.output(ENA,GPIO.HIGH)
    GPIO.output(ENB, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)                                                        
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)

finally:
    # Clean up GPIO
    GPIO.cleanup()
