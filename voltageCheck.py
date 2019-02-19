import RPi.GPIO as GPIO
import time
import obd

GPIO.setmode(GPIO.BCM)

pinList = [18,23,24,25,8,7,12,16]
obdCommandList = [18,23,24,25,8,7,12,16] 

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


defaultDelay = 0.5
engineStartupDelay = 0.7

def switchDoorSensor(command):
	if command == "default":
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
	time.sleep(1.5);
	executeCommand(16,"short")
	time.sleep(1.5);
	executeCommand(23,"on")
	switchDoorSensor("default")
	print "Engine Startup...... [DONE]"

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
		GPIO.output(int(pin),GPIO.HIGH)
		time.sleep(int(defaultDelay));
		print "Sending OFF Signal..." + str(pin) + ".... OK"

def getOBDData():
	print "========= GETTING OBD DATA ==========="
  executeCommand(12,"on")
  connection = obd.OBD("/dev/rfcomm0")
	cmdList = obd.commands.PIDS_C 
	cmd = obd.commands.RPM # select an OBD command (sensor)
	cmdVoltage = obd.commands.CONTROL_MODULE_VOLTAGE
	responseList = connection.query(cmdList)
	response = connection.query(cmd) # send the command, and parse the response
	responseVoltage = connection.query(cmdVoltage)
	print(response.value) # returns unit-bearing values thanks to Pint
	print(responseList.value)
	print(responseVoltage.value)
  executeCommand(12,"on")
	print "========= END OF OBD DATA ==========="

try:
		getOBDData()
    
except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()
