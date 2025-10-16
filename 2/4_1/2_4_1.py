import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def getting_k_b_from_data(x, y, sigma_x, sigma_y, need_b=True):
    if len(x) != len(y):
        return

    n = len(x)
    x = np.array(x)
    y = np.array(y)
    sigma_x = np.array(sigma_x)
    sigma_y = np.array(sigma_y)

    my = np.mean(y)
    mx = np.mean(x)
    mx2 = np.mean(x ** 2)
    my2 = np.mean(y ** 2)
    mxy = np.mean(y * x)

    if need_b:
        # y = kx + b
        k = (mxy - my * mx) / (mx2 - mx ** 2)
        print(f"k = ({mxy} - {my} * {mx}) / ({mx2} - {mx}**2) = {k}")
        b = my - k * mx

        sigma_k = (1 / n ** 0.5) * ((my2 - my ** 2) / (mx2 - mx ** 2) - k ** 2) ** 0.5
        sigma_b = sigma_k * (mx2 - mx * mx) ** 0.5
        return x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b
    else:
        # y = kx
        k = mxy / mx2

        sigma_k = (1 / n ** 0.5) * (my2 / mx2 - k ** 2) ** 0.5

        return x, y, sigma_x, sigma_y, k, sigma_k


# for important settings
max_x = -1e9
max_y = -1e9
min_x = 1e9
min_y = 1e9


# x = 1/T
# y = ln(P)


# heating

P_1 = np.array([7.84316, 7.85098, 7.88419, 7.97767, 8.05260, 8.11235, 8.18931, 8.24338,
                8.30462, 8.35764, 8.40800, 8.47421, 8.52578, 8.57608, 8.63114, 8.69008, 8.76050, 8.79645])

T_1 = np.array([0.0033766, 0.0033652, 0.0033539, 0.0033427, 0.0033316, 0.0033205, 0.0033095, 0.0032986, 0.0032877,
                0.0032770, 0.0032663, 0.0032556, 0.0032451, 0.0032346, 0.0032241, 0.0032138, 0.0032035, 0.0031933])

sigma_P1 = np.array([])

sigma_T1 = np.array([])

x1, y1, sigma_x1, sigma_y1, k1, sigma_k1, b1, sigma_b1 = getting_k_b_from_data(T_1, P_1, sigma_T1, sigma_P1, True)


# cooling

P_2 = np.array([8.78325, 8.68558, 8.57482, 8.45310, 8.33869, 8.18931, 8.10230, 7.97996])

T_2 = np.array([0.0032035, 0.0032241, 0.0032451, 0.0032663, 0.0032877, 0.0033095, 0.0033316, 0.0033539])

sigma_P2 = np.array([])

sigma_T2 = np.array([])

x2, y2, sigma_x2, sigma_y2, k2, sigma_k2, b2, sigma_b2 = getting_k_b_from_data(T_2, P_2, sigma_T2, sigma_P2, True)


max_x, min_x = max(x2.max(), max_x), min(x2.min(), min_x)
max_y, min_y = max(y2.max(), max_y), min(y2.min(), min_y)


x_start, x_end = 0, int(1.5*max_x)
y_start, y_end = 0, int(1.5*max_y)


fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\ln{P}$")
plt.xlabel("$1/T$")
plt.grid(True, linestyle="--")
plt.axis([0.00315, 0.0034, 7.25, 9.5])
# plt.imshow(10*np.random.rand(5,3), aspect="auto")

dots = np.array([0., 10000])


plt.plot(dots, k1 * dots + b1, "-r", linewidth=0.7,
         label="Линейная аппроксимация для нагревания" % (k1)) # $\Delta T = %.2f N$" % (k1)
plt.plot(dots, k2 * dots + b2, "-b", linewidth=0.7,
         label="Линейная аппроксимация для охлаждения" % (k2)) # $\Delta T = %.2f N$" % (k2)

plt.plot(x1, y1, "+r", label="Экспериментальные точки для нагревания", ms=10)
plt.plot(x2, y2, "+b", label="Экспериментальные точки для охлаждения", ms=10)


plt.legend()
plt.show()


print("k1: ", k1, "\sigma: ", sigma_k1, "\\varepsilon: ", sigma_k1 * 100 / k1)
print("b1: ", b1, "\sigma: ", sigma_b1, "\\varepsilon: ", sigma_b1 * 100 / b1)
print("k2: ", k2, "\sigma: ", sigma_k2, "\\varepsilon: ", sigma_k2 * 100 / k2)
print("b2: ", b2, "\sigma: ", sigma_b2, "\\varepsilon: ", sigma_b2 * 100 / b2)