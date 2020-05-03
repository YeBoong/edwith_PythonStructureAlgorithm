# 조건문 if
# 파이썬은 case문이 없기 때문에
# if로 구현해야한다.

numScore = 95
if numScore > 90 :
    print('A')

numScore = 75
if numScore > 90 :
    print('A')
else :
    print('Lower Grade')

if numScore > 90 :
    print('A')
elif numScore > 80 :
    print('B')
elif numScore > 70 :
    print('C')
else :
    print('D or F')
    