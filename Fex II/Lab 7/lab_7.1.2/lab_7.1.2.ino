#include <math.h>

double sensorValue0 = 0.00;
double sensorValue1 = 0.00;
double sensorValue2 = 0.00;
double A_0 = 3.3865469222658334 * pow(10, -1);
double B_0 = -6.45726718252631 * pow(10, -2);
double C_0 = 3.836960176189242 * pow(10, -4);

double A_1 = 3.772293243289056 * pow(10, -1);
double B_1 = -6.04276376425807* pow(10, -2);
double C_1 = 2.528871168854769* pow(10, -4);

void setup() {
  Serial.begin(9600);
}

void loop() {
  double resistencia0, temperatura0, resistencia1, temperatura1, voltaje;
  sensorValue0 = analogRead(A0);
  sensorValue1 = analogRead(A1);
  sensorValue2 = analogRead(A2);

  resistencia0 = 1000 * ((1023)/(sensorValue0) - 1);
  temperatura0 = 1 / (A_0 + B_0 * log(resistencia0) + C_0 * pow(log(resistencia0), 3));
  Serial.print(temperatura0);

  Serial.print(",");
  resistencia1 = 1000 * ((1023*3)/(sensorValue1*5)- 1);
  temperatura1 = 1 / (A_1 + B_1 * log(resistencia1) + C_1 * pow(log(resistencia1), 3));
  Serial.print(temperatura1);

  Serial.print(",");
  voltaje = (sensorValue2*5)/1023;
  Serial.println(voltaje);
  
  delay(1000);
}

