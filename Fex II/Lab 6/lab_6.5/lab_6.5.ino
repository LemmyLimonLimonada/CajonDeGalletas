#include <math.h>
//Fex II Laboratorio 6 Parte 5 

int RelayPin = 6; 
double sensorValue = 0;
double A = 3.3865469222658334 * pow(10, -1);
double B = -6.45726718252631 * pow(10, -2);
double C = 3.836960176189242 * pow(10, -4);
double k = 5409* pow(10, -6);

void setup() {
  pinMode(RelayPin, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
    double resistencia, temperatura;
  sensorValue = analogRead(A0);
  resistencia = 1000 * ((1023*3)/(sensorValue*5) - 1);
  temperatura = 1 / (A + B * log(resistencia) + C * pow(log(resistencia), 3));

  if (temperatura < 45){
    Serial.println(temperatura);
    digitalWrite(RelayPin, LOW);  
  }
  else{
    Serial.println(temperatura);
    digitalWrite(RelayPin, HIGH);  
  }  
  
  delay(1000);
}