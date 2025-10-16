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
    k = mxy / mx2
    b = my - k * mx

    sigma_k = (1 / n ** 0.5) * (my2 / mx2 - k ** 2) ** 0.5
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
N1 = np.array(list(map(float, '''0,204303000
0,396973170
0,877876320
1,318733520
1,713747200
'''.replace(',', '.').split())))

sigma_N1 = np.array(list(map(float, '''0.0002
0,0003
0,0005
0,0006
0,0007
'''.replace(',', '.').split())))

T1 = np.array(list(map(float, '''01,302211302
2,358722359
4,987714988
7,493857494
9,926289926
'''.replace(',', '.').split())))

sigma_T1 = np.array(list(map(float, '''0,073710074
0,073710074
0,073710074
0,073710074
0,073710074
'''.replace(',', '.').split())))

# x1, y1, sigma_x1, sigma_y1, k1, sigma_k1 = getting_needed_format_linear_k(N1, T1, sigma_N1, sigma_T1)
x1, y1, sigma_x1, sigma_y1, k1, sigma_k1 = getting_needed_format_linear_k(T1, N1, sigma_T1, sigma_N1)

# q_2
N2 = np.array(list(map(float, '''0,048653880
0,107323940
0,231659220
0,331860320
0,712909920
'''.replace(',', '.').split())))

sigma_N2 = np.array(list(map(float, '''0,002359445
0,004192842
0,007469495
0,009780908
0,017352621
'''.replace(',', '.').split())))

T2 = np.array(list(map(float, '''1,031941032
1,818181818
3,611793612
5,307125307
11,375921376
'''.replace(',', '.').split())))

sigma_T2 = np.array(list(map(float, '''0,073710074
0,073710074
0,073710074
0,073710074
0,073710074
'''.replace(',', '.').split())))

# x2, y2, sigma_x2, sigma_y2, k2, sigma_k2 = getting_needed_format_linear_k(N2, T2, sigma_N2, sigma_T2)
x2, y2, sigma_x2, sigma_y2, k2, sigma_k2 = getting_needed_format_linear_k(T2, N2, sigma_T2, sigma_N2)

# making graph
#np.polyfit(x_N1, y_T1, 1)

max_x, min_x = max(x2.max(), max_x), min(x2.min(), min_x)
max_y, min_y = max(y2.max(), max_y), min(y2.min(), min_y)

x_start, x_end = 0, int(1.5*max_x)
y_start, y_end = 0, int(1.5*max_y)

plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\Delta T$, $К$")
plt.xlabel("$N$, $Вт$")
plt.grid(True, linestyle="--")
plt.axis([0, 12, 0, 2])
#plt.axis([x_start, x_end, y_start, y_end])
dots = np.array([0., 10000])


plt.plot(dots, k1 * dots, "-r", linewidth=0.7,
         label="Линейная аппроксимация для $q_1$" % (k1)) # $\Delta T = %.2f N$" % (k1)
plt.plot(dots, k2 * dots, "-b", linewidth=0.7,
         label="Линейная аппроксимация для $q_2$" % (k2)) # $\Delta T = %.2f N$" % (k2)

plt.plot(x1, y1, "+r", label="Экспериментальные точки для $q_1$", ms=10)
plt.plot(x2, y2, "+b", label="Экспериментальные точки для $q_2$", ms=10)

# plt.errorbar(x1, y1, xerr=sigma_x1, yerr=sigma_y1, fmt="ok", label="Экспериментальные точки", ms=3)
# plt.errorbar(x2, y2, xerr=sigma_x1, yerr=sigma_y1, fmt="ok", label="Экспериментальные точки", ms=3)

plt.legend()
plt.show()

print("k1: ", k1, "\sigma: ", sigma_k1, "\\varepsilon: ", sigma_k1 * 100 / k1)
print("k2: ", k2, "\sigma: ", sigma_k2, "\\varepsilon: ", sigma_k2 * 100 / k2)
