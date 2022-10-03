import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.sin(x)

x = np.linspace(-10, 10, 10)

y = np.sin(np.rad2deg(x))

def fd(x):
    return -math.cos(x)

fig = plt.figure()

plt.plot(y)

plt.show()
