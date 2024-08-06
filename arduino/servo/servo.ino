#include <Servo.h>;
int pot = 0;
Servo s1;

void setup() {
  Serial.begin(9600);
  s1.attach(9);

}

void loop() {
  pot = analogRead(A0);
  Serial.println(pot);
  int asd = map(pot, 0, 1023, 0, 180);
  s1.write(asd);
}
