
def stats_decorator(func): #decorator that read each line for numbers
    def wrapper(line):
        numbers = [float(num) for num in line.split()] #split the numbers from the line into a list
        count = len(numbers) #count the total numbers
        average = sum(numbers) / count # calculate the average
        maximum = max(numbers) #calculate the max

        #printing the data
        print(f"Numbers read: {numbers}") 
        print(f"Count of numbers read: {count}")
        print(f"Average of the numbers: {average:.2f}")
        print(f"Maximum of the numbers: {maximum:.2f}")

        return func(line)

    return wrapper

@stats_decorator
def printStats(line):
    pass

with open("file3.txt", 'r') as file:
    for line in file:
        printStats(line)