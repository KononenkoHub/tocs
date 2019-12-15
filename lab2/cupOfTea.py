import matplotlib.pyplot as plt
from tkinter import *
import numpy



#parametrs

firstTemperature = 84
enviromentTemperature = 21
RATE = .09
time = 15
step = 15
timeOfExperiment = 30
listOfTemperature = [85.2, 78.6, 75.4, 73, 71.5, 69.8, 67.9, 66.8, 64.9, 63.6, 61.9, 60.2, 59.4, 58.8, 57.6, 56.4]



#FIXME
def cordinateFromWindox():




    parametrsForm = Tk()
    parametrsForm.geometry("500x250")
    parametrsForm.title('Parametre form')
    parametrsForm.resizable(width=False, height=False)

    #parametrs
    firsTemperature = DoubleVar()
    environmentTemperature = DoubleVar()
    rate = DoubleVar()
    time = DoubleVar()
    step = DoubleVar()
    timeOfExperiment = DoubleVar()


    #Label and Input for first temperature
    firsTemperatureLabel = Label(text='Початкова температура = ')
    firsTemperatureLabel.place(x=40, y=30)

    firsTemperatureEntry = Entry(parametrsForm, textvariable=firsTemperature)
    firsTemperatureEntry.place(relx= .4 ,rely= .13 )


    environmentTemperatureLabel = Label(text='Темпераура середовища = ')
    environmentTemperatureLabel.place(x=40,y=60)

    environmentTemperatureEntry = Entry(parametrsForm, textvariable=environmentTemperature)
    environmentTemperatureEntry.place(relx = .4, rely= .25)


    rateLabel = Label(text='Коефіцієнт = ')
    rateLabel.place(x = 40,y =90)

    rateEntry = Entry(parametrsForm, textvariable=rate)
    rateEntry.place(relx = .25, rely=.37)


    timeLabel = Label(text='Час в секундах = ')
    timeLabel.place(x =40, y =120)

    timeEntry = Entry(parametrsForm,textvariable=time)
    timeEntry.place(relx=.3, rely=.50)


    stepLabel = Label(text='Крок в секундах = ')
    stepLabel.place(x = 40, y = 150)

    stepEntry = Entry(parametrsForm,textvariable = step)
    stepEntry.place(relx =.35, rely = .62)


    timeOfExperimentLabel = Label(text='Час експерименту = ')
    timeOfExperimentLabel.place(x=  40, y = 180)

    timeOfExperimentEntry = Entry(parametrsForm, textvariable = timeOfExperiment)
    timeOfExperimentEntry.place(relx=.36, rely =.74)


    def getPar():
        return firstTemperature, enviromentTemperature, rate, time, \
               step, timeOfExperiment


    submitButton = Button(text = 'Start',height = 1, width = 20, command=getPar)
    submitButton.place(x=180, y=220)



    parametrsForm.mainloop()

    return getPar()


def experiment1(firstTemperature, enviromentTemperature, i):
    return enviromentTemperature + (firstTemperature-enviromentTemperature) * numpy.exp(-(RATE*i))

def experiment2(firstTemperature,enviromentTemperature,rate):
    return firstTemperature-RATE * rate *(firstTemperature-enviromentTemperature)


def main_function(firstTemperature,enviromentTemperature,rate):
    Temperature0 = firstTemperature
    yList1 = []
    yList2 = []
    xList = []
    epsList = []
    i = 1

    while Temperature0 > enviromentTemperature+1:
        firstFunctionRes = experiment1(firstTemperature,enviromentTemperature, i * rate)

        xList.append(i*rate)

        y = experiment2(Temperature0,enviromentTemperature, rate)

        Temperature0 = y

        yList1.append(firstFunctionRes)
        yList2.append(Temperature0)

        eps = pow(firstFunctionRes-Temperature0,2)
        epsList.append(numpy.sqrt(eps))
        i += 1

    return yList1, yList2, xList, epsList







def experiment4(enviromentTemperature, listOfTemperature):
    firstgraphX = []
    firstgraphY = []
    secondgraphX = []
    secondgraphY = []

    sum = 0
    listl = []
    r1 = .04
    h = 1
    firstTemperature = listOfTemperature[0]

    for i in range(len(listOfTemperature)):
        currentTemperature = firstTemperature - r1 * h * (firstTemperature-enviromentTemperature)
        firstTemperature = currentTemperature
        listl.append(currentTemperature)
        sum += numpy.power(listl[i]-listOfTemperature[i],2)
        firstgraphX.append(h*i)
        firstgraphY.append(currentTemperature)

        secondgraphX.append(h*i)
        secondgraphY.append(listOfTemperature[i])
    sigma = numpy.sqrt(sum)/len(listOfTemperature)

    print('Sum = ', sum)
    print('Sigma = ', sigma)

    return firstgraphX,firstgraphY,secondgraphX,secondgraphY





if __name__ == '__main__':

    ylist1,ylist2,xlist, epslist1 = main_function(firstTemperature,enviromentTemperature,0.1)
    _, _, xlist2, epslist2 = main_function(firstTemperature,enviromentTemperature,0.17)
    _, _, xlist3, epslist3 = main_function(firstTemperature,enviromentTemperature,0.27)

    firstgraphX, firstgraphY, secondgraphX, secondgraphY = experiment4(enviromentTemperature,listOfTemperature)


    egrid = (10, 10)
    ax = plt.subplot2grid(egrid, (0, 0), colspan=4, rowspan=4)
    ax2 = plt.subplot2grid(egrid, (6, 0), colspan=4, rowspan=4)
    ax3 = plt.subplot2grid(egrid, (0, 5), colspan=7, rowspan=10)

    ax.grid()
    ax.set_title('Temperature dependence on time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.plot(xlist, ylist1, label="Analytical graph")
    ax.plot(xlist, ylist2, label="Euler's explicit method")
    ax.legend()


    ax2.grid()
    ax2.set_title('Fault')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Temperature')
    ax2.plot(xlist,epslist1, label='0.1')
    ax2.plot(xlist2,epslist2, label='0.17')
    ax2.plot(xlist3,epslist3, label='0.27')
    ax2.legend()



    ax3.grid()
    ax3.set_title('Divergence')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Temperature')
    ax3.plot(firstgraphX,firstgraphY, color='green', label='Analytical data')
    ax3.plot(secondgraphX,secondgraphY, color='red', label='Real data')

    ax3.legend()





    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()
    




