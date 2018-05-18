import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-7.0, 7.0, 0.001)
y = sigmoid(x)
plt.plot(x, y)
plt.show()

