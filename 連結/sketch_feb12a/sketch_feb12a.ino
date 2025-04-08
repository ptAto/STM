#include "BluetoothSerial.h"

BluetoothSerial SerialBT;
String str;
unsigned long previousMillis = 0;
char chr;

void setup() {
  pinMode(0, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  
  Serial.begin(9600);
  SerialBT.begin("ESP32-BT"); // 藍牙設備名稱
}

void loop() {
  unsigned long currentMillis = millis();
  SerialBT.println(millis());

  if (SerialBT.available()) {
    str = SerialBT.readStringUntil('\n');

    if (str == "teastup") {           
        digitalWrite(13, HIGH);
        previousMillis = currentMillis;
        SerialBT.println(millis());
    } else if (str == "teastdown") {
        digitalWrite(13, LOW);
        previousMillis = currentMillis;
        SerialBT.println(millis());
    } else if (str == "up") {
        digitalWrite(8, HIGH);
        digitalWrite(9, HIGH);
        delay(10);
        digitalWrite(8, LOW);
        digitalWrite(9, LOW);
        previousMillis = currentMillis;
        SerialBT.println(millis());
    } else if (str == "down") {
        digitalWrite(6, HIGH);
        digitalWrite(7, HIGH);
        delay(10);
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        previousMillis = currentMillis;
        SerialBT.println(millis());
    } else if (str == "laft") {
        digitalWrite(7, HIGH);
        digitalWrite(9, HIGH);
        delay(10);
        digitalWrite(7, LOW);
        digitalWrite(9, LOW);
        previousMillis = currentMillis;
        SerialBT.println(millis());
    } else if (str == "right") {
        digitalWrite(6, HIGH);
        digitalWrite(8, HIGH);
        delay(10);
        digitalWrite(8, LOW);
        digitalWrite(6, LOW);
        previousMillis = currentMillis;
        SerialBT.println(millis());
    }
  }
}