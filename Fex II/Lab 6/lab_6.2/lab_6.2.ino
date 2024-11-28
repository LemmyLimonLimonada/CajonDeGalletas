#include <math.h>

double sensorValue0 = 0;
double sensorValue1 = 0.00;
double A = 3.3865469222658334 * pow(10, -1);
double B = -6.45726718252631 * pow(10, -2);
double C = 3.836960176189242 * pow(10, -4);

void setup() {
  Serial.begin(9600);
}

void loop() {
  double resistencia0, temperatura0, resistencia1, temperatura1;
  sensorValue0 = analogRead(A0);
  sensorValue1 = analogRead(A1);

  resistencia0 = 1000 * ((1023)/(sensorValue0) - 1);
  Serial.println(resistencia0);
  temperatura0 = 1 / (A + B * log(resistencia0) + C * pow(log(resistencia0), 3));

  resistencia1 = 1000 * ((1023)/(sensorValue1) - 1);
  temperatura1 = 1 / (A + B * log(resistencia1) + C * pow(log(resistencia1), 3));

  
  delay(1000);
}
