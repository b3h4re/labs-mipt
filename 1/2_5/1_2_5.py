import numpy as np
import matplotlib.pyplot as plt


omega = [0.035, 0.055, 0.086, 0.134, 0.202]
moment = [0.0672, 0.1080, 0.1683, 0.2578, 0.3895]

u = np.array(omega)
v = np.array(moment)

print("u = ", u, "\nv = ", v)

mu = np.mean(u) # средее
mv = np.mean(v)
mv2 = np.mean(v**2) # средний квадрат
mu2 = np.mean(u**2)
muv = np.mean (u * v) # среднее от произведения
k = muv / mv2
b = 0
print("k = ", k, ", b = ", b)

np.polyfit(v, u, 1)

sigma_v = 0.0004
sigma_u = 0.0004
n = 5

sigma_k = (1/n**0.5) * ((np.mean(u**2))/(np.mean(v**2)) - k**2)**0.5
sigma_b = 0

print("sigma_k = ", sigma_k, "sigma_b = ",  sigma_b)

plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$u=\Omega$, $с^{-1}$") # подписи к осям
plt.xlabel("$v=M$, $Н \cdot м^2$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0,0.5,0,0.25]) # масштабы осей
x = np.array([0., 10000]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v$" % (k)) # аппроксимация
plt.errorbar(v, u, xerr=sigma_v, yerr=sigma_u, fmt="ok", label="Экспериментальные точки", ms=3) # точки с погрешностями
plt.legend() # легенда
plt.show()