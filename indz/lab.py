import matplotlib.pyplot as plt


NUM_OF_POINTS = 14000
BREAKPOINT = NUM_OF_POINTS/2

def generateRandomNumbers():
    max_num = 6700417
    randomList = []
    randomList.append(pow(2, -32))
    for i in range(1,NUM_OF_POINTS):
        randomList.append((max_num * randomList[i-1])%1)

    return randomList


def plot_maker():
    plt.figure()

    x = generateRandomNumbers()
    print(len(x))
    x_cord = x[:int(BREAKPOINT)]
    print(len(x_cord))
    y_cord = x[int(BREAKPOINT):]
    print(len(y_cord))

    for i in range(len(x_cord)):
        plt.scatter(x_cord[i], y_cord[i], color='red')
    plt.show()

plot_maker()