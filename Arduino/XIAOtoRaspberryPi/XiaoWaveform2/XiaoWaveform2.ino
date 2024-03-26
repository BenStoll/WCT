#include <ArduinoBLE.h>

BLEService sensorService("50e967b4-2065-4356-8a56-c839b3c32117");
BLEIntCharacteristic analogCharacteristic("2A37", BLERead | BLENotify);
//int testValue = 1;

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
      int sensorValue = analogRead(A0);
      //testValue++;
      analogCharacteristic.writeValue(sensorValue);
     //analogCharacteristic.writeValue(testValue);
      delay(100);
    }
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}
