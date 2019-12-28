import matplotlib.pyplot as plt
import numpy as np

num_of_iterates = 150
k = 6
m = 175
x0 = .6
dt = .2
v = .05
w0 = 0

def foo(x0,v):
    m = .125
    x0 = .02
    dt = 0.01

    res1 = []
    res2 = []
    N = 500


    w0 = np.sqrt(k / m)

    y = 0.5

    t = 0
    for i in range(1,N):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0 - 2 * y * v * dt

        t = t + dt
        res1.append(x0)
        res2.append(v)

    plt.figure()
    plt.grid()
    plt.plot(res1,res2)
    plt.show()


def ostsilograf(x0, dt, v):
    """
    Function make two list for ostsilograf plot
    :param x0: start x cordinate
    :param dt: step of time
    :param v: speed
    :return: two list with x cordinates and speed values
    """
    N = 400
    cordinate_x = []
    v_value = []

    w0 = np.sqrt(k/m)

    time = 0

    for i in range(1,N):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0
        energy = m * v * v / 2 + x0 * x0 * k / 2
        time = time + dt
        cordinate_x.append(x0)
        v_value.append(v)

    return cordinate_x, v_value


def make_ostsilograf():
    """
    Function draw plot with ostsilograf
    :return: none
    """
    xlist, ylist = ostsilograf( x0, dt, v)
    plt.figure()
    plt.plot(xlist, ylist, color='red')
    plt.grid()
    plt.axhline()
    plt.axvline()
    plt.title("x(v)")
    plt.show()

def summary(num_of_iterates, x0, dt, v):
    """
    Method
    :param num_of_iterates: iteration number
    :param x0: firt position on X cordinate
    :param dt: step in time
    :param v: speed
    :return: four list with cordinates(2 xlists, 2 ylists)
    """

    first_plot_x_cordinates = []
    first_plot_y_cordinates = []
    second_plot_x_cordinates = []
    second_plot_y_cordinates = []

    w0 = np.sqrt(k / m)

    time = 0
    for i in range(1,num_of_iterates):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0
        energy = m * v * v / 2 + x0 * x0 * k / 2
        time = time + dt
        first_plot_x_cordinates.append(time)
        first_plot_y_cordinates.append(energy)

    time = 0
    for i in range(1,num_of_iterates):
        v = v + (-w0 * w0) * dt * x0
        x0 = x0 + dt * v
        E1 = m * v * v / 2 + x0 * x0 * k / 2
        time = time + dt
        second_plot_x_cordinates.append(time)
        second_plot_y_cordinates.append(E1)

    return first_plot_x_cordinates, first_plot_y_cordinates, second_plot_x_cordinates, second_plot_y_cordinates

def find_x_0(num_of_iterates, x0, dt, v):
    first_x_list = []
    first_y_list = []
    second_x_list = []
    second_y_list = []

    w0 = np.sqrt(k / m)
    time = 0
    for i in range(1,num_of_iterates):
        v = v + (-w0 * w0) * dt * x0
        x0 = x0 + dt * v
        time = time + dt
        first_x_list.append(time)
        first_y_list.append(x0)
    time = 0
    for i in range(1,num_of_iterates):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0
        time = time + dt

        second_x_list.append(time)
        second_y_list.append(x0)

    return first_x_list, first_y_list, second_x_list, second_y_list


def potential_energy(num_of_iterates, x0, dt, v):
    w0 = np.sqrt(k / m)
    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []

    time = 0
    for i in range(1,num_of_iterates):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0
        energy = x0 * x0 * k / 2
        time = time + dt

        xlist.append(time)
        ylist.append(energy)


    time = 0
    for i in range(1,num_of_iterates):
        v = v + (-w0 * w0) * dt * x0
        x0 = x0 + dt * v
        E1 = x0 * x0 * k / 2
        time = time + dt

        xlist2.append(time)
        ylist2.append(E1)

    return xlist,ylist , xlist2, ylist2


def kinetic_energy(num_of_iterates, x0, dt, v):
    w0 = np.sqrt(k / m)

    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []

    time = 0
    for i in range(1, num_of_iterates):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0
        E1 = m * v * v / 2
        time = time + dt
        xlist.append(time)
        ylist.append(E1)

    time = 0
    for i in range(1,num_of_iterates):
        v = v + (-w0 * w0) * dt * x0
        x0 = x0 + dt * v
        energy = m * v * v / 2
        time = time + dt

        xlist2.append(time)
        ylist2.append(energy)

    return xlist, ylist, xlist2, ylist2


