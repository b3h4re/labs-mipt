import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


T = np.array([29.1, 34.4, 39.4, 44.2, 49.2, 54.0, 59.0])
T_0 = np.array([273.16] * 7)
T += T_0

sigma = np.array([0.0721, 0.0715, 0.0707, 0.0698, 0.0690, 0.0685, 0.0675])

x, y, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(T, sigma, [], [], need_b=True)

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\sigma$, $мН/м$")
plt.xlabel("$T$, $К$")
plt.grid(True, linestyle="--")
plt.axis([300, 335, 0.06, 0.08])

dots = np.array([0., 10000])

plt.plot(dots, k * dots + b, "-r", linewidth=0.7, label=f"Линейная аппроксимация зависимости $\sigma$ от $T$" % (k))
plt.plot(x, y, "+b", label=f"Экспериментальные точки", ms=10)

# plt.legend()
# plt.show()
dsdt = k

x, y, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(T, -k*T, [], [], need_b=True)

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\sigma$, $Н/м$")
plt.xlabel("$T$, $К$")
plt.grid(True, linestyle="--")
plt.axis([300, 335, 0.04, 0.130])

dots = np.array([0., 10000])

plt.plot(dots, k * dots + b, "-b", linewidth=0.7, label=f"Линейная аппроксимация зависимости $q$ от $T$" % (k))
plt.plot(x, y, "+r", label=f"Экспериментальные точки", ms=3)



x, y, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(T, sigma-dsdt*T, [], [], need_b=True)
plt.plot(dots, k * dots + b, "-r", linewidth=0.7, label=f"Линейная аппроксимация зависимости $U/F$ от $T$" % (k))
plt.plot(x, y, "+b", label=f"Экспериментальные точки", ms=3)


plt.legend()
plt.show()

# print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
# print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)