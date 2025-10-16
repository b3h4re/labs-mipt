import numpy as np
import matplotlib.pyplot as plt


def getting_needed_format(x: list, y: list, sigma_x: list, sigma_y: list):
    n = len(y)

    x = np.array(x)
    y = np.array(y)
    sigma_x = np.array(sigma_x)
    sigma_y = np.array(sigma_y)

    my = np.mean(y)
    mx = np.mean(x)
    mx2 = np.mean(x ** 2)
    my2 = np.mean(y ** 2)
    mxy = np.mean(y * x)

    # y = kx + b
    k = (mxy - mx * my) / (mx2 - mx * mx)
    b = my - k * mx

    sigma_k = (1 / n ** 0.5) * (((my2 - my * my) / (mx2 - mx * mx)) - k ** 2) ** 0.5
    sigma_b = sigma_k * (mx2 - mx * mx) ** 0.5

    return x, y, sigma_x, sigma_y, k, b, sigma_k, sigma_b


# topping up

delta_l = [1.15, 1.32, 1.46, 1.6, 1.74, 1.87, 2.01, 2.13, 2.27, 2.4, 2.54, 2.57]
P = [4.92, 7.33, 9.74, 12.15, 14.56, 16.97, 19.36, 21.77, 24.18, 26.59, 29.0, 31.41]
sigma_delta = [0.08, 0.09, 0.1, 0.11, 0.12, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.17]
sigma_P = [0.003, 0.006, 0.009, 0.012, 0.015, 0.018, 0.021, 0.024, 0.026, 0.029, 0.032, 0.035]

xd, yd, sigma_xd, sigma_yd, kd, bd, sigma_kd, sigma_bd = getting_needed_format(P, delta_l, sigma_P, sigma_delta)

# removing

P = [31.41, 29.0, 26.59, 24.18, 21.77, 19.36, 16.97, 14.56, 12.15, 9.74, 7.33, 4.92]
delta_l = [2.57, 2.54, 2.42, 2.28, 2.15, 2.01, 1.88, 1.74, 1.61, 1.47, 1.32, 1.17]
sigma_P = [0.035, 0.032, 0.029, 0.026, 0.024, 0.021, 0.018, 0.015, 0.012, 0.009, 0.006, 0.003]
sigma_delta = [0.17, 0.17, 0.16, 0.15, 0.14, 0.13, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08]

xr, yr, sigma_xr, sigma_yr, kr, br, sigma_kr, sigma_br = getting_needed_format(P, delta_l, sigma_P, sigma_delta)

np.polyfit(xr, yr, 1)

# print("sigma_k = ", sigma_k, "sigma_b = ",  sigma_b)

plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\Delta l$, $мм$")
plt.xlabel("$P$, $Н$")
plt.grid(True, linestyle="--")
plt.axis([0, 32, 0, 3])
# plt.axis([int(min(x)), int(max(x)) + 1, int(min(y)), int(max(y)) + 1])
dots = np.array([0., 10000])

plt.plot(dots, kd * dots + bd, "-r", linewidth=0.7,
         label="Линейная аппроксимация при довешивании$\Delta l = %.3f P + %.3f$" % (kd, bd))
plt.plot(dots, kr * dots + br, "-g", linewidth=0.7,
         label="Линейная аппроксимация при снятии $\Delta l = %.3f P + %.3f$" % (kr, br))

plt.plot(xd, yd, "+r", label="Экспериментальные точки при довешивании", ms=10)
plt.plot(xr, yr, "xg", label="Экспериментальные точки при снятии", ms=10)

# plt.errorbar(xd, yd, xerr=sigma_xd, yerr=sigma_yd, fmt="ok", label="Экспериментальные точки", ms=3)
# plt.errorbar(xr, yr, xerr=sigma_xr, yerr=sigma_yr, fmt="ok", label="Экспериментальные точки", ms=3)

plt.legend()
plt.show()

print("kd: ", kd, "\sigma: ", sigma_kd)
print("kr: ", kr, "\sigma: ", sigma_kr)