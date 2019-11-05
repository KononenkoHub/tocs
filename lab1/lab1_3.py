import matplotlib.pyplot as plt
import random

def function(x):
    if 0<=x <2:
        return (0.25*x)/2
    elif 2 <=x <4:
        return (0.25*(x-2))/2
    elif 4<=x<6:
        return (0.25*(x-4)/2)
    elif 6<= x <8:
        return (0.25*(x-6)/2)
    else:
        return 0


numOfpoints = 0
M = .8
x = []
a,b = 0,8
while a<=b:
    x.append(a)
    a+=.01

y = [function(i) for i in x]
points = []



plt.figure()
plt.plot(x,y)

while numOfpoints<= 5000:
    r1 = random.random()
    r2 = random.random()
    x0 = r1*8
    tempY = r2*M

    if (tempY < function(x0)):
        plt.scatter(x0,tempY)
        numOfpoints+=1



plt.show()