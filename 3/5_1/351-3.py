import numpy as np
import matplotlib.pyplot as plt


# x = N
# y = T

# x
N_1 = np.array(list(map(float, '''24,37
21,37
18,37
15,37
12,37
9,37
7,37
5,37
3,37
1,37
0,00
-0,03
-1,37
-3,37
-5,37
-7,37
-9,37
-12,37
-15,37
-18,37
-21,37
-24,37



	



'''.replace(',', '.').split())))

# y
T_1 = np.array(list(map(float, '''176,34
181,52
181,99
175,87
159,81
133,88
112,09
84,68
55,46
22,88
0,00
-25,01
-47,35
-79,20
-108,11
-132,84
-154,55
-176,60
-191,06
-196,91
-196,14
-190,49



	



'''.replace(',', '.').split())))

N_2 = np.array(list(map(float,'''



'''.replace(',', '.').split())))

T_2 = np.array(list(map(float,'''



'''.replace(',', '.').split())))


plt.figure(figsize=(8, 5))
plt.ylabel("I, мА")
plt.xlabel("U,В")
plt.grid(True, linestyle="--")
plt.axis([-28, +28, -250, 250])

dots1 = np.array([0, 23.5])
dots2 = np.array([-23.5, 0])
dots3 = np.array([-5.2, 5.2])
dots4 = np.array([0, 5])

k1 = 3.92
b1 = 110

k2 = 3.92
b2 = -130

k3 = 25.73
b3 = -12.177


plt.gca().spines[:].set_position('center')

plt.plot(dots1, k1 * dots1 + b1, "-b", linewidth=0.7 )
plt.plot(dots2, k2 * dots2 + b2, "-b", linewidth=0.7 )
plt.plot(dots3, k3 * dots3 + b3, "-g", linewidth=0.7 )
plt.plot(dots4, 0*dots4+b1, "-b", linewidth=0.7 )

plt.scatter(N_1, T_1, color="red", s=22, label="При токе разряда $I_p = 2$ мА")
#plt.plot(N_2, T_2, "+b",  ms=10,label="Значения при уменьшении тока" )

plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.legend()
plt.show()


