#include <math.h> 

float sensorValue = 0; 

void setup() {
  Serial.begin(9600);  
}

void loop() {
  sensorValue = 1023/analogRead(A0);
  Serial.println(sensorValue);  
  delay(1000);
} 

