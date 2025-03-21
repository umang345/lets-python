def printNumFive(num):
    if num == 0:
        return
    print(num)
    printNumFive(num-1)

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

def sumOfNNaturalNumbers(num):
    #  sum(n) = n+sum(n-1)
    if num == 0:
        return num 
    return num + sumOfNNaturalNumbers(num-1)

print(sumOfNNaturalNumbers(5))