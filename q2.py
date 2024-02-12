import numpy as np
import matplotlib.pyplot as plt


def graphSnowfall(t):
    f = open(t, 'r') #opens the file
    data = [] #create the list of data
    for line in f:  #loops and read the data from the file on each line
        if(line != '\n'):
            data.append(int(line))

    graphData = [0,0,0,0,0]
    yaxis=[1,2,3,4,5]
    for num in data:
        if(num <= 10):
            graphData[0]+=1
        elif(num > 10 and num <= 20):
            graphData[1]+=1
        elif(num >20 and num <=30):
            graphData[2]+=1
        elif(num >30 and num <=40):
            graphData[3]+=1
        elif(num >40 and num <=50):
            graphData[4]+=1

    fig, ax = plt.subplots()
    ax.plot(graphData, yaxis)
    ax.set(xlabel='Level', ylabel='Number', title='Snow Levels')
    ax.grid()
    fig.savefig("test.png")
    plt.show()

    print(graphData)
    


graphSnowfall("file.txt")
