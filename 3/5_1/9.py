import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


def clear_from_nans(arr):
    arr = np.array(arr)
    arr = arr[~np.isnan(arr)]
    return arr


def centralize(x_data: np.array, y_data: np.array):
    x0 = np.mean(x_data)
    y0 = np.mean(y_data)
    x_data -= x0
    y_data -= y0


def neg(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]
    return arr


data = pd.read_csv('data.csv')
x = []
y = []

U_z = []
I_z = []

# I_p = 2 mA
U_z.append(clear_from_nans(list(data[f'U+{1}, В']) + list(-data[f'U-{1}, В'])))
I_z.append(clear_from_nans(list(data[f'I+{1}, мкА']) + list(-data[f'I-{1}, мкА'])))


# I_p = 1.5 mA
U_z.append(U_z[0])
I_z.append(clear_from_nans(list(data[f'I+{2}, мкА']) + list(-data[f'I-{2}, мкА'])))

# I_p = 0.84 mA
U_z.append(U_z[0])
I_z.append(clear_from_nans(list(data[f'I+{3}, мкА']) + list(-data[f'I-{3}, мкА'])))


plt.figure(figsize=(8, 5))

for i in range(len(U_z)):
    # print(" & ".join([str(i) for i in U_z1[i]]).replace(".", ","))
    # print(" & ".join([str(i) for i in I_z1[i]]).replace(".", ","))
    #
    # print(" & ".join([str(i) for i in reversed(U_z2[i])]).replace(".", ","))
    # print(" & ".join([str(i) for i in reversed(I_z2[i])]).replace(".", ","))

    x.append(np.array(U_z[i]))
    y.append(np.array(I_z[i]))


colors = [
    "blue",
    "red",
    "green"
]


def volt(u, a, b, c):
    return a * np.tanh(b * u) + c * u


I_p = [2, 1.5, 0.84]

labels = [f"ВАХ двойного зонда при $I_p = {I_p[i]} мА$" for i in range(len(I_p))]


for i in range(len(x)):
    x[i] -= x[i][len(x[i])//2]
    y[i] -= y[i][len(y[i]) // 2]
    x[i] = -x[i]
    y[i] = -y[i]

    popt, *pcov = curve_fit(volt, xdata=x[i], ydata=y[i], p0=(1, 1, 1))
    print(popt, labels[i])

    x_model = np.linspace(min(x[i]), max(x[i]), 1000)
    if i == 0:
        y_model = volt(x_model, 300, 0.06, -3)
    else:
        y_model = volt(x_model, popt[0], popt[1], popt[2])

    plt.plot(x_model, y_model, color=colors[i])

    plt.scatter(x[i], y[i], color=colors[i], s=22, label=labels[i])


# Title and labels
# plt.title('Frequency Response Curve', color='blueviolet', fontweight='bold')
plt.xlabel('$U_p, В$')
plt.ylabel('$I_p, мА$')

# plt.axis([17, -13, 90, -125])

# Grid and legend
plt.axhline(0, color="black")
plt.axvline(0, color="black")


plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()
