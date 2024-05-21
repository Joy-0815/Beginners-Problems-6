evenList = [2, 59, 132, 62, 50, 39, 238, 926, 529, 42, 19, 10, 52, 5, 9]

def getEven(list):
    for num in evenList:
        if num % 2 == 0:
            print(num, end=" ")
    return getEven

getEven(evenList)