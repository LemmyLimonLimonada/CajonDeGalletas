float Ta  = 1000;
float Tb = 1000;
int sensorValue = 0; 

void setup() {
pinMode(13,OUTPUT);
Serial.begin(9600);
}

void loop(){
  sensorValue = analogRead(A0);
  delay(Ta);

  if (sensorValue > 750){
    Serial.println("Encendido ---- " + String(sensorValue));
  }
  else{
    Serial.println("Apagado ---- " + String(sensorValue));
  }  
  digitalWrite(13,HIGH);

  sensorValue = analogRead(A0);
  delay(Tb);
  if (sensorValue > 750){
    Serial.println("Encendido ---- " + String(sensorValue));
  }
  else{
    Serial.println("Apagado ---- " + String(sensorValue));
  }
  digitalWrite(13,LOW);
}