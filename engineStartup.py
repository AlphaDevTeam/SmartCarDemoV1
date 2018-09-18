import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [18,23,24,25,8,7,12,16] 

#24-25 - Manual / Auto Door Sensor Switcher
#8 - Lock Open
#7 - Lock Close
#12 - Ignition 
#18 - Accesories
#23 - Blower
#16 - Engine Start

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)


defaultDelay = 1
engineStartupDelay = 0.7

def switchDoorSensor(command):
	if command == "manual":
		executeCommand(24,"off")
		executeCommand(25,"off")
	elif command == "auto":
		executeCommand(24,"on")
		executeCommand(25,"on")
	
def openLock():
	executeCommand(8,"short")

def closeLock():
	executeCommand(7,"short")
	
def initiateRemoteStart():
	switchDoorSensor("auto")
	closeLock()
	executeCommand(12,"on")
	executeCommand(18,"on")
	executeCommand(16,"short")
	executeCommand(23,"on")
	switchDoorSensor("manual")
  
  

def executeCommand(pin,command):
	print(command + " Received")
	if command == "on":
		print "Sending ON Singal..." , pin
		GPIO.output(int(pin),GPIO.LOW)
		time.sleep(int(defaultDelay));
		print "Sending ON Signal..." + str(pin) + ".... OK"
	elif command =="short":
		print "Sending Short Burst " , pin
		GPIO.output(int(pin),GPIO.LOW)
		time.sleep(engineStartupDelay);
		GPIO.output(int(pin),GPIO.HIGH)
		print "Sending Short Burst " + str(pin) + ".... OK"
	else :
		print "Sending OFF Singal..." , pin
		GPIO.output(int(pin),GPIO.LOW)
		time.sleep(int(defaultDelay));
		print "Sending OFF Signal..." + str(pin) + ".... OK"
	

try:
	
	initiateRemoteStart()
	
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
