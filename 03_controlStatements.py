# if 문
"""
if <조건식>:
	<구문>
"""
value = 10
if value > 5:
	print('value is bigger than 5')  # value is bigger than 5

"""
if <조건식 1>:
	<구문 1>
elif <조건식 2>:
	<구문 2>
else:
	<구문 3>
"""

# score = int(input('Input Score: '))     # 사용자로부터 정수값을 입력받음
score = 90
if 90 <= score <= 100:
	grade = 'A'
elif 80 <= score < 90:
	grade = 'B'
elif 70 <= score < 80:
	grade = 'C'
elif 60 <= score < 70:
	grade = 'D'
else:
	grade = 'F'

# input 80 / Grade is B
print('Grade is {}'.format(grade))

# and / or
"""
	and = & / or = | 축약가능
	하지만 동일하게 수행되는 것은 아님
"""
# ZeroDivisionError: division by zero 에러발생
# 첫번째 조건문 & => and 였다면 이상없이 수행됨. (에러없이통과)
a = 0
if a and 10 / a:
	print("a는 0입니다.")
else:
	print("에러없이통과")

# 단축평가 - 조건식 전체를 판단하지 않고 순척적으로 진행한다. 좌 => 우

#  while 문

"""
조건문이 참(True)인 동안 내부 구문을 반복수행
while <조건식>:
	<구문>
"""
value = 5
while value > 0:
	print(value)
	value -= 1
# 5\n 4\n 3\n 2\n 1

# for 문
"""
시퀀스형 객체를 순차적으로 순회
for <아이템 I> in <시퀀스형 객체 S>:
	<구문>
"""
l = ['Apple', 100, 15, 23]
for i in l:
	print(i)
# Apple
# 100
# 15
# 23
d = {"apple": 100, "orange": 200, "Banana": 300}
for k, v in d.items():
	print('{} | {}'.format(k, v))
# apple | 100
# orange | 200
# Banana | 300

# break - 반목문 내부 클록을 벗어남
for i in range(1, 10):
	if i > 5:
		break
	print('item: {}'.format(i))
# item: 1
# item: 2
# item: 3
# item: 4
# item: 5

# continue - 내부 블록을 수행하지 않고 다음차례를 순회.
for i in range(1, 10):
	if i % 2 == 0:
		continue
	print('item: {}'.format(i))
# item: 1
# item: 3
# item: 5
# item: 7
# item: 9


# else - 반복문 수행도중 break로 인하여 중간에 종료되지 않고 끝까지 수행되었을때, else 블록을 수행
for i in range(1, 10):
	if i % 2 == 0:
		continue
	print('item: {}'.format(i))
else:
	print('Exit without break!')  # 외부루프문장

# 리스트 내장
"""
기존 시퀀스 객체를 이용하며 추가적인 연산을 통하여 새로운 리스트 객체 생성
if문을 옵션으로 filter 처럼 사용가능함.
[<표현식> for <아이템> in <시퀀스 객체> (if <조건식>)]
"""
q = [1, 2, 3, 4, 5]
q2 = [i ** 2 for i in q]
print(q2)  # [1, 4, 9, 16, 25]

t = ("orange", "apple", "banana", "kiwi")
t2 = [len(i) for i in t]
print(t2)  # [6, 5, 6]
# if문을 통한 필터링
t3 = [i for i in t if len(i) > 5]
print(t3)  # ['orange', 'banana']

# 원본리스트 2개
L_1 = [3, 4, 5]
L_2 = [1.5, -0.5, 4]
L_3 = [x * y for x in L_1 for y in L_2]
print(L_3)  # [4.5, -1.5, 12, 6.0, -2.0, 16, 7.5, -2.5, 20]

# 유용한 함수
# filter
# 함수의 결과값이 참인 시퀀스 객체의 이터레이터를 반환
# None이 오는 경우 필터링 하지 않음
"""
filter(<function>|None, 시퀀스 객체)
"""
LL = [10, 25, 30]
IterL = filter(None, LL)
# item : 10 / item : 20 / item : 30
for i in IterL:
	print('item : {}'.format(i))

def GetBiggerThan20(i):
	return i > 20

print(list(filter(GetBiggerThan20, LL)))  # [25, 30]

print(list(filter(lambda i: i > 20, LL)))  # [25, 30]

# range
"""
range([시작값],종료값[,증가값]
- 시작값과 종료값은 생략가능하면, 이때는 각각 0 과 1이 할당된다.
"""
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10, 20, 2)))  # [10, 12, 14, 16, 18]

# map
"""
map(<function>, 시퀀스 객체, ...)
- 시퀀스 객체를 순회하며 function구문의 연산을 수행
- 함수의 인자 수만큼 시퀀스 객체를 전달
"""
M = [1, 2, 3]

def add10(i):
	return i + 10

print(list(map(add10, M)))  # [11, 12, 13]

# item : 11 / item : 12 / item : 13
for i in map(add10, M):
	print('item : {}'.format(i))

X = [1, 2, 3]
Y = [2, 3, 4]
# pow 지수 계산 | 1 ** 2, 2 ** 3, 3 ** 4
print(list(map(pow, X, Y)))  # [1, 8, 81]
