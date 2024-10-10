int potencjometr;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  potencjometr = analogRead(A0) * 2;

  digitalWrite(13, HIGH);
  delay(potencjometr);
  digitalWrite()
}
