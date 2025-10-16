import numpy as np
import matplotlib.pyplot as plt


def approx(f, r, Z, X):
    php = np.array([0, np.pi, np.pi/2, 3*np.pi/2, f, np.pi-f, np.pi+f, 2*np.pi-f])
    y = np.array([0, 0, Z, -Z, np.sin(f)*r, np.sin(f)*r, -np.sin(f)*r, -np.sin(f)*r])
    x = np.array([X, -X, 0, 0, np.cos(f)*r, -np.cos(f)*r, -np.cos(f)*r, np.cos(f)*r])
    yb = np.sin(php)
    xa = np.cos(php)
    b = np.mean(y*yb) / np.mean(yb**2)
    a = np.mean(x*xa) / np.mean(xa**2)

    sigma_b = (1/(8 ** 0.5)) * (np.mean(y**2)/np.mean(yb**2) - b**2)**0.5
    sigma_a = (1/(8 ** 0.5)) * (np.mean(x**2)/np.mean(xa**2) - a**2)**0.5

    return a, b, x, y, sigma_a, sigma_b


def ellipse(x, y, a, b,st,OY,OX, limx=[-30,30],limy=[-30,30]):
    plt.figure(figsize=(10, 10))

    y_approx = b*np.sin(phi)
    x_approx = a*np.cos(phi)

    plt.plot(x_approx,y_approx,label=st)
    plt.plot(x, y, 'ro',ms =10,label="Экспериментальные точки")

    #plt.plot([0,0],limy, 'k')
    #plt.plot(limx,[0,0], 'k')

    plt.xlim(limx)
    plt.ylim(limy)

    #— Decorate the spins
    arrow_length = 20 # In points

    # X-axis arrow
    plt.annotate(OX, xy=(0.993, 0), xycoords=('axes fraction', 'data'),
    xytext=(arrow_length, 0), textcoords='offset points',
    ha='left', va='center',
    arrowprops=dict(arrowstyle='<|-', fc='black'))

    # Y-axis arrow
    plt.annotate(OY, xy=(0, 0.993), xycoords=('data', 'axes fraction'),
    xytext=(0, arrow_length), textcoords='offset points',
    ha='center', va='bottom',
    arrowprops=dict(arrowstyle='<|-', fc='black'))

    plt.minorticks_on()
    plt.grid(which='major', lw=2)
    plt.grid(which='minor', lw=1)
    plt.legend(loc = 'upper left')
    # plt.show()


phi = np.linspace(0, 2*np.pi, 200)

c = 15
b = 10.01
a = 5.04
fp = np.arctan(c / b)
fe = np.arctan(c / a)
fm = np.arctan(a / (a**2 + b**2)**0.5)


# w, e, xo, yo = approx(np.pi/4, 35.05, 34.92, 34.92)
w, e, xo, yo, sigma_w, sigma_e = approx(np.pi/4, 34.11, 34.21, 34.21)

# ap, bp, xp, yp = approx(fp,25.87,29.93,20.94) #ОСЬ СС' Вдоль OY, ОСЬ AA' Вдоль OX
# ae,be,xe,ye=approx(fe,27.85,29.93,18.55) #ОСЬ ВВ' Вдоль OX, ОСЬ CC' Вдоль OY
# am,bm,xm,ym=approx(fm,20.37,18.55,20.94) #ОСЬ AA' Вдоль OX, ОСЬ BB' Вдоль OY

ap, bp, xp, yp, sigma_ap, sigma_bp = approx(fp, 25.33, 29.11, 20.92)
ae, be, xe, ye, sigma_ae, sigma_be = approx(fe, 27.06, 29.11, 18.54)
am, bm, xm, ym, sigma_am, sigma_bm = approx(fm, 21.13, 18.54, 20.92)


# ellipse(xp, yp, ap, bp,"""Аппроксимация эллипсом в сечении (YOZ) ""","""CC'(OZ)""", """AA'(OY)""")
# ellipse(xe,ye,ae,be,"""Аппроксимация эллипсом в сечении (XOZ) """, """CC'(OZ)""", """BB'(OX)""")
# ellipse(ym,xm,bm,am,"""Аппроксимация эллипсом в сечении (XOY) ""","""BB'(OY)""", """AA'(OX)""")
#
# ellipse(xo,yo,w,e,"""Аппроксимация окружностью в сечении (XOY) ""","""OY'""", """OX'""",[-40,40],[-40,40])
#
# ellipse([-34.35,34.35,0,0],[0,0,24.87,-24.87],34.35,24.87,"""Аппроксимация эллипсом в сечении блина ""","""OZ""", """OX""",[-40,40],[-40,40])
# ellipse([35.40,-35.40,0,0],[0,0,29.45,-29.45],35.40,29.45,"""Аппроксимация эллипсом в сечении цилиндра ""","""OZ""", """OX""",[-40,40],[-40,40])

print(ap,bp,ae,be,am,bm)
print('p')
print(ap, sigma_ap)
print(bp, sigma_bp)

print('e')
print(ae, sigma_ae)
print(be, sigma_be)

print('m')
print(am, sigma_am)
print(bm, sigma_bm)

print('cube')
print(w, e, sigma_w, sigma_e)

print()

X, Z = 34.35, 24.87
php = np.array([0, np.pi, np.pi/2, 3*np.pi/2])
y = np.array([0, 0, Z, -Z])
x = np.array([X, -X, 0, 0])
yb = np.sin(php)
xa = np.cos(php)
b = np.mean(y*yb) / np.mean(yb**2)
a = np.mean(x*xa) / np.mean(xa**2)
sigma_b = (1/(8 ** 0.5)) * (np.mean(y**2)/np.mean(yb**2) - b**2)**0.5
sigma_a = (1/(8 ** 0.5)) * (np.mean(x**2)/np.mean(xa**2) - a**2)**0.5
print(a, b, sigma_a, sigma_b)

T = np.array([7.01, 6.55, 5.65, 6.52, 5.81, 5.97, 6.05])
x = np.array([5.644, 4.346, 2.180, 4.609, 2.531, 2.847, 3.050])

u = T**2

v = x
print("u = ", u, "\nv = ", v)

mu = np.mean(u) # средее
mv = np.mean(v)
mv2 = np.mean(v**2) # средний квадрат
mu2 = np.mean(u**2)
muv = np.mean (u * v) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
print("k = ", k, ", b = ", b)

np.polyfit(v, u, 1)

sigma_y = 0.003
sigma_T = 2*0.04

sigma_k = (1/7**0.5) * ((np.mean(u**2) - np.mean(u)**2)/(np.mean(v**2) - np.mean(v)**2) - k**2)**0.5
sigma_b = sigma_k * (np.mean(v**2) - np.mean(v)**2)**0.5

print(sigma_k, sigma_b)

plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$u=T^2$, $с^2$") # подписи к осям
plt.xlabel("$v=I$, $г \cdot м^2$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0,6,0,60]) # масштабы осей
x = np.array([0., 10000]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v + %.2f$" % (k, b)) # аппроксимация
plt.errorbar(v, u, xerr=sigma_y, yerr=sigma_T, fmt="ok", label="Экспериментальные точки", ms=3) # точки с погрешностями
plt.legend() # легенда
plt.show()