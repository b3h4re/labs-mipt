import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


m = [i / 10 for i in range(1, 11)]
a = [0.043, 0.098, 0.150, 0.197, 0.246, 0.302, 0.346, 0.398, 0.451, 0.501]

x1 = np.array(m)

y1 = np.array(a)

x1, y1, k, sigma_k, b, sigma_b = getting_k_b_from_data(x1, y1, None, None, need_b=True, no_sigma=True)

print("k: ", k, "\\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

plt.figure(figsize=(8, 5))
plt.axis([0, 1.1, 0, 0.6])

dots = np.array([-100_000, 100_000])

plt.plot(dots, dots * k + b, color='red', linewidth=0.8, label='Наилучшая прямая')
plt.plot(x1, y1, "+b", ms=10, label='Эксперементальные точки')


# Title and labels
plt.xlabel("$m$")
plt.ylabel("$a_\\text{бок}/a_\\text{осн}$")

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
