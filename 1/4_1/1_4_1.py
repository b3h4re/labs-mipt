import numpy as np
import matplotlib.pyplot as plt


l = 0.9841

a = np.array([29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9]) # [см]
N = len(a)

n = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

t = np.array([29.97, 29.19, 28.72, 28.58, 28.67, 28.98, 29.44, 30.03, 30.75, 31.54])

T = np.array(t) / n

M0 = 947.9 # г
m_g = 291 # г
x_c0 = 27.39

y = np.array([2, 9, 16, 23, 30, 37, 44, 51, 58, 65])

x_c = (M0 * x_c0 + m_g * y) / (M0 + m_g)

print("x_c = ", x_c)

u = T**2 * x_c

v = y ** 2
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

sigma_y = 0.5e-3
sigma_T = 0.03 / 20

plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$u=T^2 x_ц$, $с^2 \cdot см$") # подписи к осям
plt.xlabel("$v=x^2_ц$, $см^2$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0,5000,0,130]) # масштабы осей
x = np.array([0., 10000]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v + %.2f$" % (k, b)) # аппроксимация
plt.errorbar(v, u, xerr=sigma_y, yerr=sigma_T, fmt="ok", label="Экспериментальные точки", ms=3) # точки с погрешностями
plt.legend() # легенда
plt.show()

plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$T$, с") # подписи к осям
plt.xlabel("$y$, см")
plt.xlim([0, 100])
plt.grid(True, linestyle="--") # пунктирная сетка
plt.errorbar(y, T, xerr=sigma_y, yerr=sigma_T, fmt=".k", label="Экспериментальные точки") # точки с погрешностями
plt.plot(y, T, "--r", linewidth=1, label="Кусочно линейная интерполяция") # интерполяция
plt.plot([0.00,100], [min(T), min(T)], "--b", linewidth=1, label="Минимум") # минимум
plt.legend() # легенда
plt.show()