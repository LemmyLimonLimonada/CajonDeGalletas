float Ta  = 200;
int sensorValue = 0; 

void setup() {
pinMode(13,OUTPUT);
Serial.begin(9600);
}

void loop(){
  sensorValue = analogRead(A0);

  if (sensorValue < 720){
    Serial.println("Luz encendida ---- " + String(sensorValue));
    digitalWrite(13,HIGH);
  }
  else{
    Serial.println("Luz apagada ---- " + String(sensorValue));
    digitalWrite(13,LOW);
  }  
  delay(Ta);
}


