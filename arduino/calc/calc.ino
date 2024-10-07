#include <Keypad.h>

int a = 0;
int b = 0;
bool isA = false;
bool isB = false;
bool isStar = false;

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

  if (klikniety) {
    Serial.println(klikniety);

    if (isA == false) {
      a = klikniety - 48;
    } else if (isB == false && isStar == false) {
      b = klikniety - 48;
    } else if (isStar == false && klikniety == '*') {
      isStar = true;
    } else if (klikniety == '#') {
      Serial.println(a*b);
    }
  }
}
