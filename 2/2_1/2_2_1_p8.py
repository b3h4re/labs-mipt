import numpy as np
import matplotlib.pyplot as plt
from math import log
from useful.base import getting_k_b_from_data


# reading data from files
file_names = ["41_3.csv", "82_5.csv", "120.csv", "161_3.csv"]
T = {}
sigma_T = {}
V = {}
sigma_V = {}
for file_name in file_names:
    data = open(file_name, "r")
    time_f = []
    v_f = []
    for line in data.readlines():
        try:
            time, v = map(float, line.strip().split(','))
            time_f.append(time)
            v_f.append(v)
        except:
            pass
    data.close()

    sigma_T[file_name] = np.array([0.003 for _ in range(len(time_f))])
    sigma_V[file_name] = np.array([0.0003/v_f[j] for j in range(len(v_f))])
    T[file_name] = np.array(time_f)
    V[file_name] = np.array([log(v) for v in v_f])


# formatting data
x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = {}, {}, {}, {}, {}, {}, {}, {}

for i in file_names:
    x[i], y[i], sigma_x[i], sigma_y[i], k[i], sigma_k[i], b[i], sigma_b[i] = \
        getting_k_b_from_data(x=T[i], y=V[i], sigma_x=sigma_T[i], sigma_y=sigma_V[i], need_b=True)


# making graph
fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\ln{P}$")
plt.xlabel("$T, с$")
plt.grid(True, linestyle="--")
plt.axis([0, 600, 0, 3])
# plt.imshow(10*np.random.rand(5,3), aspect="auto")

display = {
    file_names[0]: "43,3 торр",
    file_names[1]: "82,5 торр",
    file_names[2]: "120 торр",
    file_names[3]: "161,3 торр"
}
dots = np.array([0., 10000])
for i in file_names:
    plt.plot(dots, k[i] * dots + b[i], linewidth=0.8,
             label=f"Линейная аппроксимация для {display[i]}" % (k[i])) # $\Delta T = %.2f N$" % (k1)
    print(f"k_{display[i]}: ", k[i], "\sigma: ", sigma_k[i], "\\varepsilon: ", sigma_k[i] * 100 / k[i])

    # plt.plot(x[i], y[i], label="Экспериментальные точки для нагревания", ms=1)


plt.legend()
plt.show()