#include <ArduinoBLE.h>

//Issue is NOT with the XIAO or the transmission, it is with the Pi processing negative numbers.
//Need to figure out how to process negative numbers properly in the Pi code.

BLEService sensorService("50e967b4-2065-4356-8a56-c839b3c32117");
BLEIntCharacteristic analogCharacteristic("2A37", BLERead | BLENotify);
int testValue = 0;
const int analogInPin = A0;
bool up = true;
//int sensorValue = 0;

void setup() {
  Serial.begin(9600);
  while(!Serial);

  pinMode(A0, INPUT);
  if (!BLE.begin()) {
    Serial.println("starting BLE failed!");
    while (1);
  }

  BLE.setLocalName("Xiao BLE Sense");
  BLE.setAdvertisedService(sensorService);

  sensorService.addCharacteristic(analogCharacteristic);
  BLE.addService(sensorService);

  analogCharacteristic.writeValue(0);

  BLE.advertise();
  Serial.println("Bluetooth device active, waiting for connections...");
}

void loop() {
  BLEDevice central = BLE.central();
  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());
    
    while (central.connected()) {
      //int sensorValue = analogRead(analogInPin);
      if ((testValue < 50 && up == true) || (testValue == -50 && up == false)) {
        testValue++;
        up = true;
      }
      else {
        testValue--;
        up = false;
      }
      Serial.print("sensor = ");
      Serial.println(testValue);
      //analogCharacteristic.writeValue(sensorValue);
     analogCharacteristic.writeValue(testValue);
      delay(100);
    }
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}
