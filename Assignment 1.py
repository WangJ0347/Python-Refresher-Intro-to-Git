import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,100)
sin = np.sin(x)
cos = np.cos(x)

#plot 1 period of sin and cos on the same axes
plt.plot(x,sin, label = 'sin')
plt.plot(x,cos, label = 'cos')
plt.legend()
plt.show()
