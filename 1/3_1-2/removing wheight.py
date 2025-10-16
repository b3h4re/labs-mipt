import numpy as np
import matplotlib.pyplot as plt


P = [31.41, 29.0, 26.59, 24.18, 21.77, 19.36, 16.97, 14.56, 12.15, 9.74, 7.33, 4.92]
delta_l = [2.57, 2.54, 2.42, 2.28, 2.15, 2.01, 1.88, 1.74, 1.61, 1.47, 1.32, 1.17]
sigma_P = [0.035, 0.032, 0.029, 0.026, 0.024, 0.021, 0.018, 0.015, 0.012, 0.009, 0.006, 0.003]
sigma_delta = [0.17, 0.17, 0.16, 0.15, 0.14, 0.13, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08]

mx_l = -1
mx_P = -1
for i in range(len(delta_l)):
    mx_l = max(mx_l, 100*sigma_delta[i]/delta_l[i])
    mx_P = max(mx_P, 100*sigma_P[i]/P[i])
print("varepsilon_max_l = ", mx_l)
print("varepsilon_max_P = ", mx_P)

y = np.array(delta_l)
x = np.array(P)
sigma_y = np.array(sigma_delta)
sigma_x = np.array(sigma_P)

print("y = ", y, "\nx = ", x)

my = np.mean(y)
mx = np.mean(x)
mx2 = np.mean(x**2)
my2 = np.mean(y**2)
mxy = np.mean (y * x)

# y = kx + b
k = (mxy - mx * my) / (mx2 - mx * mx)
b = my - k * mx
print("k = ", k, ", b = ", b)

np.polyfit(x, y, 1)

n = len(y)

sigma_k = (1/n**0.5) * (((my2 - my * my) / (mx2 - mx * mx)) - k**2)**0.5
sigma_b = sigma_k * (mx2 - mx * mx) ** 0.5

print("sigma_k = ", sigma_k, "sigma_b = ",  sigma_b)
print("varepsilon_k = ", 100*sigma_k/k)

plt.figure(figsize=(8,6), dpi=100)
plt.ylabel("$\Delta l$, $мм$")
plt.xlabel("$P$, $Н$")
plt.grid(True, linestyle="--")
plt.axis([0, 32, 0, 3])
# plt.axis([int(min(x)), int(max(x)) + 1, int(min(y)), int(max(y)) + 1])
dots = np.array([0., 10000])
plt.plot(dots, k * dots + b, "-r",linewidth=1, label="Линейная аппроксимация $\Delta l = %.3f P + %.3f$" % (k, b))
plt.errorbar(x, y, xerr=sigma_x, yerr=sigma_y, fmt="ok", label="Экспериментальные точки", ms=3)
plt.legend()
plt.show()
