from lab1_lushkiv import *
import random


class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printParametrs(self):
        print(self.x, ' ', self.y)


def theoryMathExpectation(listOfPair):
    mathEx = 0
    for i in range(len(listOfPair)):
        mathEx += listOfPair[i].x * listOfPair[i].y
    return mathEx


def theoryDispersial(listOfPair):
    mathEx = 0
    for i in range(len(listOfPair)):
        mathEx += pow(listOfPair[i].x,2) * listOfPair[i].y

    disp = mathEx - pow(theoryMathExpectation(listOfPair),2)
    return disp


def indexOf(number):
    for i in range(len(listOfPair)):
        if number == listOfPair[i].x:
            return i



listOfPair = [Pair(1, .05), Pair(4, .25), Pair(12, .25), Pair(16, .15), Pair(25, .13), Pair(33, .01), Pair(37, .07)]

listOfFreq = []

listOfIntervals = []
x0 = 0.0
x1 = 0.0

for i in range(len(listOfPair)):
    x0 = x1
    x1 = x0 + listOfPair[i].y
    listOfIntervals.append(Pair(x0, x1))
    listOfFreq.append(0)

for i in range(1000):
    x = round(random.random(),3)
    for j in range(len(listOfIntervals)):
        if (x < listOfIntervals[j].y and x >= listOfIntervals[j].x):
            print(x, ' - ', listOfPair[j].x)
            listOfFreq[indexOf(listOfPair[j].x)] +=1


print('MathExpectation = ', theoryMathExpectation(listOfPair))
print('Dispersial = ', theoryDispersial(listOfPair))

for i in range(len(listOfPair)):
    print(listOfPair[i].x, '\t-\t', listOfFreq[i])


