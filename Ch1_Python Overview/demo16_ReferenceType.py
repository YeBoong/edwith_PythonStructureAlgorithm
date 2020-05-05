x = [1, 2, 3]
y = [100, x, 120]   
z = [x, 'a', 'b']
# y와 z는 x에 대해서 'value type'가 아닌,
# 'reference type'로 저장한다.
# 즉, x에 저장된 값들을 그대로 저장하는게 아니라,
# x에 대한 메모리 주소를 저장하기 때문에
# x의 값 변경이 이루어지면
# y와 z 역시 값이 변경 됨을 볼 수 있다.

print('x : ', x)        # 1, 2, 3
print('y : ', y)        # 100, [1, 1717, 3], 120
print('z : ', z)        # [1, 1717, 3], 'a', 'b'

x[1] = 1717             

print('\nx : ', x)      # 1, 1717, 3
print('y : ', y)        # 100, [1, 1717, 3], 120
print('z : ', z)        # [1, 1717, 3], 'a', 'b'

x[1] = 2
x2 = [1, 2, 3]

# '==' : 값이 같은지 비교한다.
# 'is' : 참조하는 메모리 주소가 같은지 비교한다.

if x==x2:
    print("Values are equivalent")
else:
    print("Values are not equivalent")

if x is x2:
    print("Values are stored at the same price")
else:
    print("Values are not stored at the same price")

if x[1] is y[1][1]:
    print("Values are stored at the same price")
else:
    print("Values are not stored at the same price")
