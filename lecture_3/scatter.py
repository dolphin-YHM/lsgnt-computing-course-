import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

colours = np.random.rand(N)
area = (30*np.random.rand(N))**2 # 0 to 15 point radii

plt.scatter(x, y, s = area, c = colours, alpha = 0.5)
plt.show()