import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [14,15,18,23,24,25,8]

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)


SleepTimeL =1

try:

	varRelay = input('Please enter a number between 1-8') 
	varCommand = input('Please enter Command')
	if varCommand == "ON":
		print "Turning ON ..." + varRelay
		GPIO.output(varRelay,GPIO.LOW)
		print "Turning ON ..." + varRelay + ".... OK"
	else: 
		print "Turning OFF ..." + varRelay
		GPIO.output(varRelay,GPIO.HIGH)
		print "Turning OFF ..." + varRelay + ".... OK"
	time.sleep(SleepTimeL);

except KeyboardInterrupt:
	print "Quit"

GPIO.cleanup()
