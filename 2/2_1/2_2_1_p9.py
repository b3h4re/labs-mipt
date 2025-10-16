import numpy as np
import matplotlib.pyplot as plt
from math import log
from useful.base import getting_k_b_from_data


P = np.array([41.3, 82.5, 120, 161.3])
D = np.array([11, 5.1, 3.6, 2.6])
print(1/P)

sigma_P = np.array([])
sigma_D = np.array([])

x, y, sigma_x, sigma_y, k, sigma_k = (
    getting_k_b_from_data(x=1/P, y=D, sigma_x=sigma_P, sigma_y=sigma_D, need_b=False))


fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$D$, $см^2 \cdot с^{-1}$")
plt.xlabel("$1/P$, $торр^{-1}$")
plt.grid(True, linestyle="--")
plt.axis([0, 0.025, 0, 12])
# plt.imshow(10*np.random.rand(5,3), aspect="auto")

dots = np.array([0., 10000])

plt.plot(dots, k * dots, "-r", linewidth=0.7,
         label="Линейная аппроксимация зависимости $D$ от $1/P$" % (k)) # $\Delta T = %.2f N$" % (k1)

plt.plot(x, y, "+b", label="Экспериментальные точки", ms=10)

plt.legend()
plt.show()