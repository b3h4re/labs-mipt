import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 




# for important settings
max_x = -1e9
max_y = -1e9
min_x = 1e9
min_y = 1e9

# x = N
# y = T

#x
N_1 = np.array(list(map(float, '''
25
22
19
16
13
10
8
6
4
2
0,66
-0,8
-2
-4
-6
-8
-10
-13
-16
-19
-22
-25





'''.replace(',', '.').split())))

#y
T_1 = np.array(list(map(float, '''
97,03
99,14
98,88
95,90
87,80
75,35
63,65
49,05
32,53
14,40
1,30
-0,68
-12,63
-29,62
-45,53
-58,14
-68,87
-80,17
-87,42
-90,22
-91,12
-89,10




	



'''.replace(',', '.').split())))

N_2=np.array(list(map(float,'''



'''.replace(',', '.').split())))

T_2=np.array(list(map(float,'''



'''.replace(',', '.').split())))





plt.figure(figsize=(8, 5), dpi=100)
plt.ylabel("I, мА")
plt.xlabel("U,В")
plt.grid(True, linestyle="--")
plt.axis([-28, +28, -180, 180])

dots1 = np.array([0, 23.5])
dots2 = np.array([-23.5, 0])
dots3 = np.array([-6.2, 6.2])
dots4 = np.array([0, 6])

k1=2.8
b1=51

k2=2.8
b2=-48

k3=8
b3=1


plt.gca().spines[:].set_position('center')


plt.plot(dots1, k1* dots1 + b1, "-b", linewidth=0.7 )
plt.plot(dots2, k2 * dots2 + b2, "-b", linewidth=0.7 )
plt.plot(dots3, k3 * dots3 + b3, "-g", linewidth=0.7 )
plt.plot(dots4, 0*dots4+b1, "-b", linewidth=0.7 )

plt.scatter(N_1, T_1, color="red", s=22, label="При токе разряда $I_p = 0,84$ мА")
#plt.plot(N_2, T_2, "+b",  ms=10,label="Значения при уменьшении тока" )

plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)


plt.legend()
plt.show()
