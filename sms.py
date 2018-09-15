import time
import serial

recipient = "+94777117477"
message = "Hello, World!"

phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=5.0)
try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    phone.write(bytes([26]))
    time.sleep(0.5)
finally:
    phone.close()
