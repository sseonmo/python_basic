# Chapter02-2
# 파이썬 Masic 메소드 설명
# Magic 메소드란?
# 매직메소드 생성 예제
# 매직메소드 객체 사용
# 매직메소드 예제 출력
# 기타내용

# Special Method(Magic Method)
# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직매소드 실습
# 파이썬의 중요한 핵식 프레임워크 - 시퀀스(Sequence), 반복(Interator), 함수(Functions), 클래스(Class)

# 매직메소드 기초 설명

# 기본형
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

n = 100
# 사용
print('EX1-1 -', n + 200)
print('EX1-2 -', n.__add__(200))
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(), bool(n))
print('EX1-5 -', n * 100, n.__mul__(100))

print()
print()

# class
class Student:
	def __init__(self, name, height):
		self._name = name
		self._height = height

	def __str__(self):
		return 'Student Class Info : {}, {}'.format(self._name, self._height)

	def __ge__(self, other):
		print('Called. >> __ge__ Method.')
		if self._height >= other._height:
			return True
		else:
			return False

	def __le__(self, other):
		print('Called. >> __le__ Method.')
		if self._height <= other._height:
			return True
		else:
			return False

	def __sub__(self, other):
		print('Called. >> __sub__ Method.')
		return self._height - other._height

# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# 매직메서드 출력
print('EX2-1 - ', s1 >= s2)
print('EX2-2 - ', s1 <= s2)
print('EX2-3 - ', s1 - s2)
print('EX2-4 - ', s2 - s1)
print('EX2-5 - ', abs(s2 - s1))
print('EX2-6 - ', s1)
print('EX2-7 - ', s2)

print()
print()

# 클래스 예제 2
class Vector(object):
	def __init__(self, *args):
		'''Create a vector, example : v = Vertor(1.2)'''

		if len(args) == 0:
			self._x, self._y = 0, 0
		else:
			self._x, self._y = args

	def __repr__(self):
		"""Return the informations"""
		# %r repr
		return 'Vertor(%r, %r)' % (self._x, self._y)

	def __add__(self, other):
		"""Return int vector addition of self and other"""
		return Vector(self._x + other._x, self._y + other._y)

	def __mul__(self, other):
		return Vector(self._x * other, self._y * other)

	def __bool__(self):
		return bool(max(self._x, self._y))
# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직메소드 출력
print('EX3-1 - ', Vector.__init__.__doc__)
print('EX3-2 - ', Vector.__repr__.__doc__)
print('EX3-3 - ', Vector.__add__.__doc__)
print('EX3-4 - ', v1, v2, v3)
print('EX3-5 - ', v1 + v2)
print('EX3-6 - ', v1 * 4)
print('EX3-7 - ', v2 * 10)
print('EX3-8 - ', bool(v1), bool(v2))
print('EX3-9 - ', bool(v3))

print()
print()


