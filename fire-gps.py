import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase

firebase = firebase.FirebaseApplication('https://YOUR_FIREBASE_URL.firebaseio.com/', None)
#firebase.put("/dht", "/temp", "0.00")
#firebase.put("/dht", "/humidity", "0.00")

def update_firebase():

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		sleep(5)
		str_temp = ' {0:0.2f} *C '.format(temperature)	
		str_hum  = ' {0:0.2f} %'.format(humidity)
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))	
			
	else:
		print('Failed to get reading. Try again!')	
		sleep(10)

	data = {"temp": temperature, "humidity": humidity}
	firebase.post('/sensor/dht', data)
	

while True:
		update_firebase()
		
        #sleepTime = int(sleepTime)
		sleep(5)
