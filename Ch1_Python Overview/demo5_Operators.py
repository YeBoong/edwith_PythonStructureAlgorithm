def main():
    numTest1 = 10
    numTest2 = 3.0
    numPlus = numTest1 + numTest2
    numMinus = numTest1 - numTest2
    numMultiply = numTest1 / numTest2
    numDivide = numTest1 / numTest2
    numModula = numTest1 % numTest2
    print("%d, %d, %d, %d, %d " % (numPlus, numMinus, numMultiply, numDivide, numModula))

    numDivideInt = numTest1 / int(numTest2)
    print(numDivide, numDivideInt)

    numTest2, numTest1 = numTest1, numTest2
    print(numTest1, numTest2)

    print(numTest1 == numTest2)
    print(numTest1 != numTest2)
    print(type(numTest1))

    numTest1 = str(numTest1)
    print(type(numTest1), numTest1)

    strFomula = "2011 / 7"
    print(eval(strFomula))

main()