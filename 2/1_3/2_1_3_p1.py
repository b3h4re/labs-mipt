import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


f = [
    np.array([236, 466, 699, 928, 1158, 1390, 1620, 1852, 2083, 2313, 2544, 2774, 3005, 3236]),
    np.array([242, 476, 714, 948, 1184, 1420, 1655, 1892, 2128, 2363, 2599, 2834, 3070, 3305]),
    np.array([246, 484, 724, 962, 1202, 1442, 1682, 1922, 2161, 2400]),
    np.array([250, 495, 740, 985, 1230, 1476, 1721, 1966, 2211, 2456])
]

x, y, k, sigma_k, b, sigma_b = [], [], [], [], [], []

for i in range(len(f)):
    x_, y_, sigma_x_, sigma_y_, k_, sigma_k_, b_, sigma_b_ = (
        getting_k_b_from_data(np.array(list(range(len(f[i])))), f[i], [], [], need_b=True))
    x.append(x_)
    y.append(y_)
    k.append(k_)
    sigma_k.append(sigma_k_)
    b.append(b_)
    sigma_b.append(sigma_b_)

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$f$, $Гц$")
plt.xlabel("$n$")
plt.grid(True, linestyle="--")
plt.axis([0, 15, 0, 4000])

dots = np.array([0., 10000])

for i in range(len(f)):
    plt.plot(dots, k[i] * dots + b[i], linewidth=0.7, label=f"Линейная аппроксимация зависимости $f$ от $f$ для t_{i+1}" % (k[i]))
    plt.plot(x[i], y[i], "+b", label=f"Экспериментальные точки для t_{i+1}", ms=3)

for i in range(len(f)):
    print(f"t_{i+1} | k: {k[i]}, sigma_k: {sigma_k[i]} | b: {b[i]}, sigma_b: {sigma_b[i]}")

plt.legend()
plt.show()