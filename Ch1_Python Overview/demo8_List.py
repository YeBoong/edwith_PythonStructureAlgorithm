lstTest = [1, 2, 3, 4]
print(lstTest)
print(lstTest[0], lstTest[1], lstTest[2])
print(lstTest[-1], lstTest[-2])
print(lstTest[1:3])
print(lstTest + lstTest)
print(lstTest*3)

lstTest = list(range(1, 20, 3)) # 1부터 20까지 step size 3으로 한 요소 값들을 가지는 리스트로 초기화.
print(lstTest)
print(4 in lstTest, 100 in lstTest)
lstTest.append('hey')
print(lstTest)
del lstTest[0]
print(lstTest)
lstTest.reverse()   #리스트 요소들 거꾸로 정렬.
lstTest.remove(4)
print(lstTest)
