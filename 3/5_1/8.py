import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


U_p = [26.02, 22.96, 22.86, 22.11, 22.45, 23.14, 24.49, 35.37, 24.90, 23.12, 22.00, 22.11, 22.74, 22.90, 26.29]
I_p = [0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.3, 2.0, 1.7, 1.4, 1.1, 0.8, 0.5]

print(" & ".join([str(i) for i in U_p[:8]]).replace(".", ","))
print(" & ".join([str(i) for i in I_p[:8]]).replace(".", ","))

print(" & ".join([str(i) for i in U_p[8:]]).replace(".", ","))
print(" & ".join([str(i) for i in I_p[8:]]).replace(".", ","))

I_p1 = I_p[:8]
U_p1 = U_p[:8]

I_p2 = I_p[8:]
U_p2 = U_p[8:]


y1_data = np.array(I_p1)
x1_data = np.array(U_p1)

y2_data = np.array(I_p2)
x2_data = np.array(U_p2)

max_r = -1e12
for i in range(len(U_p) - 1):
    max_r = max(max_r,
                (U_p[i] - U_p[i + 1]) / (I_p[i] - I_p[i + 1])
                )
max_r *= 1000
print(max_r)


plt.figure(figsize=(8, 5))
plt.scatter(x1_data, y1_data, color='blue', s=22, label='ВАХ газового разряда при возрастании')
plt.scatter(x2_data, y2_data, color='red', s=22, label='ВАХ газового разряда при убывании')

# plt.plot(x_model, y1_model, color='blue', label='Аппроксимация для $R_1$')
# plt.plot(x_model, y2_model, color='red', label='Аппроксимация для $R_2$')
# plt.axhline(y=1/np.sqrt(2), color='blue')

# Title and labels
# plt.title('Frequency Response Curve', color='blueviolet', fontweight='bold')
plt.xlabel('$U_p, В$')
plt.ylabel('$I_p, мА$')

# Grid and legend
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()