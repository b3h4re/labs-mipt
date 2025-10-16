import numpy as np
import matplotlib.pyplot as plt


def getting_needed_format_linear(x: list, y: list, sigma_x: list, sigma_y: list):
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

    sigma_k = (1 / n ** 0.5) * (my2 / mx2 - k ** 2) ** 0.5

    return x, y, sigma_x, sigma_y, k, sigma_k


n = list(range(1, 7+1))

# cuprum

f_n_cu = [3218.7, 6444.2, 9663.7, 12890.0, 16105.0, 19308.0, 22472.0]
sigma_f_cu = [0.3] * len(n)
sigma_n = [0] * len(n)

x_cu, y_cu, sigma_x_cu, sigma_y_cu, k_cu, sigma_k_cu = getting_needed_format_linear(n, f_n_cu, sigma_n, sigma_f_cu)

# steel

f_n_fe = [4128.6, 8285.1, 12400.0, 16529.0, 20653.0, 24772.0, 28882.0]
sigma_f_fe = [0.3] * len(n)
sigma_n = [0] * len(n)

x_fe, y_fe, sigma_x_fe, sigma_y_fe, k_fe, sigma_k_fe = getting_needed_format_linear(n, f_n_fe, sigma_n, sigma_f_fe)

# aluminum

f_n_al = [4246.2, 8514.2, 12742.0, 16998.0, 21225.0, 25453.0, 29662.0]
sigma_f_al = [0.3] * len(n)
sigma_n = [0] * len(n)

x_al, y_al, sigma_x_al, sigma_y_al, k_al, sigma_k_al = getting_needed_format_linear(n, f_n_al, sigma_n, sigma_f_al)

np.polyfit(x_al, y_al, 1)

plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$f_n$, $Гц$")
plt.xlabel("$n$, $ед$")
plt.grid(True, linestyle="--")
plt.axis([0, 10, 0, 30000])
dots = np.array([0., 10000])

plt.plot(dots, k_cu * dots, "-r", linewidth=0.7,
         label="Линейная аппроксимация для меди $f_n = %.3f P$" % (k_cu))
plt.plot(dots, k_fe * dots, "-b", linewidth=0.7,
         label="Линейная аппроксимация для стали $f_n = %.3f P$" % (k_fe))
plt.plot(dots, k_al * dots, "-g", linewidth=0.7,
         label="Линейная аппроксимация для дюралюминия $f_n = %.3f P$" % (k_al))

plt.plot(x_cu, y_cu, "+r", label="Экспериментальные точки для меди", ms=10)
plt.plot(x_fe, y_fe, "+b", label="Экспериментальные точки для стали", ms=10)
plt.plot(x_al, y_al, "+g", label="Экспериментальные точки для дюралюминия", ms=10)

plt.errorbar(x_cu, y_cu, xerr=sigma_x_cu, yerr=sigma_y_cu, fmt="ok", label="Экспериментальные точки", ms=3)
plt.errorbar(x_fe, y_fe, xerr=sigma_x_cu, yerr=sigma_y_cu, fmt="ok", label="Экспериментальные точки", ms=3)
plt.errorbar(x_al, y_al, xerr=sigma_x_cu, yerr=sigma_y_cu, fmt="ok", label="Экспериментальные точки", ms=3)

plt.legend()
plt.show()

print("k_cu: ", k_cu, "\sigma: ", sigma_k_cu, "\\varepsilon: ", sigma_k_cu*100 / k_cu)
print("k_fe: ", k_fe, "\sigma: ", sigma_k_fe, "\\varepsilon: ", sigma_k_fe*100 / k_fe)
print("k_al: ", k_al, "\sigma: ", sigma_k_al, "\\varepsilon: ", sigma_k_al*100 / k_al)