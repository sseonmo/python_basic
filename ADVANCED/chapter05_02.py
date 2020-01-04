# Chapter05-2
# 파이썬 심화

# 파이썬 클래스 관련 메소드 심화
#   private 속성실습
#       - self.__a : `__` 이용한 private 변수 생성하여 instence 에서 접근불가능하게 만든다.
#       - Getter, Setter 이용하여 메소드를 활용해서 변경가능하게 만든다.
#           - 변수명으로 method 생성하는 것이 관례
# 		    - Getter : @property 어노테이션 이용함
# 	        - Setter : @[getter 메소드명].setter / Getter의 메소드명과 동일하게 생성해야함.
#   __slot__ 예제 - 메모리 절감효과
#   객체슬라이딩, 인덱싱
#   ABC, 상속, 오버라이딩

# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# class 선언
class VectorP(object):
	def __init__(self, x, y):
		self.__x = float(x)
		self.__y = float(y)

	def __iter__(self):
		print('__init__ call')
		return (i for i in (self.__x, self.__y))  # Generator

	# Getter 역활
	@property
	def x(self):
		print('Called property X')
		return self.__x

	# Setter 역활 - getter와 이름이 동일해야한다.
	@x.setter
	def x(self, v):
		print('Called property X Setter')
		self.__x = v

	# Getter 역활
	@property
	def y(self):
		print('Called property Y')
		return self.__y

	# Setter 역활 - getter와 이름이 동일해야한다.
	@y.setter
	def y(self, v):
		print('Called property Y Setter')
		if v < 30:
			raise ValueError('30 below is not possible')
		self.__y = float(v)

v = VectorP(20, 40)
# 객체선언

# '__' = private , 인스턴스를 이용하더라도 접근불가
# print('EX1-1 -', v.__x, v.__y)

# Getter, Setter
print(v.x)
v.x = 10
v.y = 40
print('EX1-2 -', dir(v), v.__dict__)
print('EX1-3 -', v.x, v.y)

# Iter 확인
for val in v:
	print('EX1-4 -', val)

print()
print()

# __slot__
# 파이썬 인터프리터에게 통보
# 핵심 : 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용
# 반드시 문자열로 입력해야 한다.
# 참조설명 - https://planbs.tistory.com/entry/Python-slots
#   알려진(known) 속성들로 구성된 클래스들의 경우 이러한 구조는 딕셔너리가 낭비하는 RAM 때문에 병목이 발생할 수 있습니다.
#   클래스 레벨에 __slots__라는 변수를 설정해서, 해당 클래스에 의해 만들어진 객체의 인스턴스 속성 관리에 딕셔너리 대신
#   속성에 대한 고정된(fixed) set을 사용하도록 할 수 있습니다.

class TestA(object):
	__slots__ = ('a',)

class TestB:
	pass

use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__) # error
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
	def repeat_inner():
		obj.a = 'TEST'
		del obj.a

	return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number=10000)))
print(min(timeit.repeat(repeat_outer(no_slot), number=10000)))

print()
print()

# 객체 슬라이싱
class Objects:
	def __init__(self):
		self._numbers = [n for n in range(1, 100, 3)]

	def __len__(self):
		return len(self._numbers)

	def __getitem__(self, idx):
		return self._numbers[idx]

s = Objects()

print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s))
print('EX3-3 -', len(s._numbers))
print('EX3-4 -', s[1:100])
print('EX3-5 -', s[-1])
# 시퀀스객체[::증가폭]
print('EX3-5 -', s[::10])
# 시퀀스객체[시작인덱스::증가폭]
print('EX3-6 -', s[::5])

# 파이썬 추상클래스
# 참고 : https://docs.python.org/3/library/collections.abc.html

# 추상클래스 사용이유
# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서  인스턴스를 생성해야함
# 개발과 관련된 공통된 내용(필드, 메소드)을 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contailn__ 기능 작동
# 객체 전체를 자동으로조사 -> 시퀀스 프로토콜

class IterTestA:
	def __getitem__(self, item):
		print(repr(item))
		return range(1, 50, 2)[item]  # range(1, 50, 2)

i1 = IterTestA()
print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4:10])
print('EX4-3 -', 3 in i1[1:10])
# print('EX4-4 -', [i for i in i1])     # 이해가 안됨
# print('EX4-4 -', [i for i in i1[:]])

print()
print()

# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작

from collections.abc import Sequence

class IterTestB(Sequence):
	def __getitem__(self, item):
		print('__getitem__', repr(item))
		return range(1, 50, 2)[item]  # range(1, 50, 2)

	def __len__(self, idx):
		print('__len__', repr(idx))
		return len(range(1, 50, 2)[idx])

i2 = IterTestB()
print('EX4-5 -', i2[4])
print('EX4-6 -', i2[4:10])
print('EX4-7 -', 3 in i2[1:10])
print()
print()
# abc 활용예제 - abstract class
import abc

class RandomMachine(abc.ABC):  # metaclass=abc.ABCMeta(3.4이하)
	# __metaclass__ = abc.ABCMeta

	# 추상메소드
	@abc.abstractmethod
	def load(self, iterobj):
		"""Iterable 항목추가"""

	# 추상메소드
	@abc.abstractmethod
	def pick(self):
		"""무작위 항목 뽑기"""

	def inspect(self):
		items = []
		while True:
			try:
				items.append(self.pick())
			except LookupError:
				break
			return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
	def __init__(self, items):
		self._readomizer = random.SystemRandom()
		self._items = []
		self.load(items)

	def load(self, iterobj):
		self._items.extend(iterobj)
		self._readomizer.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:  # item이 더이상 없을때 에러발생함.
				raise LookupError('Empty Crane Box')

	def __call__(self):
		return self.pick()

# 서브클래스 확인 - issubclass(자식, 부모)
print('EX5-1 -', issubclass(RandomMachine, CraneMachine))
print('EX5-2 -', issubclass(CraneMachine, RandomMachine))

# 상속 구조 확인
print('EX5-3 -', CraneMachine.__mro__)
cm = CraneMachine(range(1, 100)) # 추상메소드 구현 안하면 에러

print('EX5-4 -', cm._items)
print('EX5-5 -', cm.pick())
print('EX5-6 -', cm())
print('EX5-7 -', cm.inspect())

