import serial
import requests

port = "/dev/ttyACM1"
serialFromArduino = serial.Serial(port,9600)

serialFromArduino.flushInput()
while True:
	input_s = serialFromArduino.readline()
	durl = 'http://10.0.2.15'
	payload = {'tmp':input_s.decode()[:-1]}

	r = requests.get(durl,params = payload)
	print("end r");
	print(r.text)
