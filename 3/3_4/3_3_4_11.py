import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data

B = np.array([0.19, 0.36, 0.55, 0.73, 0.88, 1.00, 1.09, 1.16])
I_M = np.array([0.19, 0.37, 0.56, 0.75, 0.93, 1.13, 1.3, 1.5])

x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(I_M, B, [], [])

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$B, Тл$")
plt.xlabel("$I_M, А$")
plt.grid(True, linestyle="--")
plt.axis([0, 1.6, 0, 1.5])
dots = np.array([0., 10000])
plt.plot(dots, k * dots + b, linewidth=0.8, label=f"Линейная аппроксимация" % (k)) # $\Delta T = %.2f N$" % (k1)

plt.plot(x, y, "+r", label="Экспериментальные точки", ms=10)

print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

plt.legend()
plt.show()