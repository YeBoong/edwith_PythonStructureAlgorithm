strTest = "Hello World! ISE"
print(strTest)
print(strTest[1], strTest[2], strTest[3])
print(strTest[1:3])     # index 1부터 3까지
print(strTest[3:])      # index 3부터 끝까지
print(strTest[:3])      # index 처음부터 3까지
print(strTest[1:9:2])   # index 1부터 9까지 step size 2로.
                        # 즉, index 1, 3, 5, 7, 9
print(strTest[1:len(strTest):2])    # index 1부터 (문자열 총 길이 수)까지 step size 2로.
print(strTest[1::2])    # index 1부터 끝까지 step size 2로.
print(strTest[5::-1])   # index 5부터 처음까지 step size -1로.
                        # 즉, 5,4,3,2,1,0 으로 거꾸로 출력.
