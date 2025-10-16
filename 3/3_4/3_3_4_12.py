import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data

B = np.array([0.19, 0.36, 0.55, 0.73, 0.88, 1.00, 1.09, 1.16])
I_M_B = np.array([0.19, 0.37, 0.56, 0.75, 0.93, 1.13, 1.3, 1.5])

xb, yb, sigma_xb, sigma_yb, kb, sigma_kb, bb, sigma_bb = getting_k_b_from_data(I_M_B, B, [], [])


I = [0.46, 0.55, 0.64, 0.73, 0.82, 0.91, 1.00]
I_M = np.array([0.25, 0.50, 0.75, 1.00, 1.25, 1.50])

U_34s = [
    np.array([1.49, 3.04, 4.44, 5.65, 6.41, 6.92]),
    np.array([1.76, 3.60, 5.31, 6.68, 7.61, 8.22]),
    np.array([2.12, 4.25, 6.19, 7.82, 8.86, 9.58]),
    np.array([2.37, 4.87, 7.04, 8.87, 10.11, 10.92]),
    np.array([2.63, 5.35, 7.85, 9.98, 11.35, 12.26]),
    np.array([2.88, 5.99, 8.77, 11.07, 12.58, 13.61]),
    np.array([3.22, 6.61, 9.68, 12.19, 13.83, 14.95])
]

B_34 = kb*I_M + bb

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$k, В/Тл$")
plt.xlabel("$I, мА$")
plt.grid(True, linestyle="--")
plt.axis([0.3, 1.1, 5, 14])
dots = np.array([0., 10000])

colors = ["r", "b", "g", "c", "m", "y", "r"]
ks = []
sigma_ks = []

i = 0
for U_34 in U_34s:
    x, y, sigma_x, sigma_y, k, sigma_k = getting_k_b_from_data(B_34, U_34, [], [], need_b=False)
    ks.append(k)
    sigma_ks.append(sigma_k)

    # plt.plot(dots, k * dots, f"-{colors[i]}", linewidth=0.8, label=f"I = {I[i]} A" % (k))  # $\Delta T = %.2f N$" % (k1)
    # plt.plot(x, y, f"+{colors[i]}", label="Экспериментальные точки", ms=4)
    i += 1


# plt.legend()
# plt.show()

ks = np.array(ks)
I = np.array(I)

x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(I, ks, [], [])

plt.plot(dots, k * dots, linewidth=0.8, label=f"Линейная аппроксимация" % (k)) # $\Delta T = %.2f N$" % (k1)
plt.plot(x, y, "+r", label="Экспериментальные точки", ms=10)

print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

plt.legend()
plt.show()