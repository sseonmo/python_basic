# Chapter03-1
# 파이썬 심화

# 시퀀스형 설명
# Dict Comprehenaion
# Hahstable
# setDefault
# User Defined Dictionary
# immutable Dict
# Set vs Frozenset

# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복허용 x, Set -> 중복허용 x
# Dict 및 Set 심화

# Dict 구조
print('EX1-1 -', )
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print('EX1-2 -', hash(t1))
# print('EX1-3 -', hash(t2))

print()
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 CSV TO List of tuple
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
	temp = csv.reader(f)
	# Header Skip
	next(temp)
	# 변환
	NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -', )
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()
print('EX2-2 -', )
print(n_code1)
print()
print()
print('EX2-3 -', )
print(n_code2)

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No Use setdefault
for k, v in source:
	if k in new_dict1:
		new_dict1[k].append(v)
	else:
		new_dict1[k] = [v]

print('EX3-1 -', new_dict1)

# Use setdefault
for k, v in source:
	# k가 있으면 디폴트값([])을사용
	new_dict2.setdefault(k, []).append(v)

print('EX3-2 -', new_dict2)
print()
print()
# 사용자 정의 dict 상속(UserDict 가능)
# 반드시 dict 를 상속받아야 dict 형태로 오버라이딩 할 수 있다.
class UserDict(dict):
	def __missing__(self, key):
		print('Called : __missing__')
		if isinstance(key, str):
			raise KeyError(key)
		return self[str(key)]

	def get(self, key, default=None):
		print('Called : __getitem__')
		try:
			return self[key]
		except KeyError:
			return default

	def __contains__(self, key):
		print('Called : __contains__')
		return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, tow=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ("two", 2)])
# 출력
print('EX4-1 -', user_dict1, user_dict2, user_dict3)
print('EX4-2 -', user_dict2.get('two')) # Called : __getitem__ ->(값이없으면) Called : __missing__
print('EX4-3 -', 'one' in user_dict3)   # Called : __contains__
# print('EX4-4 -', user_dict3['three'])   # __missing__ 바로 감.
print('EX4-5 -', user_dict3.get('three'))
print('EX4-6 -', 'three' in user_dict3)

