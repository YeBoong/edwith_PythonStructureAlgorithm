# for
# 가장 일반적인 루프 문
# continue : 현재 조건에 대한 루프를 넘기고, 다음 조건부터 새로 시작
# break : 반복문을 종료하고 빠져나옴.

for i in range(10) :
    print(i, end = ' ')
print()

sum = 0
for i in range(1, 11):
    sum += 0
print(sum)
for i in range(1, 100, 10) : # 1부터 10까지 stepsize 10으로
    if i == 51:   # i가 51일 경우 그에 대한 루프를 뛰어넘고 다음 조건인 61부터 시작.
        continue
    else:
        print(i, end = ' ')
print()

for i in range(5) :
    print(i, end = ' ')
else:               # for문에서의 else는 for문이 끝났을 때 실행.
    print('!')
print('done')

print()

for i in range(5) : 
    if i == 3:
        break
    print(i, end = ' ')
else :              # break 문과 같이 반복문을 강제 종료로 빠져나올 경우는 else문이 실행 되지 않는다.
    print('!')
print('done')

