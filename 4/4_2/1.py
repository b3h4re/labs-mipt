import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


y = np.array(list(reversed([-0.3247, -0.3314, -0.3466, -0.3471, -0.3479, -0.3856, -0.4194, -0.4386, -0.4400, -0.4568, -0.4604])))
lambdas = np.array([404.7, 404.7, 404.7, 404.7, 404.7, 491.6, 546.1, 577, 577, 640, 640])


plt.figure(figsize=(8, 5))
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.xlabel("$\\lambda$, нм")
plt.ylabel("$\sin{\phi_m} - \sin{\psi}$")

plt.plot(lambdas, y, "+r", label=f"Экспериментальные точки", ms=10)

x, y, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(lambdas[2:], y[2:], [], [], need_b=True)
dots = np.array([390, 650])
plt.plot(dots, k * dots + b, f"-b", linewidth=0.7, label=f"$k = ({"{:.5f}".format(k)} \\pm {"{:.5f}".format(sigma_k)})$" % (k))

print(k, sigma_k)
print(1 / k)
print(1 / k * (sigma_k / k) ** 2)

plt.legend()
plt.show()