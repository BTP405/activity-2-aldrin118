import numpy as np
import matplotlib.pyplot as plt
def graphSnowfall(t):
    f = open(t, 'r') #opens the file
    data = [] #create the list of data
    for line in f:  #loops and read the data from the file on each line
        if(line != '\n'):
            data.append(int(line))

    graphData = [0,0,0,0,0] #initiating the graph data
    yaxis=[1,2,3,4,5] #intiating the y axis
    for num in data: #setting each data from the file for each snow levels
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
    results = ['0-10', '11-20', '21-30', '31-40','41-51'] #setting the bar labels data
    bar_labels = ['red', 'blue', '_red', 'orange','_blue'] # setting the colors legends data
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:blue','tab:red'] # setting the bar colors data
    fig, ax = plt.subplots() #initiating the bag graph

    ax.bar(results, graphData, label=bar_labels, color=bar_colors) #initiating the bag graph

    ax.set_ylabel('Number') #setting the bar graphs y axis title
    ax.set_title('Snow Levels') #setting the bar graphs title
    ax.legend(title='Snow Levels') #setting the bar graphs title
    fig.savefig("test.png") # saving in file

    plt.show()


graphSnowfall("file.txt")
