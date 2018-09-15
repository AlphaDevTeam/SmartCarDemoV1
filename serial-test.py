import serial
from time import sleep

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

while True:
    port.write("AT")
    rcv = port.read(10)
    sleep(5)    
