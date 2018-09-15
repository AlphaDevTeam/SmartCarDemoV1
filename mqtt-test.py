import time
import serial

recipient = "+94777117477"
message = "Hello, World!"

phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=5.0)
try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CREG?\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CGATT=1\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CSTT=default\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CIICR\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CIFSR\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CIPSTART="TCP","35.198.207.43","1883"\r')
    rcv = phone.read(10)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write("\x1A\r\n")
finally:
    phone.close()
    
