from bluepy.btle import Peripheral, DefaultDelegate
import matplotlib.pyplot as plt
import time

class MyDelegate(DefaultDelegate):
  def __init__(self):
    DefaultDelegate.__init__(self)
    self.data = []

  def handleNotification(self, cHandle, data):
    print("I'm here")
    self.data.append(int.from_bytes(data,byteorder='little'))
p = Peripheral("0C:CF:6F:54:6C:60")
p.setDelegate(MyDelegate())

try:
  service = p.getServiceByUUID("50e967b4-2065-4356-8a56-c839b3c32117")
  characteristic = service.getCharacteristics("2A37")[0]
  start_time = time.time()
  while True:
    if p.waitForNotifications(1.0):
      print("here")
      continue
    print("Waiting...")
    if time.time() - start_time > 10:
      break
finally:
  p.disconnect()

plt.plot(p.delegate.data)
plt.show()
