float Ta = 500;
float Tb = 500;

void setup() {
pinMode(13,OUTPUT);

}

void loop() {
digitalWrite(13,HIGH);
delay(Ta);
digitalWrite(13,LOW);
delay(Tb);
}

