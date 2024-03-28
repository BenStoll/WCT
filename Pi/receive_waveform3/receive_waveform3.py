#This is the updated WORKING code for the Raspberry Pi.
#Instructions to run on the Pi (make sure XIAO code is running too):
#-- Initial Setup --
#source myenv/bin/activate
#cd Desktop/
#-- To run: --
#python3 receive_waveform3.py

from bluepy import btle
import matplotlib.pyplot as plt
import time

readings = []
for i in range(20):
  readings.append(0)

class MyDelegate(btle.DefaultDelegate):
  def __init__(self):
    btle.DefaultDelegate.__init__(self)
    self.data = []

  def handleNotification(self, cHandle, data):
    global readings
    print(data)
    print(data[0])
    readings = readings[1:]
    readings.append(data[0])

address = "0C:CF:6F:54:6C:60"
service_uuid = "50e967b4-2065-4356-8a56-c839b3c32117"
char_uuid = "2A37"

p = btle.Peripheral(address)
p.setDelegate(MyDelegate())

svc = p.getServiceByUUID(service_uuid)
ch = svc.getCharacteristics(char_uuid)[0]

setup_data = b"\x01|x00"
p.writeCharacteristic(ch.valHandle + 1, setup_data)

ch_data = p.readCharacteristic(ch.valHandle + 1)
print(type(ch_data))
print(ch_data)

start_time = time.time()

print("=== Main Loop ===")

while True:
  if time.time() - start_time > 10:
    break
  if p.waitForNotifications(1.0):
    plt.cla()
    plt.plot(readings)
    plt.pause(0.001)
    continue
  print ("Waiting...")

p.disconnect()
plt.show()
