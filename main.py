import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm.set_pwm_freq(50)

while 1:
	for i in range(0,100):
		pwm.set_pwm(0, 0, (300+i))
		time.sleep(0.05)
	for i in range(0,100):
		pwm.set_pwm(0, 0, (400-i))
		time.sleep(0.05)
