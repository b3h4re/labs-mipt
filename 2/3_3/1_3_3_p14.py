import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


data_file = open("data_p14.data", "r")
Q = np.array(list(map(float, data_file.readline().split())))
P = np.array(list(map(float, data_file.readline().split())))
r = np.array(list(map(float, data_file.readline().split())))
x = (P * r**5) ** 0.5
y = Q


x, y, sigma_x, sigma_y, k, sigma_k = getting_k_b_from_data(x=x, y=y, sigma_x=[], sigma_y=[], need_b=False)

print(f"k: {k}, sigma_k: {sigma_k}")
print()

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.xlabel("$\sqrt{\Delta P r^5}$")
plt.ylabel("$P, Па$")
plt.grid(True, linestyle="--")
plt.axis([50, 220, 0, 20])

dots = np.array([0., 10000])

plt.plot(dots, k * dots, "-r", linewidth=0.7,
         label="Линейная аппроксимация зависимости" % (k)) # $\Delta T = %.2f N$" % (k1)

x1, y1, x2, y2 = [], [], [], []
for i in range(len(x)):
    if r[i] == r[0]:
        x1.append(x[i])
        y1.append(y[i])
    else:
        x2.append(x[i])
        y2.append(y[i])

x1 = np.array(x1)
y1 = np.array(y1)
x2 = np.array(x2)
y2 = np.array(y2)

plt.plot(x1, y1, "+r", label=f"Экспериментальные точки для первой трубы", ms=10)
plt.plot(x2, y2, "+b", label=f"Экспериментальные точки для второй трубы", ms=10)

plt.legend()
plt.show()