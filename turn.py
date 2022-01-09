import Adafruit_PCA9685
import time
import sys

servo_min = 180  # Min pulse length out of 4096
servo_max = 400 # Max pulse length out of 4096
servo = 2
pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm.set_pwm_freq(50)

def turn_left():
    pwm.set_pwm(servo, 0, servo_min)
    print(servo_min)

def turn_right():
    pwm.set_pwm(servo, 0, servo_max)
    print(servo_max)

def straight():
    pwm.set_pwm(servo, 0, 300)
    print(servo_max)
