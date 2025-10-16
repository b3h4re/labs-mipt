import kwargs
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize


def lin(par, x):
    return par[0] * x + par[1]


x = np.arange(0, 250, 0.1)
y = np.arange(0, 800, 0.1)

X1 = np.array([114.67, 96.35, 87.07, 80.33, 71.57, 68.21, 126.6, 138.25, 119.75, 121.74])
Y1 = np.array([585, 495, 450, 415, 370, 350, 650, 710, 610, 625])
Xerr1 = []
for i in X1:
    Xerr1.append(i * 0.002 + 0.02)
Yerr1 = []
for i in Y1:
    Yerr1.append(i * 0.005 + 0.025)

X2 = np.array([121.81, 110.97, 100.26, 91.78, 82.68, 220.29, 200.13, 178.98, 163.13, 144.2])
Y2 = np.array([380, 350, 315, 290, 260, 690, 625, 560, 510, 450])

Xerr2 = []
for i in X2:
    Xerr2.append(i * 0.002 + 0.02)
Yerr2 = []
for i in Y2:
    Yerr2.append(i * 0.005 + 0.025)

X3 = np.array([122.04, 126.12, 145.08, 160.61, 176.16, 204.65, 228.01, 104.31, 90.84, 73.78])
Y3 = np.array([260, 265, 305, 340, 370, 430, 480, 220, 190, 155])

Xerr3 = []
for i in X3:
    Xerr3.append(i * 0.002 + 0.02)
Yerr3 = []
for i in Y3:
    Yerr3.append(i * 0.005 + 2.5)

# kb = fit(lin, [0, 0], X, Y)

# plt.plot(X, lin(kb, X), 'k', linewidth=1, label='N approximation')

A1 = np.vstack([X1, np.ones(len(X1))]).T
m1, c1 = np.linalg.lstsq(A1, Y1, rcond=None)[0]
plt.plot(x, m1 * x + c1, 'black', label='Fitted line')
plt.text(150, 710, '$l = 50$ см', c='red', fontsize=16)

A2 = np.vstack([X2, np.ones(len(X2))]).T
m2, c2 = np.linalg.lstsq(A2, Y2, rcond=None)[0]
plt.plot(x, m2 * x + c2, 'black', label='Fitted line')
plt.text(210, 610, '$l = 30$ см', c='green', fontsize=16)

A3 = np.vstack([X3, np.ones(len(X3))]).T
m3, c3 = np.linalg.lstsq(A3, Y3, rcond=None)[0]
plt.plot(x, m3 * x + c3, 'black', label='Fitted line')
plt.text(210, 360, '$l = 20$ см', c='blue', fontsize=16)

plt.errorbar(X1, Y1, xerr=Xerr1, yerr=Yerr1, fmt='ro', markersize=3, c='red')
plt.errorbar(X2, Y2, xerr=Xerr2, yerr=Yerr2, fmt='ro', markersize=3, c='green')
plt.errorbar(X3, Y3, xerr=Xerr3, yerr=Yerr3, fmt='ro', markersize=3, c='blue')

plt.xlabel('$I_A$, мА', fontdict=None, labelpad=None, loc=None, fontsize=18)
plt.ylabel('$V_B$, мВ', fontdict=None, labelpad=None, loc=None, fontsize=18)

plt.xlim([0, 250])
plt.ylim([0, 800])

plt.grid(True, color="grey", linewidth="1")

plt.xticks(np.arange(min(x), max(x) + 1, 25.0))
plt.yticks(np.arange(min(y), max(y) + 1, 50.0))

print(m1)
print(m2)
print(m3)
print()
sum = 0
for i in range(10):
    sum += (m1 - Y1[i] / X1[i]) ** 2
print((sum / 10 * 9) ** 0.5)

sum = 0
for i in range(10):
    sum += (m2 - Y2[i] / X2[i]) ** 2
print((sum / 10 * 9) ** 0.5)

sum = 0
for i in range(10):
    sum += (m3 - Y3[i] / X3[i]) ** 2
print((sum / 10 * 9) ** 0.5)
plt.show()
