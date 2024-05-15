import Jetson.GPIO as GPIO
import time

# Definisikan pin
ENA = 32
IN1 = 35
IN2 = 37
ENB = 33
IN3 = 40
IN4 = 38

# Atur mode GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Inisialisasi PWM
pwm_motorA = GPIO.PWM(ENA, 100) # Frekuensi PWM 1000 Hz
pwm_motorB = GPIO.PWM(ENB, 100)

# Mulai PWM dengan duty cycle 30%
pwm_motorA.start(5)
pwm_motorB.start(5)

# Majukan motor A
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

# Majukan motor B
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

# Tunggu selama 5 detik
time.sleep(5)

# Berhenti PWM
pwm_motorA.stop()
pwm_motorB.stop()

# Matikan motor
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)

# Cleanup GPIO
GPIO.cleanup()
