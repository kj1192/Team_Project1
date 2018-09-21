#include <Servo.h>

int sensorPin = 0;
int servoPin = 9;
int angle = 0;
Servo servo
void setup(){
  Serial.begin(9600);
  servo.attach(servoPin);  
}

void loop()
{
  int reading = analogRead(sensorPin);
  
  float voltage = reading * 5.0;
  voltage /= 1024.0;
 
  float  tempC = (voltage -0.5) * 100;
  Serial.println(tempC);
  if(tempC >30){
    if(angle == 0){
      servo.write(180);
      angle = 180;
    }
    else {
      servo.write(0);
      angle = 0;
    }
  }

  delay(1000);
}



