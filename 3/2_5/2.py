import numpy as np
import matplotlib.pyplot as plt
from math import e, log, pi
from useful.base import getting_k_b_from_data, default_plot


theta = np.array([0.350449637, 0.495128421, 0.627577082, 0.831756479, 1.070033082, 1.032727650, 1.562185028])


R_L = (23.168 + 23.243 + 24.160) / 3
R = np.array([408.4, 680.6, 952.9, 1225.2, 1497.5, 1769.7, 2042.0])

X = 1/(R + R_L)**2
Y = 1/theta**2

print(X)
print(Y)


x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(X[4::2], Y[4::2], [], [])
default_plot(X, Y, [0, 0.000007, 0, 10], "$1/\\theta^2$", "$1/R_\Sigma^2, Ом^{-2}$", k, sigma_k, b, sigma_b)


r = 2 * pi * k**0.5
print(r, 2 * pi / k**0.5)