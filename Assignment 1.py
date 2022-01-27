import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,100)
sin = np.sin(x)
cos = np.cos(x)
points = [i*np.pi for i in range(-4,5)]
labels = ['-2π','-3π/2','-π','-π/2','0','π/2','π','3π/2','2π']

plt.plot(x,sin, label = 'sin')
plt.plot(x,cos, label = 'cos')
plt.legend()
plt.show()
