import serial
import requests
port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)

serialFromArduino.flushInput()

while True:
	input_s = serialFromArduino.readline()
	print(input_s)
	url = 'localhost'
	params = {'code' = 'code'}
	r = requests.get*(url = url , params = params)
	
