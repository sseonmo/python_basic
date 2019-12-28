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
# 외부함수(포함하고 있는)의 변수에 접근할 수 있는 내부 함수를 일컫습니다.
# 스코프 체인(scope chain)으로 표현되기도 합니다

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

# 인스턴스 생성
avg_cls = Average()

# 누적확인
print('EX-3-1 -', avg_cls(15))
print('EX-3-2 -', avg_cls(35))
print('EX-3-3 -', avg_cls(40))

print()
print()

# 크로저(Closure) 사용
# 전역변수 사용 감소
# 다지인 패턴 적용

def closure_acg1():
	# Free variable
	series = []
	a = 0

	# 클로져 영역
	def averager(v):
		series.append(v)
		print('def >>> {} / {}'.format((series), len(series)))
		return sum(series) / len(series)

	return averager

avg_closure1 = closure_acg1()

print('EX4-1 -', avg_closure1(15))
print('EX4-2 -', avg_closure1(35))
print('EX4-3 -', avg_closure1(40))

print()
print()

print('EX5-1 -', dir(avg_closure1))
print()
print('EX5-2 -', dir(avg_closure1.__code__))
print()
print('EX5-3 -', avg_closure1.__code__.co_freevars)
print()
print('EX5-4 -', dir(avg_closure1.__closure__[0]))
print()
print('EX5-5 -', dir(avg_closure1.__closure__[0].cell_contents))

print()
print()

# 잘못된 클로져 사용 예

def closure_avg2():
	# free variable
	cnt = 0
	total = 0

	# 클로져 영역
	def averager(v):
		nonlocal cnt, total
		cnt += 1
		total += v
		print('def2 >>> {} / {}'.format(total, cnt))
		return total / cnt

	return averager

avg_closure2 = closure_avg2()

print('EX5-6 -', avg_closure2(15))
print('EX5-7 -', avg_closure2(35))
print('EX5-8 -', avg_closure2(40))

# 데코레이터 실습
# 1. 중복제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함
# 3. 에러 발생지점 추적 어려움

import time

def perf_clock(func):
	def perf_clocked(*args):
		# 시작시간
		st = time.perf_counter()
		result = func(*args)
		# 종료시간
		et = time.perf_counter() - st
		# 함수명
		name = func.__name__
		# 매개변수
		arg_str = ','.join(repr(arg) for arg in args)
		# 출력 | %s : str | %r : repr | %f : 실수 | %d : 정수
		# %0.5f => 실수 5자리까지
		print('Result [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
		return result

	return perf_clocked

@perf_clock
def time_func(seconds):
	time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
	return sum(numbers)

@perf_clock
def fact_func(n):
	return 1 if n < 2 else n * fact_func(n - 1)

# 5 : 5 * 24
# 4 : 4 * 6
# 3 : 3 * 2
# 2 : 2 * 1
# 1 : return 1

# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
print('EX7-2 -', non_deco2, non_deco2.__code__.co_freevars)
print('EX7-3 -', non_deco3, non_deco3.__code__.co_freevars)

# print('*' * 40, 'Called Non Deco -> time_func')
# print('EX7-4 -')
# non_deco1(2)
# print('EX7-5 -')
# non_deco2(100, 200, 300, 500)
# print('EX7-6 -')
# non_deco3(10)

print()
print()
print('*' * 40, 'Called Non Deco -> time_func')
print('EX7-7 -')
time_func(2)

print('*' * 40, 'Called Non Deco -> time_func')
print('EX7-8 -')
sum_func(100, 200)

print('*' * 40, 'Called Non Deco -> time_func')
print('EX7-9 -')
fact_func(5)