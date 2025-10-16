import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data, default_plot

calib_k, sigma_ck, calib_b, sigma_cb = None, None, None, None


def p_6():
    global calib_k, sigma_ck, calib_b, sigma_cb
    I = np.array([0.0, 0.4, 0.6, 1.0, 1.3, 1.6, 2.0, 2.3, 2.4])
    B = np.array([0.14, 0.25, 0.31, 0.42, 0.50, 0.61, 0.72, 0.81, 0.82])

    x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(I, B, [], [])
    calib_k, sigma_ck = k, sigma_k
    calib_b, sigma_cb = b, sigma_b

    default_plot(x, y, [-0.1, 2.5, 0, 0.9], "$B, Тл$", "$I, А$", k, sigma_k, b, sigma_b)


def p_7():
    global calib_k, sigma_ck, calib_b, sigma_cb
    I = [
        np.array([0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4]),
        np.array(list(reversed([0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4])))
    ]
    B = [calib_k * I[0], calib_k * I[1]]

    B2 = [B[0] * B[0], B[1] * B[1]]

    F = [
        np.array([0, 20, 49, 88, 128, 186, 245, 304]),  # Aluminum
        np.array([324, 265, 196, 137, 88, 49, 20, 0]),  # Aluminum reverse
        np.array([20, 78, 177, 294, 461, 647, 863, 1099]),  # W
        np.array([1099, 912, 697, 510, 334, 196, 88, 29]),  # W reverse
        np.array([98, 216, 334, 422, 461, 471, 441, 373]),  # C4
        np.array([373, 432, 481, 481, 451, 383, 255, 137])  # C4 reverse
    ]
    names = [
        "алюминия", "алюминия в обратном порядке",
        "вольфрама", "вольфрама в обратном порядке",
        "графита", "графита в обратном порядке"
    ]
    colors = [
        "r", "r", "b", "b", "g", "g"
    ]

    axis = [0, 0.7, -10, 1200]

    fig = plt.figure(figsize=(8, 6), dpi=100)
    plt.ylabel("$F, мН$")
    plt.xlabel("$B^2, Тл^2$")
    plt.grid(True, linestyle="--")
    plt.axis(axis)
    dots = np.array([-10000, 10000])

    for i in range(len(F) - 2):
        x, y, sigma_x, sigma_y, k, sigma_k = getting_k_b_from_data(B2[i % 2], F[i], [], [], need_b=False)
        print(names[i])
        print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
        # print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)
        plt.plot(dots, k * dots, f"-{colors[i]}", linewidth=0.8,
                 label=f"Линейная аппроксимация для {names[i]}" % (k) if i % 2 == 0 else "")  # $\Delta T = %.2f N$" % (k1)

        plt.plot(x, y, f"+{colors[i]}", ms=10)

    x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(B2[0][:4], F[4][:4], [], [])
    print(names[4])
    print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
    print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)

    plt.plot(dots, k * dots + b, f"-{colors[4]}", linewidth=0.8,
             label=f"Линейная аппроксимация для {names[4]}" % (k))  # $\Delta T = %.2f N$" % (k1)
    plt.plot(B2[0], F[4], f"+{colors[4]}", ms=10)

    x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b = getting_k_b_from_data(B2[0][:3], F[5][:3], [], [])
    print(names[5])
    print("k: ", k, "\sigma: ", sigma_k, "\\varepsilon: ", sigma_k * 100 / k)
    print("b: ", b, "\sigma: ", sigma_b, "\\varepsilon: ", sigma_b * 100 / b)
    plt.plot(dots, k * dots + b, f"-{colors[5]}", linewidth=0.8)  # $\Delta T = %.2f N$" % (k1)
    plt.plot(B2[0], F[5], f"+{colors[5]}", ms=10)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    p_6()
    p_7()
