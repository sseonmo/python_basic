#  +, * 연산자
print('py''thon')  # python - 중간에 + 생략되어 있다.
print('py' * 3)  # pypypy

# 문자 인덱싱 & 슬라이싱
tempStr = 'python'
print(tempStr[0])  # p
print(tempStr[5])  # n
print(tempStr[1:4])  # yth
print(tempStr[-2:])  # on

# 유니코드
print('가')
print(type('가'))
print('가'.encode('utf-8'))

print(type('가'.encode('utf-8')))

# 리스트
colors = ['red', 'green', 'gold']
print(colors)  # ['red', 'green', 'gold']

colors.append("blue")
print(colors)  # ['red', 'green', 'gold', 'blue']

colors.insert(1, 'black')
print(colors)  # ['red', 'black', 'green', 'gold', 'blue']

colors.extend(['white', 'gray'])
print(colors)  # ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray']

print(colors.index("black"))  # 1
# 검색범위 안에 값이 없으면 error
# print(colors.index("black", 3, 4))  # ValueError: 'black' is not in list

colors.append('red')
print(colors.count('red'))  # 2

print(colors)  # ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray', 'red']
print(colors.pop())  # red
print(colors)  # ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray']

# 세트
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # 합집합 - {1, 2, 3, 4, 5}
print(a.intersection(b))  # 교집합 - {3}

# 튜플
c, d = 1, 2
print(c, d)  # 1 2
c, d = d, c
print(c, d)  # 2 2

#  딕셔너리
# color = dict(apple='red', banana='yello')
color = {'apple': 'red', 'banana': 'yello'}
print(color["apple"])  # red
color["apple"] = 'green'
print(color["apple"])  # green
print(color.keys())  # dict_keys(['apple', 'banana'])
print(color.values())  # dict_values(['green', 'yello'])

for k, v in color.items():
	print(k, v)  # apple green, banana yello

color.__delitem__('apple')
print(color)
color.clear()
print(color)
print('aaa')

# 얕은복사 vs 깊은복사
from copy import copy, deepcopy

a = [1, [1, 2, 3]]
b = copy(a)

# 얕은복사
# 겉을 감사는 복합객체를 생성되었지만 내부객체를 동일한 객체를 바라본다
print(id(a), id(a))  # 4511448192 4511448192
print(id(a[0]), id(a[1]))  # 4509003536 4511825184
print(id(b[0]), id(b[1]))  # 4509003536 4511825184

# 변경하려는 객체의 성격(변이, 불변) 에 따라 객체가 재할당되거나 참조객체가 수정된다.
b[0] = 100  # immutable
b[1][0] = 11  # mutable

print(a, b)  # [1, [1, 2, 3]] [100, [1, 2, 3]]
print(id(a[0]), id(a[1]))  # 4509003536 4511825184
print(id(b[0]), id(b[1]))  # 4512185200 4511825184

# 깊은복사
# 모든 객체에 대해서 재할당한다.
c = deepcopy(a)
print(id(a), id(c))        # 4521155712 4521532384
print(id(a[0]), id(a[1]))  # 4518706960 4521532704
print(id(c[0]), id(c[1]))  # 4518706960 4521532624