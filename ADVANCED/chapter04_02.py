# Chapter04-2
# 파이썬 심화
# 일급함수(일급객체)
# Docorator & Closure

# 데코레이터 설명
#   파이썬 변수 범위
#   여러가지 클로져 구현
#   클로저 속성
#   데코레이터 작성 예제
#   데코레이터 작동원리

# 파이썬 변수 범위(global)

# 예제1
def func_v1(a):
	print(a)
	print(b)

# 예외
# func_v1(5)
b = 10

# 예제2
def func_v2(a):
	print(a)
	print(b)

func_v2(5)

# 예제3
def func_v3(a):
	print(a)
	print(b)
	b = 5

# print(func_v3(5))

# 바이트코드(파이썬 인터프리터)의 실행 흐림을 볼 수 있는 package
from dis import dis

print('EX1-1 -', )
print(dis(func_v3))

print()
print()

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언 된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드를 직접 접근이 가능하다.

a = 10
print('EX2-1 -', a + 10)
print('EX2-2 -', a + 100)

# 결과누적
print('EX2-3 -', sum(range(1, 51)))
print('EX2-4 -', sum(range(51, 100)))

print()
print()

# 클래스 이용
class Average():
	def __init__(self):
		self._serise = []

	def __call__(self, v):
		self._serise.append(v)
		print('class >>> {} / {}'.format(self._serise, len(self._serise)))
		return sum(self._serise) / len(self._serise)

# 인스터느 생성
avg_cls = Average()
