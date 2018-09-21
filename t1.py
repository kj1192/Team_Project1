import serial
import requests
port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)

serialFromArduino.flushInput()

while True:
	input_s = serialFromArduino.readline()
	print(input_s)
	url = 'localhost'
	r = requests.get(url,params = {'tmp' : input_s})
	print(r.status)
	print(r.txt)
