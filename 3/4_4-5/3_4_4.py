import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
from math import isnan, nan


data = pd.read_excel("8290.xlsx", sheet_name="data")
H = []
B = []

for row in data.iterrows():
    t = row[1]
    H.append(t.iloc[0])
    B.append(t.iloc[1])

print(H)
print(B)

x = np.array(H)
y = np.array(B)

H_start = np.array([0.0, 85.5, 156.6, 218.2, 248.0, 312.1, 371.7, 529.1, 876.5, 1395.7, 2866.0, 8132.8])
B_start = np.array([0, 0.028, 0.083, 0.143, 0.158, 0.206,0.242, 0.292, 0.345, 0.412, 0.526, 0.750])



plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', s=12, label='Эксперементальные точки')
plt.scatter(H_start, B_start, color='green', s=12, label='Эксперементальные точки')
# plt.plot(x_model, y_model, color='red', label='Вольт амперная характеристика')

# Title and labels
plt.ylabel('$B, Тл$')
plt.xlabel('$H, А/м$')

# Grid and legend
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
