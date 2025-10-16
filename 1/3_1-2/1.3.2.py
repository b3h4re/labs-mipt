import numpy as np
import matplotlib.pyplot as plt


T_2 = [2.607, 3.038, 3.742, 4.279, 5.249, 6.015, 7.070, 8.416, 10.062, 11.293, 13.239, 15.113, 17.144, 19.149, 21.437, 23.805, 26.384
]
l_2 = [4.07, 9.11, 16.14, 25.18, 36.21, 49.25, 64.28, 81.32, 100.35, 121.39, 144.42, 169.46, 196.49, 225.53, 256.56, 289.60, 324.63
]

u = np.array(T_2)
v = np.array(l_2)

print("u = ", u, "\nv = ", v)

mu = np.mean(u) # средее
mv = np.mean(v)
mv2 = np.mean(v**2) # средний квадрат
mu2 = np.mean(u**2)
muv = np.mean (u * v) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
print("k = ", k, ", b = ", b)

np.polyfit(v, u, 1)
n = len(u)
sigma_v = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18])
sigma_u = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3])


sigma_k = (1/n**0.5) * ((np.mean(u**2) - np.mean(u)**2)/(np.mean(v**2) - np.mean(v)**2) - k**2)**0.5
sigma_b = sigma_k * (np.mean(v**2) - np.mean(v)**2)**0.5

print("sigma_k = ", sigma_k, "sigma_b = ",  sigma_b)

print(100*sigma_u/u)

plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$u=t^2$, $с^{2}$") # подписи к осям
plt.xlabel("$v=l_c^2$, ${см}^2$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0,350,0,30]) # масштабы осей
x = np.array([0., 10000]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v + %.2f$" % (k, b)) # аппроксимация
plt.errorbar(v, u, xerr=sigma_v, yerr=sigma_u, fmt="ok", label="Экспериментальные точки", ms=3) # точки с погрешностями
plt.legend() # легенда
plt.show()