import numpy as np
from math import log
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


p_lim = 0.87

# Input data
worse = [f"worse-{i}.data" for i in [1, 2]]
better = [f"better-{i}.data" for i in [1, 2]]
color = {
    worse[0]: "r",
    worse[1]: "b",
    better[0]: "r",
    better[1]: "b"
}

p, t, x, y, k, sigma_k, b, sigma_b = [{} for _ in range(8)]

for f in worse + better:
    p[f] = []
    t[f] = []
    x[f] = []
    y[f] = []
    k[f] = []
    sigma_k[f] = []
    b[f] = []
    sigma_b[f] = []

for file_name in worse + better:
    for t_, p_ in [tuple(map(float, x.strip().split('\t'))) for x in open(file_name, "r")]:
        try:
            p[file_name].append(log(abs(p_ - p_lim)))
            t[file_name].append(t_)
        except:
            pass
    p[file_name] = np.array(p[file_name])
    t[file_name] = np.array(t[file_name])
    x[file_name], y[file_name], k[file_name], sigma_k[file_name], b[file_name], sigma_b[file_name] = (
        getting_k_b_from_data(t[file_name], p[file_name], [], [], True, True))

# Worse graph


fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\ln (P - P_{пр})$")
plt.xlabel("$t$, $с$")
plt.grid(True, linestyle="--")
plt.axis([0, 60, -2, 2.5])

dots = np.array([0., 10000])

for f in worse:
    plt.plot(dots, k[f] * dots + b[f], "-"+color[f], linewidth=0.7,
             label=f"Линейная аппроксимация зависимости $f$ от $n$ для углекислого газа" % (k))
    plt.plot(x[f], y[f], "+"+color[f], label=f"Экспериментальные точки", ms=10)

plt.legend()
plt.show()

# Better graph

fig = plt.figure(figsize=(8, 6), dpi=100)
plt.ylabel("$\ln (P - P_{пр})$")
plt.xlabel("$t$, $с$")
plt.grid(True, linestyle="--")
plt.axis([0, 60, -7, 2.5])

dots = np.array([0., 10000])

for f in better:
    plt.plot(dots, k[f] * dots + b[f], "-"+color[f], linewidth=0.7,
             label=f"Линейная аппроксимация зависимости $f$ от $n$ для углекислого газа" % (k))
    plt.plot(x[f], y[f], "+"+color[f], label=f"Экспериментальные точки", ms=10)

plt.legend()
plt.show()