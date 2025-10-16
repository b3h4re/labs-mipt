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
N_1 = np.array(list(map(float, '''24,00
21,00
18,00
15,00
12,00
9,00
7,00
5,00
3,00
1,00
-0,34
-1,66
-3,00
-5,00
-7,00
-9,10
-11,00
-14,00
-17,00
-20,00
-23,00
-26,00

	



'''.replace(',', '.').split())))

#y
T_1 = np.array(list(map(float, '''139,60
144,50
143,26
138,20
125,92
106,69
88,73
68,05
44,25
18,02
0,00
-23,38
-41,41
-67,21
-88,51
-108,41
-123,24
-140,68
-152,85
-156,90
-156,18
-151,70




	



'''.replace(',', '.').split())))

N_2=np.array(list(map(float,'''



'''.replace(',', '.').split())))

T_2=np.array(list(map(float,'''



'''.replace(',', '.').split())))





plt.figure(figsize=(8, 5), dpi=100)
plt.ylabel("I, мА")
plt.xlabel("U,В")
plt.grid(True, linestyle="--")
plt.axis([-28, +28, -250, 250])

dots1 = np.array([0, 23.5])
dots2 = np.array([-23.5, 0])
dots3 = np.array([-5.2, 5.2])
dots4 = np.array([0, 5])

k1=4.07
b1=75

k2=4.07
b2=-85

k3=15.56
b3=3.39995


plt.gca().spines[:].set_position('center')

plt.plot(dots1, k1* dots1 + b1, "-b", linewidth=0.7 )
plt.plot(dots2, k2 * dots2 + b2, "-b", linewidth=0.7 )
plt.plot(dots3, k3 * dots3 + b3, "-g", linewidth=0.7 )
plt.plot(dots4, 0*dots4+b1, "-b", linewidth=0.7 )

plt.scatter(N_1, T_1, color="red", s=22, label="При токе разряда $I_p = 1,51$ мА")
#plt.plot(N_2, T_2, "+b",  ms=10,label="Значения при уменьшении тока" )

plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
