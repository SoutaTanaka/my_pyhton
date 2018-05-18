import numpy as np
import matplotlib.pylab as plt


def f(si, vx, vy, t):
    v0 = vx / np.cos(si)
    x = vx * t
    y1 = np.tan(si) * x
    g = 9.80665
    y2 = 2 * v0 ** 2
    y3 = np.cos(si) ** 2 
    y4 = x ** 2
    y5 = y2 * y3
    y6 = g / y5
    y7 = y6 * y4
    y = y1 - y7
    return y


y = ([])
x = np.arange(0, 5, 0.01)
print(x)
for i in x:
    y.append(f(43, 20, 20, i))


print(y)
plt(x, y)
plt.show()
