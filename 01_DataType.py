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
color = dict(apple='red', banana='yello')
print(color["apple"])  # red
color["apple"] = 'green'
print(color["apple"])  # green
print(color.keys())  # dict_keys(['apple', 'banana'])
print(color.values())  # dict_values(['green', 'yello'])

for k, v in color.items():
    print(k, v)  # apple green, banana yello
