# Saple Program : Finding Prime Numbers

def isPrimeNumber(numP1):
    for i in range(2, numP1) :
        if numP1 % i == 0:
            break
    else :
        return True
    return False

def findPrimes(numP1, numP2):
    numCount = 1
    for i in range(numP1, numP2):
        if i == 1:
            continue
        if isPrimeNumber(i) == True:
            print(numCount, " th prime : ", i)
            numCount = numCount + 1

findPrimes(1, 10)