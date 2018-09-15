import serial
import time
phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=5.0)
try:
    time.sleep(1)
    phone.write(b'AT\r')
    rcv = phone.read(10)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(1)
    
finally:
    phone.close()
