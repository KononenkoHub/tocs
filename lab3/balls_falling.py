import turtle
import matplotlib.pyplot as plt
import time


GRAVITATION = 9.81
HIGHT = 2.9
WEIGHT = .115


def experiment1(dt=.01):
    speed = 0
    time = 0
    y = HIGHT
    timeList = []
    yList = []
    speedList = []

    while y>=0:
        y -= speed*dt
        speed += GRAVITATION*dt
        time += dt
        yList.append(y)
        speedList.append(speed)
        timeList.append(time)

    fig, (plt1, plt2) = plt.subplots(1, 2)
    fig.suptitle('Linear without resistance')
    plt1.plot(timeList, yList, color='red')
    plt1.set(xlabel='time s', ylabel= 'hight m')
    plt1.grid()

    plt2.plot(timeList, speedList)
    plt2.set(xlabel='time s', ylabel= 'speed m/s')
    plt2.grid()
    plt.show()


def experiment2liner(dt, rate):
    timeList = []
    yList = []
    speedList=[]
    speed = 0
    HIGHT = 2.9
    time = 0
    y = HIGHT

    while y >= 0:
        temp = (WEIGHT * GRAVITATION) / rate
        a = GRAVITATION * (1 - speed / temp)

        y -= speed * dt
        speed += a * dt
        time += dt
        timeList.append(time)
        yList.append(y)
        speedList.append(speed)

    fig, (plt1, plt2) = plt.subplots(1, 2)
    fig.suptitle('Linear with respect to resistance')
    plt1.plot(timeList, yList, color='green')
    plt1.set(xlabel='time s', ylabel='hight m')
    plt1.grid()

    plt2.plot(timeList, speedList, color='black')
    plt2.set(xlabel='time s', ylabel='speed m/s')
    plt2.grid()
    plt.show()


def experiment2square(dt,rate):
    timeList = []
    yList = []
    speedList = []
    speed = 0
    time = 0
    y = HIGHT

    while y >= 0:
        temp = pow((WEIGHT * GRAVITATION) / rate, .5)
        a = GRAVITATION * (1 - pow((speed / temp), 2))

        y -= speed * dt
        speed += a * dt
        time += dt
        timeList.append(time)
        yList.append(y)
        speedList.append(speed)

    fig, (plt1, plt2) = plt.subplots(1, 2)
    fig.suptitle('Quadratic with resistance')
    plt1.plot(timeList, yList, color='blue')
    plt1.set(xlabel='time s', ylabel='hight m')
    plt1.grid()

    plt2.plot(timeList, speedList)
    plt2.set(xlabel='time s', ylabel='speed m/s')
    plt2.grid()
    plt.show()


def visualization(dt, rate):
    speed1 = 0
    speed2 = 0

    time1 = 0
    time2 = 0

    y1 = HIGHT
    y2 = HIGHT

    wf = turtle.Screen()
    wf.bgcolor("black")
    wf.screensize(500, 600)
    turtle.title('Simulations of falling balls in area')

    ball1 = turtle.Turtle()
    ball2 = turtle.Turtle()

    ball1.shape('circle')
    ball2.shape('circle')

    ball1.color('red')
    ball2.color('green')

    ball1.penup()
    ball2.penup()

    ball1.speed(0)
    ball2.speed(0)

    ball1.goto(0, 200)

    ball2.goto(50, 200)

    while y1 >= 0:

        y1 -= speed1 * dt
        speed1 += GRAVITATION * dt
        time1 += dt

        temp2 = pow((WEIGHT * GRAVITATION) / rate, .5)
        a2 = GRAVITATION * (1 - pow((speed2 / temp2), 2))

        y2 -= speed2 * dt
        speed2 += a2 * dt
        time2 += dt

        ball1.dy = -speed1

        ball2.dy = -speed2
        if ball1.ycor() > -248:
            ball1.sety(ball1.ycor() + ball1.dy)

        if ball2.ycor() > -248:
            ball2.sety(ball2.ycor() + ball2.dy)


if __name__ == '__main__':
    experiment1()
    experiment2liner(.001, .5)
    experiment2square(.001, .5)
    visualization(.001, 1)
