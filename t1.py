import serial
import requests
import urllib
import RPi.GPIO as IO

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)
serialFromArduino.flushInput()
IO.setmode(IO.BCM)
try:
    while True:
        input_s = serialFromArduino.readline().decode()[:-5]
        print(input_s)
        
        RawData = {'tmp' : input_s}
        Rdata = urllib.parse.urlencode(RawData).encode("utf-8")
        print(Rdata)
        req = urllib.request.Request(url = "http://192.168.0.184/put", data = Rdata, method = 'PUT')     
     ##   durl = 'http://192.168.0.184/put' 
     ##   req = requests.put(url = durl, data = RawData)
     ##  print(req.status)
        response = urllib.request.urlopen(req)
        print(response.status)
        
except KeyboardInterrupt as e:
    print(e.decode())
    
    
