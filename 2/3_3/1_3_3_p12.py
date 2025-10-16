import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


# Клоунский ввод данных, но пусть будет
data = {
    1: [[81, 41, 11, 0], [50, 40, 30, 11], [79.4, 63.5, 47.6, 60.4], [-10, 100, 30, 100]],
    2: [[80.5, 40.5, 10.5, 0], [50, 40, 30, 10.5], [31.8, 27.0, 20.6, 27.0], [-10, 100, 10, 50]]
}


for n in [1, 2]:
    X, L, P, ranges = data[n]
    # X = np.array(X)
    # L = np.array(L)
    # P = np.array(P)

    x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = (
        getting_k_b_from_data(x=X[:3], y=P[:3], sigma_x=[], sigma_y=[], need_b=True))

    print(f"k: {k}, b: {b}, sigma_k: {sigma_k}, sigma_b: {sigma_b}")
    print()

    fig = plt.figure(figsize=(8, 6), dpi=100)
    plt.xlabel("$x, см$")
    plt.ylabel("$P, Па$")
    plt.grid(True, linestyle="--")
    plt.axis(ranges)
    # plt.imshow(10*np.random.rand(5,3), aspect="auto")

    dots = np.array([0., 10000])

    plt.plot(dots, k * dots + b, "-r", linewidth=0.7,
             label="Линейная аппроксимация для ламинарного течения" % (k)) # $\Delta T = %.2f N$" % (k1)

    plt.plot(x, y, "+r", label=f"Экспериментальные точки для ламинарного течения", ms=10)
    plt.plot(X[-1], P[-1], "+b", label=f"Экспериментальные точки для турбулентного течения", ms=10)

    plt.legend()
    plt.show()