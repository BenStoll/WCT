from bluepy import ble
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import time
import csv

file_name = 'heartData.csv'
field_names = ['iteration', 'reading']

iteration = 0

readings = []

with open(file_name, 'w') as data_file:
  csv_writer = csv.DictWriter(data_file, fieldnames=field_names)
  csv_writer.writeheader()

# BLE Delegate Class
class MyDelegate(btle.DefaultDelegate):
  def __init__(self):
    btle.DefaultDelegate.__init__(self)
    self.data = []
  
  def handleNotification(self, cHandle, data):
    global iteration
    with open(file_name, 'a') as data_file:
      csv_writer = csv.DictWriter(data_file, fieldnames=field_names)

      iteration+=1

      info = {
        "iteration": iteration,
        "reading": data[0]
      }

      csv_writer.writerow(info)
      print(iteration,data[0])

address = "44:1D:62:69:DC:E4"
#0C:CF:6F:54:6C:60
service_uuid = "50e967b4-2065-4356-8a56-c839b3c32117"
char_uuid = "2A37"

p = btle.Peripheral(address)
p.setDelegate(MyDelegate())

svc = p.getServiceByUUID(service_uuid)
ch = svc.getCharacteristics(char_uuid)[0]

setup_data = b"/x01|x00"
p.writeCharacteristic(ch.valHandle + 1)
print(type(ch_data))
print(ch_data)

start_time = time.time()

print("=== Main Loop ===")

while True:
  if p.waitForNotifications(1.0):
    continue
  print("Waiting...")

p.disconnect()

plt.plot(readings)
plt.show()
