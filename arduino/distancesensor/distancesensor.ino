float odleglosc;

void setup() {
  // put your setup code here, to run once:
  pinMode(12, INPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(11, HIGH);
  delay(10);
  digitalWrite(12, LOW);

  odleglosc = pulseIn(12, HIGH) / 148.00 * 2.54;

  Serial.println(odleglosc);
}
