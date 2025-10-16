import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from useful.base import getting_k_b_from_data

# 20
x = [21.4, 18.5, 16.3, 14.6, 13.3, 12.1, 11.2, 10.3, 9.6, 9.0]
I = [2.053, 2.045, 2.037, 2.028, 2.020, 2.012, 2.004, 1.996, 1.988, 1.980]


x_data, y_data, k, sigma_k, b, sigma_b = getting_k_b_from_data(x, I, None, None, need_b=True, no_sigma=True)

print("k: ", k, "\\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)


plt.figure(figsize=(8, 5))

dots = np.array([min(x), max(x)])

plt.plot(dots, dots * k + b, color='red', linewidth=0.8, label='Наилучшая прямая')
plt.scatter(x_data, y_data, color='blue', s=12, label='Эксперементальные точки')
# plt.scatter(x, I, color='green', s=12, label='Эксперементальные точки')
# plt.plot(x_model, y_model, color='red', label='Вольт амперная характеристика')

# Title and labels
plt.ylabel('$I, мкА$')
plt.xlabel('$x, см$')

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
# plt.show()

# 23

x_max = np.array([13.5, 12.9, 13.4, 12.4, 12.6, 11.5, 11.7, 10.5, 9, 6.7, 5.8, 5.2, 4.3, 3.2])
R = np.array([50, 45, 40, 35, 30,25, 20, 15, 10, 5, 4, 3, 2, 1])


R_0 = 450
x_data = 1/(1000 * R + R_0)
y_data = x_max


def f(x, a, b, c):
    return np.exp(a*x ) * b + c


popt, *pcov = curve_fit(f, x_data, y_data, p0=(1, 1, 1))


x_model = np.linspace(min(x_data), max(x_data), 1000)
y_model = f(x_model, popt[0], popt[1], popt[2])

l0 = 14.4

RR_0 = 50*np.log((l0 - popt[2]) / popt[1]) / popt[0]
print(RR_0)

print((1/RR_0 - R_0) /1000)




plt.figure(figsize=(8, 5))


plt.scatter(x_data, y_data, color='blue', s=12, label='Эксперементальные точки')
plt.plot(x_model, y_model, color='red', label='аппроксимация')

# Title and labels
plt.ylabel('$x_{max}, см$')
plt.xlabel('$\\frac{1}{R + R_0}, Ом^{-1}$')

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()