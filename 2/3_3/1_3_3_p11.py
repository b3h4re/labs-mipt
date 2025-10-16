import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data


data_file_names = ["data_1-p-q.data", "data_2-p-q.data"]
ranges = {
    "data_1-p-q.data": [0, 400, 0.2, 8.5],
    "data_2-p-q.data": [0, 400, 1, 17.5]
}


for data_file_name in data_file_names:
    data_file = open(data_file_name, "r")
    laminar = int(data_file.readline())
    Q1_all = list(map(float, data_file.readline().split()))
    P1_all = list(map(float, data_file.readline().split()))
    data_file.close()

    Q1_lam = np.array(Q1_all[:laminar + 1])
    P1_lam = np.array(P1_all[:laminar + 1])
    print(Q1_lam)

    Q1_turb = np.array(Q1_all[laminar:])
    P1_turb = np.array(P1_all[laminar:])
    print(Q1_turb)


    x_lam, y_lam, sigma_x_lam, sigma_y_lam, k_lam, sigma_k_lam, b_lam, sigma_b_lam = (
        getting_k_b_from_data(x=P1_lam, y=Q1_lam, sigma_x=[], sigma_y=[], need_b=True))

    x_turb, y_turb, sigma_x_turb, sigma_y_turb, k_turb, sigma_k_turb, b_turb, sigma_b_turb = (
        getting_k_b_from_data(x=P1_turb, y=Q1_turb, sigma_x=[], sigma_y=[], need_b=True))

    print(f"lam k: {k_lam}, b: {b_lam}, sigma_k: {sigma_k_lam}, sigma_b: {sigma_b_lam}")
    print(f"turb k: {k_turb}, b: {b_turb}, sigma_k: {sigma_k_turb}, sigma_b: {sigma_b_turb}")
    print()

    fig = plt.figure(figsize=(8, 6), dpi=100)
    plt.ylabel("$Q, л/мин$")
    plt.xlabel("$\Delta P, Па$")
    plt.grid(True, linestyle="--")
    plt.axis(ranges[data_file_name])

    dots = np.array([0., 10000])


    plt.plot(dots, k_lam * dots + b_lam, "-r", linewidth=0.7,
             label="Линейная аппроксимация для ламинарного течения" % (k_lam)) # $\Delta T = %.2f N$" % (k1)

    plt.plot(dots, k_turb * dots + b_turb, "-b", linewidth=0.7,
             label="Линейная аппроксимация для турбулентного течения" % (k_lam)) # $\Delta T = %.2f N$" % (k1)

    plt.plot(x_lam, y_lam, "+r", label="Экспериментальные точки для ламинарного течения", ms=10)
    plt.plot(x_turb, y_turb, "+b", label="Экспериментальные точки для турбулентного течения", ms=10)


    plt.legend()
    plt.show()