def decaying(k,v):
    """
    Function wich calculate fading fluctuations.
    Generate three par of list with cordinates for diferent fluctuations
    :param k:
    :param v: speed
    :return: 3 par os lists(listx, listy)
    """
    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []
    xlist3 = []
    ylist3 = []

    res_list1 = []
    res_list2 = []


    num_of_iterates = 300
    m = .175
    dt = .01
    x0 =.07
    w0 = np.sqrt(k / m)



    y = 1
    y1 = 5
    y2 = 10
    time = 0
    for i in range(1,num_of_iterates):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0 - 2 * y * v * dt
        energy = m * v * v / 2
        time = time + dt
        xlist.append(time)
        ylist.append(x0)

    time = 0
    x1= .07
    v1 = v
    for i in range(1,num_of_iterates):
        x1 = x1 + dt * v1
        v1 = v1 + (-w0 * w0) * dt * x1 - 2 * y1 * v1 * dt
        E1 = m * v1 * v1 / 2
        time = time + dt
        xlist2.append(time)
        ylist2.append(x1)

    time = 0
    x2 = .07
    v2 = v
    for i in range(1,num_of_iterates):
        x2 = x2 + dt * v2
        v2 = v2 + (-w0 * w0) * dt * x2 - 2 * y2 * v2 * dt
        E2 = m * v2 * v2 / 2
        time = time + dt
        xlist3.append(time)
        ylist3.append(x2)

        res_list1.append(x2)
        res_list2.append(time)

    return xlist, ylist, xlist2, ylist2, xlist3, ylist3, res_list1, res_list2


def potenzial_and_kinetic_energy(k,v):
    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []
    xlist3 = []
    ylist3 = []


    num_of_iterates = 300
    m = .175
    dt = .01
    x0 =.07
    w0 = np.sqrt(k / m)



    y = 1
    y1 = 5
    y2 = 10
    time = 0
    for i in range(1,num_of_iterates):
        x0 = x0 + dt * v
        v = v + (-w0 * w0) * dt * x0 - 2 * y * v * dt
        energy = x0 * x0 * k / 2
        E1 = m * v * v / 2
        E2 = m * v * v / 2 + x0 * x0 * k / 2
        time = time + dt

        xlist.append(time)
        ylist.append(energy)

        xlist2.append(time)
        ylist2.append(E1)

        xlist3.append(time)
        ylist3.append(E2)

    return xlist, ylist, xlist2, ylist2, xlist3, ylist3


def make_first_plot():
    """
    This function make 4 subplots on matplotlib figure.
    Was used four outher functions in this module: summary(), find_x(), potential_energy() and kinetic_energy().
    :return: none
    """
    egrid = (10, 10)
    ax = plt.subplot2grid(egrid, (0, 0), colspan=4, rowspan=4)
    ax2 = plt.subplot2grid(egrid, (6, 0), colspan=4, rowspan=4)
    ax3 = plt.subplot2grid(egrid, (0, 5), colspan=7, rowspan=4)
    ax4 = plt.subplot2grid(egrid, (6, 5), colspan=7, rowspan=4)


    summary_xlist, summary_ylist, summary_xlist2, summary_ylist2 = summary(num_of_iterates, x0, dt, v)
    find_x_xlist, find_x_ylist, find_x_xlist2, find_x_ylist2 = find_x_0(num_of_iterates, x0, dt, v)

    potential_energy_xlist, potential_energy_ylist, potential_energy_xlist2, potential_energy_ylist2 = potential_energy(num_of_iterates, x0, dt, v)

    kinetic_energy_xlist1, kinetic_energy_ylist1, kinetic_energy_xlist2, kinetic_energy_ylist2 = kinetic_energy(num_of_iterates, x0, dt, v)

    ax.plot(summary_xlist, summary_ylist)
    ax.plot(summary_xlist2, summary_ylist2)
    ax.grid()
    ax.set_title("Сумарна")

    ax2.plot(find_x_xlist, find_x_ylist)
    ax2.plot(find_x_xlist2, find_x_ylist2)
    ax2.grid()
    ax2.set_title("x0")

    ax3.plot(potential_energy_xlist, potential_energy_ylist)
    ax3.plot(potential_energy_xlist2, potential_energy_ylist2)
    ax3.grid()
    ax3.set_title("Потенційна енергія")

    ax4.plot(kinetic_energy_xlist1, kinetic_energy_ylist1)
    ax4.plot(kinetic_energy_xlist2, kinetic_energy_ylist2)
    ax4.grid()
    ax4.set_title("Кінетична енергія")


    plt.show()


def make_second_plot():
    """
    This function make two subplots on one figure.
    Was used functions decaying() and potenzial_and_kinetic_energy() with k and v parametrs
    :return: none
    """
    fxlist, fylist, fxlist2, fylist2, fxlist3, fylist3, fxlist4, fylist4 = decaying(k, v)
    sxlist, sylist, sxlist2, sylist2, sxlist3, sylist3 = potenzial_and_kinetic_energy(k,v)

    fig, (plt1, plt2) = plt.subplots(1, 2)
    plt1.plot(fxlist, fylist)
    plt1.plot(fxlist2, fylist2)
    plt1.plot(fxlist3, fylist3)
    plt1.set(xlabel='Time', ylabel='Energy')
    plt1.set(title='x(t)')
    plt1.grid()

    plt2.plot(sxlist,sylist)
    plt2.plot(sxlist2,sylist2)
    plt2.plot(sxlist3, sylist3)
    plt2.set(xlabel='time', ylabel='Energy')
    plt2.set(title='x(t)')
    plt2.grid()
    plt.show()


foo(x0,v)
make_ostsilograf()
make_first_plot()
make_second_plot()




