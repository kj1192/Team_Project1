#include <Servo.h>

int sensorPin = 0;
int motorPin = 9;


void setup(){
  Serial.begin(9600);
  pinMode(motorPin,OUTPUT);
}

void loop()
{
  int reading = analogRead(sensorPin);
  float voltage = reading * 5.0;
  voltage /= 1024.0;
 
  float  tempC = (voltage -0.5) * 100;
  Serial.println(tempC);
  if(tempC > 28 && tempC <31){
   analogWrite(motorPin,150); 
  }
  else if(tempC >= 31){
    analogWrite(motorPin,200);
  }
  else{
    analogWrite(motorPin,0);
  }

  delay(5000);
}



