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
  if(tempC >= 290 && tempC <300){
   analogWrite(motorPin,200); 
  }
  else if(tempC >=300){
    analogWrite(motorPin,249);
  }
  else{
    analogWrite(motorPin,0);
  }

  delay(2000);
}



