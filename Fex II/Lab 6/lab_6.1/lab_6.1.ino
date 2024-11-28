int RelayPin = 6; 
int sensorValue = 0; 
int Ta = 500;

void setup() {
  pinMode(RelayPin, OUTPUT); 
  Serial.begin(9600); 
}

void loop() {
  digitalWrite(RelayPin, LOW);  
  delay(Ta);

  sensorValue = digitalRead(RelayPin);
  Serial.print("Estado del pin: ");
  Serial.println(sensorValue);

  digitalWrite(RelayPin, HIGH);  
  delay(Ta);

  sensorValue = digitalRead(RelayPin);
  Serial.print("Estado del pin: ");
  Serial.println(sensorValue);
}


