import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [14,15,18,23,24] 

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)


SleepTimeL =2
EngineStartupDelay = 1

try:

  for i in pinList:
    if i == 24:
	print "Engine ON Singal..." , i
	GPIO.output(int(i),GPIO.LOW)
	time.sleep(EngineStartupDelay);
	print "Engine ON Signal..." + str(i) + ".... OK"
	print "Engine ON Signal Cutoff..." , i
	GPIO.output(int(i),GPIO.HIGH)
	time.sleep(EngineStartupDelay);
	print "Engine ON Signal Cutoff..." + str(i) + ".... OK"
    else:
	print "Turning ON ..." , i
	GPIO.output(int(i),GPIO.LOW)
	time.sleep(SleepTimeL);
	print "Turning ON ..." + str(i) + ".... OK"
 
  while True:
		varRelay = input('Please enter a number between 1-8 : ') 
		varCommand = raw_input('Please enter Command : ').lower().split(' ')
		print "Command received ..." , varCommand[0]
		if varCommand[0] == "on":
			print "Turning ON ..." , varRelay
			GPIO.output(int(varRelay),GPIO.LOW)
			print "Turning ON ..." + str(varRelay) + ".... OK"
		else: 
			print "Turning OFF ..." , varRelay
			GPIO.output(int(varRelay),GPIO.HIGH)
			print "Turning OFF ..." + str(varRelay) + ".... OK"
		  	time.sleep(SleepTimeL);

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()
