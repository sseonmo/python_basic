# Chapter05-1
# 파이썬 심화

# 파이썬 참조 심화
#   파이썬 객체 참조 다양한 특징
#   Copy
#   Deep Copy
#   매개변수 전달 주의할 점

# 갹체 참조 중요한 특징들
# Python Object Reference

print('EX!-1 -')
print(dir())

# id vs __eq__ (==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x
# 얇은 복사
print('EX2-1 -', id(x), id(y))  # EX2-1 - 4446430304 4446430304
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)

print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}
print('EX2-6 -', x, z)
print('EX2-7 -', x is z)  # 같은 객체인지 판별 / id() 값은 틀림
print('EX2-8 -', x is not z)
print('EX2-9 -', x == z)  # 값은 동일

# 객체 새성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, '=='(__eq__)는 값을 비교
print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

print()
print()

# Copy, DeepCopy

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)  # EX4-1 - True
print('EX4-2 -', tl1 is tl2)  # EX4-2 - True
print('EX4-3 -', tl1 == tl3)  # EX4-3 - True
# 생성자를 통해서 다른 객체를 생성한다. - list(tl1)
print('EX4-4 -', tl1 is tl3)  # EX4-4 - False
print('EX4-4 -', tl1 == tl3)  # EX4-4 - True

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()
print(id(tl1[2]))
tl1[1] += [100, 120]
tl1[2] += (100, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2)  # 튜플 재 할당 (객체 새로 생성) - 불편객체
print('EX4-10 -', tl3)
print(id(tl1[2]))

print()
print()

# Deep Copy

# 장바구니
class Basket():
	def __init__(self, products=None):
		if products is None:
			self._products = []
		else:
			self._products = list(products)

	def put_prod(self, prod_name):
		self._products.append(prod_name)

	def del_prod(self, prod_name):
		self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
# 얇은복사 : 객체(첫번재 data type만)는 재생성하지만 인스턴스의 속성들은 복사가 되지 않는다.
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -', id(basket1), id(basket2), id(basket3))  # EX5-1 - 4470073744 4469926288 4469713744
print('EX5-2 -', id(basket1._products), id(basket2._products),
      id(basket3._products))  # EX5-2 - 4405600336 4405600336 4405809952z

print()
basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('Ex5-3 -', basket1._products)
print('Ex5-4 -', basket2._products)
print('Ex5-5 -', basket3._products)

# 함수 매개벼수 전달 사용법

