import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [14,15,18,23,24,25,8]

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)


SleepTimeL =2

try:

	GPIO.output(14,GPIO.LOW)
	print "one"
	time.sleep(SleepTimeL);

	GPIO.output(14,GPIO.HIGH)
        print "one closed"
        time.sleep(SleepTimeL);
	
	GPIO.output(15,GPIO.LOW)
        print "15 closed"
        time.sleep(SleepTimeL);

	GPIO.output(18,GPIO.LOW)
	print "15 closed"
	time.sleep(SleepTimeL);

	GPIO.output(23,GPIO.LOW)
        print "15 closed"
        time.sleep(SleepTimeL);

	GPIO.output(24,GPIO.LOW)
        print "15 closed"
        time.sleep(SleepTimeL);


except KeyboardInterrupt:
	print "Quit"

GPIO.cleanup()
