# Chapter03-1
# 파이썬 심화

# 시퀀스형 설명
# List Comprehenaion
# Container VS flat
# Generator
# List VS Array
# Mutable VS Immutable
# Sort VS Sorted

# 컨테이너(Container) : 서로 다른 자료형 [list, tuple, collections.deque ]
# Flat : 한 개의 자료형 [ str, bytes, bytearray, array.array, memoryview ] - 성능상 더 빠르다
# 가변 : list, bytearray, array.arrat memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트 (Comprehending Lists)

# Non Comprehending Lists
from array import array

chars = '!@#$%%^&*(_'
codes1 = []
for c in chars:
	codes1.append(ord(c))

# Comprehending Lists - 데이터 양이 많을때 더 빠름(빅데이터)
codes2 = [ord(c) for c in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(c) for c in chars if ord(c) > 40]
# map(<function>, 시퀀스 객체, ...)
# lambda 인수: <구문>
# filter(<function>|None, 시퀀스 객체)
codes4 = list(filter(lambda x: x > 40, map(ord, chars)))  # 가독성도 괜찮아 보임

print('EX-1-1 -', codes1)
print('EX-1-2 -', codes2)
print('EX-1-3 -', codes3)
print('EX-1-4 -', codes3)
print('EX-1-5 -', [chr(c) for c in codes1])
print('EX-1-6 -', [chr(c) for c in codes2])
print('EX-1-7 -', [chr(c) for c in codes3])
print('EX-1-8 -', [chr(c) for c in codes4])
print('EX-1-8 -', "".join([chr(c) for c in codes2]))

print()
print()

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X )
# 값을 가지는 구조만 구성한다.
# 실제 사용을 할때 값을 생성한다.
# 한마디로 대기상태이고 값을 사용할때 메모리에 할당한다.
#  generator expression = ()
tuple_g = (ord(c) for c in chars)
# Array
array_g = array('I', (ord(c) for c in chars))
# array_g = array('str', (ord(c) for c in chars))

print("EX-2-1 -", tuple_g)  # EX-2-1 1 <generator object <genexpr> at 0x10aa95cd0>
print("EX-2-2 -", next(tuple_g))
print("EX-2-3 -", next(tuple_g))
print("EX-2-4 -", array_g)
print("EX-2-5 -", array_g.tolist())

# 제네레이터 예제
print("EX-3-1 -", ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
	print('EX-3-2 -', s)

print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('Ex4-1 -', marks1)
print('Ex4-2 -', marks2)
# Ex4-1 - [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
# Ex4-2 - [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

print()
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('Ex4-3 -', marks1)
print('Ex4-4 -', marks2)
# Ex4-3 - [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~']]
# Ex4-4 - [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]

# 증명
print('Ex4-5 -', [id(l) for l in marks1])
print('Ex4-6 -', [id(l) for l in marks2])
# Ex4-5 - [4515001600, 4515001440, 4515001360]
# Ex4-6 - [4515001200, 4515001200, 4515001200]

# Tuple Advanced

# Packing & Unpacking
print('Ex5-1 -', divmod(100, 9))
print('Ex5-2 -', divmod(*(100, 9)))
print('Ex5-3 -', *(divmod(100, 9)))  # 자주 사용하지 않는 스타일

print()

x, y, *rest = range(10)
print('Ex5-4 -', x, y, rest)
x, y, *rest = range(2)
print('Ex5-5 -', x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print('Ex5-6 -', x, y, rest)

print()
print()

# Mutable(가변) VS Immutable(불편)
i = (10, 15, 20)
m = [10, 15, 20]
print('Ex6-1 -', i, m, id(i), id(m))

i = i * 2
m = m * 2
print('Ex6-2 -', i, m, id(i), id(m))

i *= 2
m *= 2
print('Ex6-3 -', i, m, id(i), id(m))
# Ex6-1 - (10, 15, 20) [10, 15, 20] 4316721392 4316803712
# Ex6-2 - (10, 15, 20, 10, 15, 20) [10, 15, 20, 10, 15, 20] 4316566368 4316803632
# Ex6-3 - (10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20) [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20] 4315648880 4316803632

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'lemon', 'papaya', 'coconut', 'strawberry']

# sorted :  정렬 후 '새로운 객체' 반환
print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
print('EX7-3 -', sorted(f_list, key=len))
print('EX7-4 -', sorted(f_list, key=lambda x: x[-1]))  # 마지막 글자로 정렬
print('EX7-5 -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print('EX7-6 -', f_list)  # 원본은 변경되지 않음

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인 None하면 객체를 직접 변경하는 함수라고 생각할 수 있다.
a = f_list.sort()
print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
