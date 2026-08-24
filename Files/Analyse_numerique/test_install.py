import numpy as np
import matplotlib.pyplot as plt

print("NumPy version :", np.__version__)

x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, np.sin(x))
plt.title("Si vous voyez cette courbe, tout fonctionne !")
plt.show()