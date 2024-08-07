#include <Keypad.h>

const byte ROWS = 4;
const byte COLUMNS = 4;

const char keys[ROWS][COLUMNS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {9,8,7,6};
byte colPins[COLUMNS] = {5,4,3,2};

Keypad klawiatura = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLUMNS); 

void setup() {
  Serial.begin(9600);
}

void loop() {
  char klikniety = klawiatura.getKey();

  Serial.println(klikniety);
}
