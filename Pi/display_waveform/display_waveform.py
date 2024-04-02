import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight") # Check styles later

x_vals = []
y_vals = []

# Live Plotting Function
def animate(i):
  data = pd.read_csv('heartData.csv')
  data = data.iloc[-50:]
  x = data['iteration']
  y = data['reading']

  plt.cla()

  plt.plot(x,y, label='Heartbeat')

  plt.legend(loc='upper left')
  plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=2)

plt.tight_layout()
plt.show()
