import numpy as np
import matplotlib.pyplot as plt


delta_l = [3.2, 5.9, 8.6, 11.3, 13.8, 16.4, 18.8, 21.4, 23.8, 26.5, 27.1]
mass = [246.1, 491.7, 737, 982.5, 1228.1, 1472.5,1717.8 , 1963.4, 2208.9, 2454.5, 2700.3]

u = np.array(delta_l)
v = np.array(mass)

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
plt.axis([0,3000,0,40]) # масштабы осей
x = np.array([0., 10000]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v$" % (k)) # аппроксимация
plt.errorbar(v, u, xerr=sigma_v, yerr=sigma_u, fmt="ok", label="Экспериментальные точки", ms=3) # точки с погрешностями
plt.legend() # легенда
plt.show()