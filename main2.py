#!/usr/bin/env python

import Jetson.GPIO as GPIO
import time

# For 1st Motor on ENA
ENA = 32
IN1 = 35
IN2 = 37

# For 2nd Motor on ENB
ENB = 33
IN3 = 40
IN4 = 38


# Set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# Initialize EnA, In1, In2, EnB, In3, In4
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.HIGH)

try:
    # Stop
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(10) 
    
    i = 20 
    
    for i in range(0,100,1):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)  
        time.sleep(0.07)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)  
        time.sleep(0.03)
    # Stop
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)

    # Backward
    #GPIO.output(IN1, GPIO.LOW)
    #GPIO.output(IN2, GPIO.HIGH)
    #GPIO.output(IN3, GPIO.LOW)
    #GPIO.output(IN4, GPIO.HIGH)
    #time.sleep(1)

    # Stop
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(ENB, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)

finally:
    GPIO.cleanup()
