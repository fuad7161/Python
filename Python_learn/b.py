import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.01)
xt = np.sin(2 * np.pi * 3 * t)
plt.stem(t, xt)

t = np.arange(0, 1, 0.01)
xt = np.sin(2 * np.pi * 3 * t)
plt.plot(t, xt)