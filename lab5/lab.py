import matplotlib.pyplot as plt


E = 50
R = 2000
c = 150
dt = .00003



Uc = 0
Ucn = 0
vz = 0
t = 0

C = c * 1e-9

f1_plot1_x = []
f1_plot1_y = []
f1_plot2_x = []
f1_plot2_y = []

f2_plot1_x = []
f2_plot1_y = []

f3_plot1_x = []
f3_plot1_y = []
f3_plot2_x = []
f3_plot2_y = []

f4_plot1_x = []
f4_plot1_y = []

while t < .001:
    f1_plot1_x.append(t)
    f1_plot1_y.append((E-Uc)/R)
    f1_plot2_x.append(t)
    f1_plot2_y.append((E - Ucn) / R)

    f2_plot1_x.append(t)
    f2_plot1_y.append(((E-Uc)/R)-((E-Ucn)/R))

    f3_plot1_x.append(t)
    f3_plot1_y.append(Uc)
    f3_plot2_x.append(t)
    f3_plot2_y.append(Ucn)

    f4_plot1_x.append(t)
    f4_plot1_y.append(Uc - Ucn)

    Uc = Uc + dt * (E - Uc) / (R * C)
    Ucn = (Ucn + E * dt / (R * C)) / (1 + dt / (R * C))
    t+=dt




egrid = (10, 10)
ax = plt.subplot2grid(egrid, (0, 0), colspan=4, rowspan=4)
ax2 = plt.subplot2grid(egrid, (6, 0), colspan=4, rowspan=4)
ax3 = plt.subplot2grid(egrid, (0, 5), colspan=7, rowspan=4)
ax4 = plt.subplot2grid(egrid, (6, 5), colspan=7, rowspan=4)

ax.set_title('Струм в колі')
ax.grid()
ax.plot(f1_plot1_x,f1_plot1_y, color='red')
ax.plot(f1_plot2_x,f1_plot2_y)

ax2.grid()
ax2.plot(f2_plot1_x, f2_plot1_y)
ax2.plot()

ax3.set_title('Напруга в колі')
ax3.grid()
ax3.plot(f3_plot1_x, f3_plot1_y)
ax3.plot(f3_plot2_x, f3_plot2_y)

ax4.set_title('Похибка')
ax4.grid()
ax4.plot(f4_plot1_x, f4_plot1_y)


plt.show()