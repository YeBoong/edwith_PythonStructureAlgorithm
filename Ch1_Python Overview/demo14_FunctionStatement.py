# 사용자 정의 함수
# def 함수 이름(매개변수1, 매개변수2, ... ) :

numA = 1
numB = 2

def add(numP1, numP2):
    return numP1 + numP2
def multiply(numP1, numP2):
    return numP1 * 2,  numP2 * 3
def increase(numP1, step = 1):
    return numP1 + step

numC = add(numA, numB)
numD, numE = multiply(numA, numB)
numF = increase(numA, 5)
numG = increase(numA)

lambdaAdd = lambda numP1, numP2 : numP1 + numP2

numH = lambdaAdd(numA, numB)
print(numC, numD, numE, numF, numG, numH)