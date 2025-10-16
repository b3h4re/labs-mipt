import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def f(x, a, b, c):
    return a / (x + b) + c


nu = [333, 667, 1000, 1333, 1667, 2000, 2333]
kn = [0.333, 0.179, 0.125, 0.066, 0.075, 0.070, 0.045]

x_data = np.array(nu)

y_data = np.array(kn)


popt, *pcov = curve_fit(f, x_data, y_data, p0=(1, 0.02, 0.1))

x_model = np.linspace(min(x_data), max(x_data), 1000)
y_model = f(x_model, popt[0], popt[1], popt[2])

plt.figure(figsize=(8, 5))
plt.axis([0, 2500, 0, 0.4])

dots = np.array([-100_000, 100_000])

plt.plot(x_model, y_model, color='red', label="Аппроксимация")
plt.plot(x_data, y_data, "+b", ms=10, label="Экспериментальные точки")


# Title and labels
plt.xlabel("$\\nu, кГц$")
plt.ylabel("$K_n$")

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
