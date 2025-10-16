import numpy as np
import matplotlib.pyplot as plt
from math import e, log
from useful.base import getting_k_b_from_data, default_plot
from scipy.optimize import curve_fit


def p6():
    tau_0 = 9.045
    t0 = 273
    tau = np.array([10.7929, 10.693, 10.528, 10.21502, 9.878, 9.34852, 9.3002, 9.267, 9.244, 9.2253, 9.21023])

    t = np.array([286.8, 288.6, 290.7, 292.7, 294.6, 300.6, 302.6, 304.6, 306.6, 308.7, 310.6])

    # dropped bad points
    dropped_t = np.array([293.8, 295.5, 312.6])
    dropped_tau = np.array([9.545, 9.4184, 9.198824])

    dropped_tau = 1/(dropped_tau**2 - tau_0**2)
    tau = 1 / (tau ** 2 - tau_0 ** 2)

    # t_ = np.array([14.02, 16.01, 18.04, 20.07, 22.05, 24.01, 26.01, 28.07, 30.06, 32.05, 34.03, 36.03, 38.02, 40.00]) + t0

    start = 4
    finish = 14 - 2 - 2

    x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(t[start:finish], tau[start:finish], [], [])
    # default_plot(x, y, [280, 320, 0, 0.5], "$1/(\\tau^2 - \\tau_0^2), мкс^{-2}$", "$T, К$", k, sigma_k, b, sigma_b)

    fig = plt.figure(figsize=(8, 6), dpi=100)
    plt.ylabel("$1/(\\tau^2 - \\tau_0^2), мкс^{-2}$")
    plt.xlabel("$T, К$")
    plt.grid(True, linestyle="--")
    plt.axis([270, 320, 0, 0.5])
    dots = np.array([-10000, 10000])

    plt.plot(dots, k * dots + b, "-r", linewidth=0.8,
             label=f"Линейная аппроксимация" % (k))  # $\Delta T = %.2f N$" % (k1)
    plt.plot(t, tau, "+b", label="Экспериментальные точки", ms=10)

    plt.plot(dropped_t, dropped_tau, "+g", label="Выброшенные точки", ms=10)

    print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
    print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

    t_kuri = - b / k
    sigma_t_kuri = t_kuri * ((sigma_k/k)**2 + (sigma_b/b)**2)**0.5

    print(f"Температура Кюри = ({t_kuri} \\pm {sigma_t_kuri}) К")



    y_data = tau[:start]
    x_data = t[:start]

    params = [1, 1]

    d = 10000
    popt, *pcov = curve_fit((lambda x, k, c: k*e**(x/d) + c), x_data, y_data, p0=params)
    x_model = np.linspace(0, max(x_data), 100)
    k, c = popt[0], popt[1]
    y_model = k*e**(x_model/d) + c
    print(k, c)
    # y_model = ach(x_model, g)
    # plt.axhline(y=1 / sqrt(2))
    plt.scatter(x_data, y_data, s=22)
    plt.plot(x_model, y_model)
    print(log(e))

    print(f"Температура Кюри = ({log(-c/k) * d} \\pm {sigma_t_kuri}) К")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    p6()
