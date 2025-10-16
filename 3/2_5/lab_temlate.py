import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.odr import ODR, Model, RealData

# x -- ток накала I_H
# y = np.array([0.98, 0.71, 0.52, 0.41, 0.26, 0.24, 0.22, 0.18, 1.48, 1.63, 1.74, 1.89, 1.99, 2.12, 2.12, 2.21])  # координаты по оси Y
y = np.array([-0.98, -0.71, -0.52, -0.41, -0.26, -0.24, -0.22, -0.18, -1.48, -1.63, -1.74, -1.89, -1.99, -2.12, -2.12,
              -2.21])  # координаты по оси Y
x = np.array([6.29, 6.58, 6.87, 7.16, 7.45, 7.74, 8.03, 8.32, 5.89, 5.78, 5.67, 5.56, 5.45, 5.34, 5.23,
              5.12])  # координаты по оси X

# Погрешности по х
x_err_syst = 0.035  # зависит от прибора
x_cena_delenia = 0  # величина одной клетки ЗАМЕНИТЬ НУЛЬ, ЕСЛИ ЕСТЬ ОШИБКА ЗАМЕРА РУКАМИ
x_err_analog = 1 / 2 * x_cena_delenia / x
x_err = (x_err_syst + x_err_analog) * x

# Погрешности по у
y_err_syst = 0.04  # зависит от прибора
y_cena_delenia = 0  # величина одной клетки ЗАМЕНИТЬ НУЛЬ, ЕСЛИ ЕСТЬ ОШИБКА ЗАМЕРА РУКАМИ
y_err_analog = 1 / 2 * y_cena_delenia / y
y_err = abs((y_err_syst + y_err_analog) * y)


# Определение теоретической функции
def teor_func(params, x):
    Q = params[0]
    phi_offset = params[1]
    omega_0 = 6500  # кГц
    omega = x * 1000  # кГц
    delta = omega / omega_0 - omega_0 / omega
    phi = np.arctan(Q * delta) + phi_offset
    return phi


# Создание объекта теоретической функции
func = Model(teor_func)

# Экспериментальные данные с погрешностями
data = RealData(x, (y - (np.pi - 2.21)), sx=x_err, sy=y_err)

# Начальное приближение параметров
beta0 = [3.7, np.pi / 4]  # Начальные значения для Q и phi_offset

# Создание объекта ODR и выполнение аппроксимации
odr = ODR(data, func, beta0=beta0)
output = odr.run()

# Получение аппроксимированных параметров
params = output.beta
print(f"Аппроксимированные параметры: Q = {params[0]:.4f}")

# Получение теоретических значений y
y_teor = teor_func(params, x)

# Разность теоретического и экспериментального значения по у (для хи квадрата)
delta_y = output.eps

# Разность теоретического и экспериментального значения по х (для хи квадрата)
delta_x = output.delta

# Вычисление хи квадрата
chi_square = np.sum((delta_x / x_err) ** 2 + (delta_y / y_err) ** 2)
print(f"Значение χ²: {chi_square:.4f}")

# Вычисление числа степеней свободы, N -- количество замеров, M -- количество параметров
N = len(x)
M = len(params)
degrees_of_freedom = abs(N - M)

# Вычисление редуцированного хи квадрата
reduced_chi_square = chi_square / degrees_of_freedom
print(f"Значение редуцированного χ²: {reduced_chi_square:.4f}")

# Автоматический расчёт хи квадратов
auto_chi_square = output.sum_square
auto_chi_square_red = output.res_var

# Построение графика
fig = plt.figure(figsize=(8, 9 / 2), dpi=300)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
ax = fig.add_subplot(111)

# Построение аппроксимированной функции
x_fit = np.linspace(min(x), max(x), 1000)
ax.plot(x_fit, teor_func(params, x_fit), color='red', label='_nolegend_')

# Отображение точек с погрешностями
ax.errorbar(x, y - (np.pi - 2.21), xerr=x_err, yerr=y_err, fmt='.', color='black', label='_nolegend_')

ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))

plt.subplots_adjust(bottom=0.2)

plt.grid(which='major', alpha=1)
plt.grid(which='minor', linestyle=':', alpha=0.5)
plt.xlabel(r'$\varphi$', fontsize=25)
plt.ylabel(r'$\omega$', rotation=90, fontsize=25)

legend_text = (
    # f"$\chi^2$: {chi_square:.4f}\n"
    # f"Редуцированный $\chi^2$: {reduced_chi_square:.4f}\n"
    # f"Q: {params[0]:.4f}"
    # f"Автоматически рассчитанный $\chi^2$: {auto_chi_square:.4f}\n"
    # f"Автоматически рассчитанный $\chi^2$: {auto_chi_square_red:.4f}\n"
    f"\n"
    f"$\chi^2$: {chi_square:.2f}\n"
    r"$\chi^2_{red}$:"
    f" {reduced_chi_square:.2f}\n\n"

    f"\n"
    f"$\chi^2$: {auto_chi_square:.2f}\n"
    r"$\chi^2_{red}$:"
    f" {auto_chi_square_red:.2f}"

    # f"Q: {params[0]:.2f}\n"
)
plt.text(1.45, 1, legend_text, fontsize=12, va='top', ha='right', bbox=dict(facecolor='white', alpha=1))
plt.show()
