import matplotlib.pyplot as plt
import numpy as np
import random



def generateRandomNumbers():
    maxNum =  140433
    randomList = []
    randomList.append(pow(2,-32))
    for i in range(1000):
        randomList.append((randomList[i-1]*maxNum)-int(randomList[i-1]*maxNum))

    return randomList


def printRandomList(randomList):
    for i in randomList:
        print(i,'\n')


def mathExpectatio(randomList):
    sumOfNumber = sum(randomList)
    expectedValue = sumOfNumber/(len(randomList))
    return expectedValue


def dispersion(randomList):
    summ = 0
    avg = mathExpectatio(randomList)
    for i in range(len(randomList)-1):
        summ+=pow(randomList[i]-avg,2)
    
    disp = (summ / 1000.0)
    return disp


def barChart(randomList):
    objects = ('0 - 0.3','0.3 - 0.6','0.6 - 0.9')
    num1,num2,num3 = 0,0,0

    for i in randomList:
        if .3 <= i < .6:
            num2+=1
        elif i >= .6:
            num3+=1
        else:
            num1+=1

    performance = [num1,num2,num3]
    y_pos = np.arange(len(objects))
    plt.bar(y_pos,performance)
    plt.xticks(y_pos, objects)
    plt.show()




if __name__ == '__main__':

    generateRandomNumbers()
    print('Math expectation = ',mathExpectatio(generateRandomNumbers()))

    print('Dispersion = ', dispersion(generateRandomNumbers()))

    barChart(generateRandomNumbers())
    print()


















    secondList = {}