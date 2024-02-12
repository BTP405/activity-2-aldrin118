def getPrimeNumbers(n):
    primeList = []

    #loops cannot be avoided since each between 2 and n needs to be check if its a prime number or not.
    for num in range(2,n): #loops through 2 to n
        prime = True    #set the current num to isPrime
        #no code is repeated
        for i in range(2,num): #loops num of its divisible by any number between 2 and num
            if (num%i==0):  #check if divisible by any number between 2 and num
                prime = False #if divisible not a prime
        if prime:
            primeList.append(num) #if not divisible append to the prime list.

    return primeList

print(getPrimeNumbers(101))