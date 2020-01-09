# Chapter06-1
# 파이썬 심화
# 흐름제어, 병행처리(concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제너레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter(x) 함수 호출
# iterable : 한마디로 반복가능한 객체
# iterator : 값을 차례대로 꺼낼수 있는 객

t = 'ABCDE'

# for 사용
for c in t:
	print('EX1-1 -', c)

print()
# while 사용
print(type(t))
w = iter(t)
print(type(w))
while True:
	try:
		print('EX1-2 -', next(w))
	except StopIteration:
		break

print()
from collections import abc

# 반복형 확인
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))

print()
print()

class WordSplitIter:
	def __init__(self, text):
		self._idx = 0
		self._text = text.split(' ')

	def __next__(self):
		print('Called __next__')
		try:
			word = self._text[self._idx]
		except IndexError:
			raise StopIteration('stop')

		self._idx += 1
		return word

	def __iter__(self):
		print('Called __iter__')
		return self

	#
	# def __str__(self):
	# 	print('__str__')
	# 	return 'WordSplit{}'.format(self._text)

	def __repr__(self):
		print('__str__')
		return 'WordSplit(%s)' % self._text

# next 사용

wi = WordSplitIter('Who says the nights are for sleeping')

print('EX2-1 -', wi)
print('EX2-2 -', next(wi))
print('EX2-3 -', next(wi))
print('EX2-4 -', next(wi))
print('EX2-5 -', next(wi))
print('EX2-6 -', next(wi))
print('EX2-7 -', next(wi))
print('EX2-8 -', next(wi))
# print('EX2-2  -', next(wi))

print()
print()

# Generator
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제네레이터 완화
# 2. 단위 실행 가능한 코루틴(coroutine) 구형에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출 할 때마다 하나의 값만 리턴-> 아주 작은 메모리 양을 필요로 함
class WordSplitGenerator:
	def __init__(self, text):
		self._text = text.split(' ')

	def __iter__(self):
		for word in self._text:
			yield word
		return

	def __repr__(self):
		print('__str__')
		return 'WordSplit(%s)' % self._text

wg = WordSplitGenerator('Who says the nights are for sleeping')
wt = iter(wg)

print('EX3-1 -', wt)
print('EX3-2 -', next(wt))
print('EX3-3 -', next(wt))
print('EX3-4 -', next(wt))
print('EX3-5 -', next(wt))
print('EX3-6 -', next(wt))
print('EX3-7 -', next(wt))
print('EX3-8 -', next(wt))

# print('EX3-9 -', next(wt))

# Genarator 예제1
def generator_ex1():
	print('start')
	yield 'AAA'
	print('continue')
	yield 'BBB'
	print('end')

temp = iter(generator_ex1())

# print('EX4-1 -', next(temp))
# print('EX4-2 -', next(temp))
# print('EX4-3 -', next(temp))

for v in generator_ex1():
	pass
	print('EX4-3 -', v)

print()
print()
# Generator 예제2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print('EX5-1 -', temp2)
print('EX5-2 -', temp3)
# EX5-1 - ['AAAAAAAAA', 'BBBBBBBBB']
# EX5-2 - <generator object <genexpr> at 0x10e1e2dd0> -> 아직 계산이 되어있지않아 메모리를 먹지 않는다.

for i in temp2:
	print('EX5-3 -', i)

print()
print()

for i in temp3:
	print('EX5-4 -', i)

print()
print()

# Genarator 예제3 ( 자주사용하는 함수 )
import itertools

gen1 = itertools.count(1, 2.5)  # next()로 호출될때만다 2.5을 더한 후 값을 반환

print('EX6-1 -', next(gen1))
print('EX6-2 -', next(gen1))
print('EX6-3 -', next(gen1))
print('EX6-4 -', next(gen1))
# ... 무한

# 조건
# takewhile(predicate, iterable)
# predicate 는 True 나 False 를 리턴하는 함수라고 보면 되고, iterable 은 리스트, 튜플, 문자열과 같이 각각의 요소에 접근할 수 있는 자료형이라고 보면 된다.
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
	print('EX6-5 -', v)

print()

# 필터 반대 - 조건의 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
	print('EX-6-6 -', v)

print()

# 누적합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
	print('EX6-6 -', v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print('EX6-7 -', list(gen5))  # EX6-7 - ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결2
gen6 = itertools.chain(enumerate('ABCED'))
print('EX6-8 -', list(gen6))  # EX6-8 - [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'E'), (4, 'D')]

# 개별
gen7 = itertools.product('ABCED')  # EX6-9 - [('A',), ('B',), ('C',), ('E',), ('D',)]
print('EX6-9 -', list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCED', repeat=2)
print('EX6-10 -', list(gen8))
# EX6-10 - [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'E'), ('A', 'D')
# , ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'E'), ('B', 'D')
# , ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'E'), ('C', 'D')
# , ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'E'), ('E', 'D')
# , ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'E'), ('D', 'D')]

# 그룹화
gen9 = itertools.groupby('AAAABBCCCCDDEEEE')
# print('EX6-11 -', list(gen9))

for chr, group in gen9:
	print('EX6-12 -', chr, ':', list(group))

print()
