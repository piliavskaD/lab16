import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() 

x = np.linspace(0.1, 9, 50)
y = np.log(x) + np.log10(x) + 0.21 * x


ax.plot(x, y, color="red", linestyle="--", label='y = log(x) + log10(x) + 0.21 * x')

ax.set_title("Графік функції")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.savefig("logarifm.png", format="png")

ax.grid(True)
ax.legend(loc="lower right")

plt.show()