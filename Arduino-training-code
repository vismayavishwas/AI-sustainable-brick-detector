const int solenoidPin = 9;
const int piezoPin = A0;
const int totalHits = 25;

bool testing = false;
int hitCount = 0;

void setup() {

  pinMode(solenoidPin, OUTPUT);
  digitalWrite(solenoidPin, LOW);

  Serial.begin(115200);

  Serial.println("================================");
  Serial.println("AI BRICK TESTER READY");
  Serial.println("Type 's' to START");
  Serial.println("================================");
}

void loop() {

  // Start command
  if (Serial.available() > 0) {

    char command = Serial.read();

    if (command == 's' || command == 'S') {

      testing = true;
      hitCount = 0;

      Serial.println("--------------------------------");
      Serial.println("TEST STARTED");
      Serial.println("Hit,Peak,Energy,DecayTime");
      Serial.println("--------------------------------");

      delay(1000);
    }
  }

  if (testing && hitCount < totalHits) {

    // FIRE SOLENOID
    digitalWrite(solenoidPin, HIGH);
    delay(60);
    digitalWrite(solenoidPin, LOW);

    delay(20);

    int peak = 0;
    long energy = 0;

    // REAL decay time
    long decayTime = 0;

    for (int i = 0; i < 300; i++) {

      int sensorValue = analogRead(piezoPin);

      if(sensorValue > 2) {

        energy += sensorValue;

        if(sensorValue > peak) {
          peak = sensorValue;
        }

        // last vibration moment
        decayTime = i;
      }

      delay(1);
    }

    hitCount++;

    Serial.print(hitCount);
    Serial.print(",");

    Serial.print(peak);
    Serial.print(",");

    Serial.print(energy);
    Serial.print(",");

    Serial.println(decayTime);

    delay(3000);
  }

  if (testing && hitCount >= totalHits) {

    testing = false;

    Serial.println("--------------------------------");
    Serial.println("25 HITS COMPLETE");
    Serial.println("CHANGE BRICK");
    Serial.println("Type 's' TO START AGAIN");
    Serial.println("--------------------------------");
  }
}
