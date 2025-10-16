import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


f = np.array([342, 673, 1006, 1339, 1671, 2005, 2339, 2677, 3014, 3349])
n = np.array([i+1 for i in range(len(f))])

x, y, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(n, f, [], [], need_b=True)

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$f$, $Гц$")
plt.xlabel("$n$")
plt.grid(True, linestyle="--")
plt.axis([0, 11, 0, 4000])

dots = np.array([0., 10000])

plt.plot(dots, k * dots + b, "-r", linewidth=0.7, label=f"Линейная аппроксимация зависимости $f$ от $n$ для углекислого газа" % (k))
plt.plot(x, y, "+b", label=f"Экспериментальные точки", ms=10)

plt.legend()
plt.show()