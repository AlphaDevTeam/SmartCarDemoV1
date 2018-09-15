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
    phone.write(b'AT+CIPSTART=TCP,35.198.207.43,1883\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(b'AT+CIPSEND\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write(serial.to_bytes([0x10,0x12,0x0,0x4,0x4D,0x51,0x54,0x54,0x4,0x2,0x0,0x3C,0x0,0x6,0x41,0x42,0x43,0x44,0x45,0x46]))
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write("\x1A\r\n")
    time.sleep(0.5)
    phone.write(b'AT+CIPSEND\r')
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    phone.write(serial.to_bytes([0x30,0xA,0x0,0x6,0x2F,0x68,0x65,0x6C,0x6C,0x6F,0x4F,0x4E]))
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write("\x1A\r\n")
    time.sleep(0.5)
    phone.write(serial.to_bytes([0x82,0x0B,0x0,0x1,0x0,0x8,0x2F,0x68,0x65,0x6C,0x6C,0x6F,0x0]))
    rcv = phone.read(50)
    print "\r\nYou sent:" + repr(rcv) 
    time.sleep(0.5)
    phone.write("\x1A\r\n")
    
    while True:
		rcv = phone.read(50)
        print "\r\nReceived:" + repr(rcv)
finally:
    phone.close()
    
