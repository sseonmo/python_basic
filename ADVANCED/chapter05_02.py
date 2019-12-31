# Chapter05-2
# 파이썬 심화

# 파이썬 클래스 관련 메소드 심화
#   private 속성실습
#       - self.__a : __ 이용한 private 변수 생성하여 instence 에서 접근불가능하게 만든다.
#       - Getter, Setter 이용하여 메소드를 활용해서 변경가능하게 만든다.
#           - 변수명으로 method 생성하는 것이 관례
# 		    - Getter : @property 어노테이션 이용함
# 	        - Setter : @[getter 메소드명].setter / Getter의 메소드명과 동일하게 생성해야함.
#   __slot__ 예제
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
v.y = 20

# Iter 확인
for val in v:
	print('EX1-2 -', val)
