import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [8,23,24,25,8,7,12,16] 

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)


SleepTimeL =1
EngineSleepTimeL = 0.6

try:

	while True:
		varRelay = input('Please enter a number between 1-8 : ') 
		varCommand = raw_input('Please enter Command : ').lower().split(' ')
		print "Command received ..." , varCommand[0]
		if varCommand[0] == "on":
			print "Turning ON ..." , varRelay
			GPIO.output(int(varRelay),GPIO.LOW)
			print "Turning ON ..." + str(varRelay) + ".... OK"
		elif varCommand[0] == "engine": 
			print "Turning ON ... Short Burst " , varRelay
			GPIO.output(int(varRelay),GPIO.LOW)
			time.sleep(EngineSleepTimeL);
			GPIO.output(int(varRelay),GPIO.HIGH)
			print "Turning OFF ... EngineSleepTimeL " + str(varRelay) + ".... OK"
		else : 
			print "Turning OFF ..." , varRelay
			GPIO.output(int(varRelay),GPIO.HIGH)
			print "Turning OFF ..." + str(varRelay) + ".... OK"

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()
