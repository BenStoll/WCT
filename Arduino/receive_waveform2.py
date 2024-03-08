from bluepy.btle import Peripher, DefaultDelegate
import matplotlib.pylot as plt
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
  service = p.getServiceByUUID("50
