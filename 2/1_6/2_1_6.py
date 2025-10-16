import numpy as np
import matplotlib.pyplot as plt


def getting_needed_format_linear_k_b(x: list, y: list, sigma_x: list, sigma_y: list):
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
    k = (mxy - my * mx) / (mx2 - mx**2)
    b = my - k * mx

    sigma_k = (1 / n ** 0.5) * ((my2 - my**2)/(mx2 - mx**2) - k**2) ** 0.5
    sigma_b = sigma_k * (mx2 - mx * mx) ** 0.5

    return x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b


def getting_needed_format_linear_k(x: list, y: list, sigma_x: list, sigma_y: list):
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

    # y = kx
    k = mxy / mx2

    sigma_k = (1 / n ** 0.5) * (my2 / mx2 - k ** 2) ** 0.5

    return x, y, sigma_x, sigma_y, k, sigma_k


# for important settings
max_x = -1e9
max_y = -1e9
min_x = 1e9
min_y = 1e9

# x = N
# y = T

# q_1
P1 = np.array(list(map(float, '''3.9
3.7
3.5
3.3
3.1
2.8
2.6
2.3
2.1
1.8
1.4
'''.replace(',', '.').split())))

sigma_P1 = np.array(list(map(float, '''0.1
0.1
0.1
0.1
0.1
0.1
0.1
0.1
0.1
0.1
0.1
'''.replace(',', '.').split())))

T1 = np.array(list(map(float, '''3.93
3.71
3.49
3.32
3.10
2.46
2.48
2.21
1.94
1.65
1.23
'''.replace(',', '.').split())))

sigma_T1 = np.array(list(map(float, '''0.15
0.15
0.15
0.15
0.15
0.15
0.15
0.15
0.15
0.15
0.15
'''.replace(',', '.').split())))

x1, y1, sigma_x1, sigma_y1, k1, sigma_k1, b1, sigma_b1 = getting_needed_format_linear_k_b(P1, T1, sigma_P1, sigma_T1)

# q_2
P2 = np.array(list(map(float, '''3.4
3.2
3.0
2.8
2.5
2.2
2.0
1.8
'''.replace(',', '.').split())))

sigma_P2 = np.array(list(map(float, '''0.1
0.1
0.1
0.1
0.1
0.1
0.1
0.1
'''.replace(',', '.').split())))

T2 = np.array(list(map(float, '''3.13
2.94
2.72
2.43
2.22
1.88
1.71
1.49
'''.replace(',', '.').split())))

sigma_T2 = np.array(list(map(float, '''0.14
0.14
0.14
0.14
0.14
0.14
0.14
0.14
'''.replace(',', '.').split())))

x2, y2, sigma_x2, sigma_y2, k2, sigma_k2, b2, sigma_b2 = getting_needed_format_linear_k_b(P2, T2, sigma_P2, sigma_T2)

# making graph
#np.polyfit(x_N1, y_T1, 1)

max_x, min_x = max(x2.max(), max_x), min(x2.min(), min_x)
max_y, min_y = max(y2.max(), max_y), min(y2.min(), min_y)

x_start, x_end = 0, int(1.5*max_x)
y_start, y_end = 0, int(1.5*max_y)

plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\Delta T$, $К$")
plt.xlabel("$\Delta P$, $атм$")
plt.grid(True, linestyle="--")
plt.axis([1, 4.2, 0, 4.5])
#plt.axis([x_start, x_end, y_start, y_end])
dots = np.array([0., 10000])


plt.plot(dots, k1 * dots + b1, "-r", linewidth=0.7,
         label="Линейная аппроксимация для $t_1$" % (k1)) # $\Delta T = %.2f N$" % (k1)
plt.plot(dots, k2 * dots + b2, "-b", linewidth=0.7,
         label="Линейная аппроксимация для $t_2$" % (k2)) # $\Delta T = %.2f N$" % (k2)

plt.plot(x1, y1, "+r", label="Экспериментальные точки для $t_1$", ms=10)
plt.plot(x2, y2, "+b", label="Экспериментальные точки для $t_2$", ms=10)

#plt.errorbar(x1, y1, xerr=sigma_x1, yerr=sigma_y1, fmt="ok", label="Экспериментальные точки", ms=3)
#plt.errorbar(x2, y2, xerr=sigma_x1, yerr=sigma_y1, fmt="ok", label="Экспериментальные точки", ms=3)

plt.legend()
plt.show()

print("k1: ", k1, "\sigma: ", sigma_k1, "\\varepsilon: ", sigma_k1 * 100 / k1)
print("b1: ", b1, "\sigma: ", sigma_b1, "\\varepsilon: ", sigma_b1 * 100 / b1)
print("k2: ", k2, "\sigma: ", sigma_k2, "\\varepsilon: ", sigma_k2 * 100 / k2)
print("b2: ", b2, "\sigma: ", sigma_b2, "\\varepsilon: ", sigma_b2 * 100 / b2)
