import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x ** 2


def f2(x):
    return x*8 - 16

x1_array, x2_array = np.arange(0,10,0.01), np.arange(0,10,0.01)
y1_array, y2_array = f1(x1_array), f2(x2_array)



plt.plot(x1_array ,y1_array)
plt.plot(x2_array, y2_array)
plt.show()

