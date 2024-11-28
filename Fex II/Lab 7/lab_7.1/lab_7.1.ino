#include <math.h>
const int Rc = 1000;
const int Vcc = 5;
const int SensorPin1 = A0;
const int SensorPin2 = A1;

double A = 3.3865469222658334 * pow(10, -1);
double B = -6.45726718252631 * pow(10, -2);
double C = 3.836960176189242 * pow(10, -4);

float K = 2.5;

void setup() {
  Serial.begin(9600);
}
  
void loop() {
  float V01 = analogRead(SensorPin1);
  float V1 = V01 / 1024 * Vcc;
  float V02 = analogRead(SensorPin2);
  float V2 =  V02 / 1024 * Vcc;

  float R1 = (Rc * V1);
  float R2 = (Rc * V2);

  float logR1 = log(R1);
  float logR2 = log(R2);
  float TsH1= 1.0 / (A + (B * logR1) + (C * logR1 * logR1 * logR1) );
  float TsH2= 1.0 / (A + (B * logR2) + (C * logR2 * logR2 * logR2) );

  float kelvin1 = TsH1 - (V1*V1) / (K * R1) * 1000;
  float celsius1 = kelvin1 - 273.15;

  float kelvin2 = TsH2 - (V2*V2) / (K * R2) * 1000;
  float celsius2 = kelvin2 - 273.15;

  Serial.print("Temperatura1: ");
  Serial.print(celsius1);
  Serial.print(" °C   ---   ");
  Serial.print("Temperatura2: ");
  Serial.print(celsius2);
  Serial.println(" °C");
  delay(1000);
  

}
