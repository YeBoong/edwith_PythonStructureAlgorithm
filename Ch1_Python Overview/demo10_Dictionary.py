# 딕셔너리
# 키와 값의 한 쌍으로 이루어져 있다는게 특징

dicTest = {1 : 'one', 2 : 'two', 3 : 'three'}
print(dicTest[1])   # 'one'
dicTest[4] = 'four' # 요소 추가
dicTest[1] = 'hana' # 키 '1'의 값 변경
print(dicTest)
print(dicTest.keys()) # 키만
print(dicTest.values()) # 값만
print(dicTest.items()) # 키와 쌍 둘 다


