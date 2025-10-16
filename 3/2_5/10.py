import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import pi


nu_0 = 5.92

L = 0.1
C = 6 * 10**-9

nu = np.array([5.26, 5.35, 5.44, 5.53, 5.62, 5.71, 5.80, 5.89, 5.98, 6.07, 6.16, 6.25, 6.34, 6.43, 6.52, 6.61, 6.70, 6.79, 6.88, 6.97, 7.06])
U_1 = np.array([3.56, 4.06, 4.76, 5.46, 6.26, 7.26, 8.12, 8.74, 8.92, 8.66, 8.06, 7.38, 6.60, 6.00, 5.50, 5.08, 4.62, 4.28, 4.02, 3.82, 3.62])
U_2 = np.array([1.89, 1.95, 2.03, 2.08, 2.15, 2.20, 2.26, 2.30, 2.33, 2.33, 2.35, 2.31, 2.31, 2.31, 2.32, 2.34, 2.34, 2.31, 2.30, 2.26, 2.21])

x_data = nu / nu_0
y1_data = U_1 / U_1[10]
y2_data = U_2 / U_2[10]

f = lambda x, shift, compress, rais: np.arctan(-compress*(x-shift))/pi + rais


popt1, *pcov = curve_fit(f, x_data, y1_data, p0=(0, 1, 0))
popt2, *pcov = curve_fit(f, x_data, y2_data, p0=(0, 1, 0))
print(popt1)
print(popt2)


x_model = np.linspace(min(x_data), max(x_data), 1000)
y1_model = f(x_model, popt1[0], popt1[1], popt1[2])
y2_model = f(x_model, popt2[0], popt2[1], popt2[2])


plt.figure(figsize=(8, 5))
plt.scatter(x_data, y1_data, color='blue', s=22, label='Экспериментальные точки для $R_1$')
plt.scatter(x_data, y2_data, color='red', s=22, label='Экспериментальные точки для $R_2$')
plt.plot(x_model, y1_model, color='blue', label='Аппроксимация для $R_1$')
plt.plot(x_model, y2_model, color='red', label='Аппроксимация для $R_2$')
plt.axhline(y=1/np.sqrt(2), color='blue')

# Title and labels
# plt.title('Frequency Response Curve', color='blueviolet', fontweight='bold')
plt.xlabel('$\\nu / \\nu_0$')
plt.ylabel('$U / U_0$')

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()