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
    results = ['0-10', '11-20', '21-30', '31-40','41-51']
    bar_labels = ['red', 'blue', '_red', 'orange','_blue']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:blue','tab:red']

    ax.bar(results, graphData, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Number')
    ax.set_title('Snow Levels')
    ax.legend(title='Snow Levels')

    plt.show()


graphSnowfall("file.txt")
