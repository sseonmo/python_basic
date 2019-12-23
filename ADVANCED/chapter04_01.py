# Chapter04-1
# 파이썬 심화

# 일급함수설명(일급객체)
# 파이썬 함수 특징
#   1. 런타임 초기화
#   2. 변수 등에 할당 가능
#   3. 함수 인수 전달 가능
#   4. 함수 결과로 반환가능

# 함수 객체 속성 확인
# Map, Filter, Reduce
# 익명함수
# 다양한 매개변수 사용

# 함수객체예제
def factorial(n):
	"""Factorial Function -> n:int """
	# print(n)
	if n == 1:  # n < 2
		return 1
	else:
		return n * factorial(n - 1)

class A:
	pass

print('EX-1 - ', factorial(5))
print('EX1-2 - ', factorial.__doc__)
print('EX1-3 - ', type(factorial), type(A))
print('EX1-4 - ', set(sorted(dir(factorial))) - set(sorted(dir(A))))  # 함수만 가지고 있는 함수
# EX1-4 -  {'__call__', '__get__', '__code__', '__qualname__', '__name__', '__globals__', '__kwdefaults__', '__defaults__', '__closure__', '__annotations__'}
print('EX1-5 - ', factorial.__name__)
print('EX1-6 - ', factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial
print('EX2-1 - ', var_func)
print('EX2-2 - ', var_func(5))
print('EX2-3 - ', map(var_func, range(1, 6)))
print('EX2-3 - ', list(map(var_func, range(1, 6))))
