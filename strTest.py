import serial
import requests

port = "/dev/ttyACM1"
serialFromArduino = serial.Serial(port,9600)

serialFromArduino.flushInput()
#b'25.68\r\n'
while True:
        input_s = serialFromArduino.readline()
        print(input_s.decode()[:-1])


