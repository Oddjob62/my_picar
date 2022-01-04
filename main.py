import Adafruit_PCA9685
import time

while 1:
	for i in range(0,100):
		pwm.set_pwm(0, 0, (300+i))
		time.sleep(0.05)
	for i in range(0,100):
		pwm.set_pwm(0, 0, (400-i))
		time.sleep(0.05)
