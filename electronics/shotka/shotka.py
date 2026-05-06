import numpy as np
import matplotlib.pyplot as plt
from useful.base import getting_k_b_from_data
import os
from math import log10
from scipy.optimize import curve_fit

sdf = []

# вах cv
labels = {
    "1-Al-Al": "Алюминий-Алюминий Напыленный",
    "1-fusedAl-fusedAl-max_distance": "Вплавленный Алюминий Максимальная дистанция",
    "1-fusedAl-fusedAl-min_distance": "Вплавленный Алюминий Минимальная дистанция",
    "1-fusedAu-fusedAl": "Алюминий-Золото Вплавленные",
    "1-Al": "Алюминий Напыленный",
    "1-Au": "Золото Напыленное",
    "1-Au-melted": "Золото Вплавленное",
    "1-Al-fusedAl": "Алюминий - Вплавленный Алюминий",
    "1-Al-melted": "Флюминий Вплавленный"
}


def read_header(data_dir):
    header = data_dir + ".header"
    file = open(os.path.join(DATA_DIR, header))
    text = file.readlines()
    file.close()
    measurements = []
    for i in range(len(text)):
        if HEADER_SEP in text[i]:
            if i + 3 >= len(text):
                break
            m_type = text[i + 3].split()[-1]
            m_file = text[i + 8].split()[-1]
            measurements.append((m_type, m_file))
    return measurements


def read_data(data_file, m_type):
    data_file = data_file[1:].replace(f"{data_file[0]}", f"{BASE_DIR[0]}")
    data_file = os.path.join(DATA_DIR, data_file)
    file = open(data_file)
    text = file.readlines()
    file.close()
    start = 15 if m_type == "IV" else 21
    if m_type == "IV":
        bias, current, resistance = [], [], []
        for i in range(start + 1, len(text)):
            tmp = list(map(float, text[i].split()))
            bias.append(tmp[0])
            current.append(tmp[1])
            resistance.append(tmp[2])
        bias = np.array(bias)
        current = np.array(current)
        resistance = np.array(resistance)
        return  bias, current, resistance
    else:
        voltage, resistance, reactance, ac, freq = [], [], [], [], []
        for i in range(start + 1, len(text)):
            tmp = list(map(float, text[i].split()))
            try:
                voltage.append(tmp[0])
                resistance.append(tmp[1])
                reactance.append(tmp[2])
                ac.append(tmp[3])
                freq.append(tmp[4])
            except:
                pass
        voltage = np.array(voltage)
        resistance = np.array(resistance)
        reactance = np.array(reactance)
        ac = np.array(ac)
        freq = np.array(freq)
        return  voltage, resistance, reactance, ac, freq


def IofV(x, a, b, r):
    return a * (np.exp(b * (x +r)) - 1)


def plot_dc(data, measurement_name):
    bias, current, resistance = data
    voltage = current * resistance
    x = voltage
    # y = np.log10(np.abs(current))
    y = current

    popt, *pcov = curve_fit(IofV, x, y, p0=(-0.000005, -10, 0.001))
    print(popt)

    x_model = np.linspace(min(x), max(x), 1000)
    y_model = IofV(x_model, popt[0], popt[1], popt[2])


    print(measurement_name)
    plt.figure(figsize=(12, 6))
    plt.grid(True, linestyle="--")
    plt.xlabel("$V$, $В$")
    plt.ylabel("$\ln{I}$")
    plt.plot(x, y, "-r", label=f"ВАХ для контакта {labels[measurement_name]}")
    plt.plot(x_model, y_model, color="green", label=f"ВАХ для контакта {labels[measurement_name]}")

    # start, end = 300, 350
    # dots = np.array([0.2, 1])
    # if measurement_name == "1-Al":
    #     start, end = 150, 175
    # elif measurement_name == "1-Al-melted":
    #     start, end = 150, 175
    # try:
    #     ___, ____, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(x[start:end], y[start:end], [], [], need_b=True)
    #     plt.plot(dots, k * dots + b, "-b", linewidth=0.7,
    #              label=f"Линейная аппроксимация зависимости $y = {"{:.4f}".format(k)} * x + {"{:.4f}".format(b)}$" % (k))
    # except ZeroDivisionError:
    #     pass
    #
    # start, end = 50, 100
    # dots = np.array([-1, -0.2])
    # if measurement_name == "1-Al":
    #     start, end = 50, 75
    # elif measurement_name == "1-Al-melted":
    #     start, end = 50, 75
    # try:
    #     ___, ____, _, __, k, sigma_k, b, sigma_b = getting_k_b_from_data(x[start:end], y[start:end], [], [], need_b=True)
    #     plt.plot(dots, k * dots + b, "-b", linewidth=0.7,
    #              label=f"Линейная аппроксимация зависимости $y = {"{:.4f}".format(k)} * x + {"{:.4f}".format(b)}$" % (k))
    # except ZeroDivisionError:
    #     pass

    plt.legend()
    plt.show()


def plot_cv(data, measurement_name):
    voltage, resistance, reactance, ac, freq = data
    x = voltage
    c_0 = reactance[0]
    for i in range(len(voltage)):
        if voltage[i] < 0.00001:
            c_0 = reactance[i]
            break
    y = ((c_0 / reactance) ** 2) - 1

    print(measurement_name)
    plt.figure(figsize=(12, 6))
    plt.grid(True, linestyle="--")
    plt.xlabel("$V$, $В$")
    plt.ylabel("$\\left( C_0 / C \\right)^2 - 1$")
    plt.plot(x, y, "-r", label=f"CV для контакта {labels[measurement_name]} и частотой 10^{int(log10(np.mean(freq)))} Гц")

    plt.legend()
    plt.show()


BASE_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(BASE_DIR, 'gr4_306_14_02')
HEADER_SEP = "______________________________________________________"

dirs = []
headers = []

if __name__ == "__main__":
    for filepath in os.listdir(DATA_DIR):
        if os.path.isfile(os.path.join(DATA_DIR, filepath)):
            headers.append(filepath)
        else:
            dirs.append(filepath)



    for data_dir in dirs:
        if data_dir != "1-Al":
            continue
        measurements = read_header(data_dir)
        for m_type, m_file in measurements:
            data = read_data(m_file, m_type)
            if m_type == "IV":
                plot_dc(data, data_dir)
                pass
            else:
                plot_cv(data, data_dir)
                pass
