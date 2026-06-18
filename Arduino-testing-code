#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int solenoidPin = 9;
const int piezoPin = A0;
const int totalHits = 25;

bool testing = false;
int hitCount = 0;

float totalPeak = 0;
float totalEnergy = 0;
float totalDecay = 0;

void setup() {

  pinMode(solenoidPin, OUTPUT);
  digitalWrite(solenoidPin, LOW);

  Serial.begin(115200);

  lcd.init();
  lcd.backlight();

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("AI BRICK TEST");
  lcd.setCursor(0,1);
  lcd.print("READY");

  Serial.println("Type 's' to START");
}

void loop() {

  if (Serial.available() > 0) {

    char command = Serial.read();

    if(command == 's' || command == 'S') {

      testing = true;
      hitCount = 0;

      totalPeak = 0;
      totalEnergy = 0;
      totalDecay = 0;

      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("SWITCHING ON");
      delay(1500);

      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("TESTING...");
    }
  }

  if(testing && hitCount < totalHits) {

    digitalWrite(solenoidPin, HIGH);
    delay(60);
    digitalWrite(solenoidPin, LOW);

    delay(20);

    int peak = 0;
    long energy = 0;
    long decayTime = 0;

    for(int i = 0; i < 300; i++) {

      int sensorValue = analogRead(piezoPin);

      if(sensorValue > 2) {

        energy += sensorValue;

        if(sensorValue > peak) {
          peak = sensorValue;
        }

        decayTime = i;
      }

      delay(1);
    }

    totalPeak += peak;
    totalEnergy += energy;
    totalDecay += decayTime;

    hitCount++;

    lcd.setCursor(0,1);
    lcd.print("Hit:");
    lcd.print(hitCount);
    lcd.print("/25 ");

    delay(3000);
  }

  if(testing && hitCount >= totalHits) {

    testing = false;

    float avgPeak = totalPeak / totalHits;
    float avgEnergy = totalEnergy / totalHits;
    float avgDecay = totalDecay / totalHits;

    // Send to Python
    Serial.print("FINAL,");
    Serial.print(avgPeak);
    Serial.print(",");
    Serial.print(avgEnergy);
    Serial.print(",");
    Serial.println(avgDecay);

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("ANALYZING...");
  }

  // Receive prediction from Python
  if(Serial.available()) {

    String result = Serial.readStringUntil('\n');

    if(result == "HIGH") {

      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("QUALITY:");
      lcd.setCursor(0,1);
      lcd.print("HIGH");

    } else if(result == "MEDIUM") {

      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("QUALITY:");
      lcd.setCursor(0,1);
      lcd.print("MEDIUM");

    } else if(result == "LOW") {

      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("QUALITY:");
      lcd.setCursor(0,1);
      lcd.print("LOW");
    }
  }
}
