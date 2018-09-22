import serial
import requests
port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)

serialFromArduino.flushInput()
while True:
    input_s = serialFromArduino.readline().decode()[:-5]
    print(input_s)
    durl = 'http://192.168.0.28/' + input_s
    req = requests.get(url = durl)
    
    
    