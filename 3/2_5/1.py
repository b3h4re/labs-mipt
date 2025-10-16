import numpy as np
import matplotlib.pyplot as plt
from math import e, log, pi
from useful.base import getting_k_b_from_data, default_plot


L = 0.1
C = np.array([0.7662414513, 1.7662414513, 2.7662414513, 3.7662414513, 4.7662414513, 5.7662414513, 6.7662414513,
              7.7662414513, 8.7662414513, 9.7662414513])


T_theor = 2 * pi * (L * C * 10**(-9)) ** 0.5   * 1000

T_exp = np.array([0.055, 0.0736, 0.0884, 0.101, 0.113, 0.122, 0.132, 0.143, 0.149, 0.159])

print(T_theor)
print(T_exp)

x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(T_theor, T_exp, [], [])
default_plot(T_theor, T_exp, [0, 0.2, 0, 0.2], "$T_{exp}$, мс", "$T_{theor}, мс$", k, sigma_k, b, sigma_b)


print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)