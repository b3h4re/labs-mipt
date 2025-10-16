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

N_2=np.array(list(map(float,'''24,00
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

T_2=np.array(list(map(float,'''
139,60
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


N_3=np.array(list(map(float,'''24,37
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

T_3=np.array(list(map(float,'''176,34
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


plt.figure(figsize=(8, 5), dpi=100)
plt.ylabel("I, мА")
plt.xlabel("U,В")
plt.grid(True, linestyle="--")
plt.axis([-28, +28, -300, 300])




plt.gca().spines[:].set_position('center')



plt.plot(N_1, T_1, "+r", ms=10 ,label="При токе разряда = 0.84 мА" )
plt.plot(N_2, T_2, "+b",  ms=10,label="При токе разряда = 1.51 мА" )
plt.plot(N_3, T_3, "+g", ms=10 ,label="При токе разряда = 2 мА" )

plt.legend()
plt.show()
