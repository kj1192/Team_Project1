import serial
import requests
import urllib.request
#port = "/dev/ttyACM1"
#serialFromArduino = serial.Serial(port,9600)

#serialFromArduino.flushInput()

    #input_s = serialFromArduino.readline().decode()[:-2]
durl = 'http://192.168.43.121/3699' #+ input_s
r = requests.get(url = durl)  
print(r.status)
print("end r")

	#try:
        #response = urllib.request.urlopen(req)
        #print(response.read())
	#except urllib.error.HTTPError as e:
	#	print(e.code)
#print(e.read())



