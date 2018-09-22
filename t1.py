import serial
import requests
import urllib.request
port = "/dev/ttyACM1"
serialFromArduino = serial.Serial(port,9600)

serialFromArduino.flushInput()
while True:
	input_s = serialFromArduino.readline().decode()[:-1]
	#durl = 'http://10.0.2.15?tmp='+input_s.decode()[:-1]
	#payload = {'tmp':input_s.decode()[:-1]}
	#r = requests.get(durl)

	send = uirllib.request.Request(url='http://10.0.2.15',data = inpu_s,method = 'PUT', headers = 'tmp')
	print("end r");
	print(r.text)
