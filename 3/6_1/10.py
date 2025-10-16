import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


Delta_nu = [46.00, 25.00, 17.33, 13.36, 11.11, 9.01, 8.00, 7.00, 6.03, 5.53, 4.98]  # kHz
tau = [20, 38, 56, 74, 92, 110, 128, 146, 164, 182, 200]  # mcs

x1 = np.array(tau) / 10**6
x1 = 1 / x1

y1 = np.array(Delta_nu) * 1000

x1, y1, k, sigma_k, b, sigma_b = getting_k_b_from_data(x1, y1, None, None, need_b=True, no_sigma=True)

print("k: ", k, "\\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

plt.figure(figsize=(8, 5))
plt.axis([0, 55000, 0, 55000])

dots = np.array([-100_000, 100_000])

plt.plot(dots, dots * k + b, color='red', linewidth=0.8, label='Наилучшая прямая')
plt.plot(x1, y1, "+b", ms=10, label='Эксперементальные точки')


# Title and labels
plt.xlabel("$1 / \\tau, с^{-1}$")
plt.ylabel("$\\Delta \\nu, Гц$")

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
# plt.show()

print()
print()

delta_nu = [5.007, 1.252, 0.715, 0.501, 0.385, 0.313, 0.264, 0.226, 0.203]
T = [0.2, 0.800, 1.400, 2.000, 2.600, 3.200, 3.800, 4.400, 5.000]

x2 = np.array(T) / 1000
x2 = 1 / x2

y2 = np.array(delta_nu) * 1000

x2, y2, k, sigma_k, b, sigma_b = getting_k_b_from_data(x2, y2, None, None, need_b=True, no_sigma=True)

print("k: ", k, "\\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

print(k, b)


plt.figure(figsize=(8, 5))
plt.axis([0, 6000, 0, 6000])

dots = np.array([-100_000, 100_000])

plt.plot(dots, dots * k + b, color='red', linewidth=0.8, label='Наилучшая прямая')
plt.plot(x2, y2, "+b", ms=10, label='Эксперементальные точки')


# Title and labels
plt.xlabel("$1 / T, с^{-1}$")
plt.ylabel("$\\delta \\nu, Гц$")

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()