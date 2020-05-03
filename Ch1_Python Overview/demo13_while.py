# while

i = 0
sum = 0
while i < 10:
    i += 1
    sum += i
else:               # while이 정상종료 될 경우, 실행
    print("Sum from 1 to 10 : ", sum)

i = sum = 0
while i < 10:
    i += 1
    if i == 5 :     # i가 5일 경우 while문 강제 종료.
        break
    sum += i
else:
    print("Sum from 1 to 10 : ", sum)
print("Good bye")

