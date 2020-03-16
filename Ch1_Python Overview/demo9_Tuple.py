# 튜플은 리스트와 매우 유사하지만 한번 초기화 된 요소 값은
# 변경할 수 없다는 것이 차이점.
tplTest = (1, 2, 3)
print(tplTest)
print(tplTest[0], tplTest[1], tplTest[2])
print(tplTest[-1], tplTest[-2])
print(tplTest[1:3])
print(tplTest+tplTest)
print(tplTest*3)

tplTest[0] = 100    # 값을 변경할 수 없다.
                    # 튜플과 리스트의 차이점.
