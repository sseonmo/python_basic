# Exception
"""
- 프로그램의 제어 흐름을 조정하기 위해 사용하는 이벤트
- 처리를 하지 않는 예외는 자동으로 에러(ERROR)가 발생하고 프로그램 종료된다.

#### 처리되지 않는 예외( Unhandled Exeception ) - 실해중 에러가 발생하기 때문에.. 체크예외 에러이다(java 용어 기준)
- '0' 으로 나누는 경우
- 원격에 있는 데이터베이스 접속 시 연결되는 않는 경우
- 파일을 열었는데 사용자에 의해서 삭제된 경우

### 자주발생하는 대표적인 예외
- NameError : 선언하지 않는 변수에 접근
- ZeroDivisionError : '0' 으로 나눔
- IndexError : 리스트에 접근 가능한 인덱스를 넘음
- TypeError :  지원하지 않는 연산 (ex) 정수를 문자열로 나눔

### 주요 내장 예외
- Exception : 모든 내장 예외의 기본클래스 / 사용자 정의 예외를 작성시 활용
- ArithmeticError : 수치연산 예외의 기본클래스
- LookupError : 시퀀스 관련 예외의 기본 클래스
- EnvironmentError : 파이썬 외부 에러의 기본클래스
"""

"""
### 예외처리
### try 구문
try:
	<예외 밸생가능성이 잇는 문장>
expect <예외종류>:
	<예외처리문장>
expect <예외1, 예외2>:
	<예외처리문장>
expect 예외 as 인자:
	<예외처리문장>
else:
	<예외가 발생하지 않는 경우 수행할 문장> - option
finally:
	<예외 발생 유무에 상관없이 try 블록 이후 수행할 문장>
"""

# ex) 1
def divide(a, b):
	return a / b

"""
Result: 2.5
항상 finally 블록은 수행합니다.
모든 인수는 숫자이여야 합니다. unsupported operand type(s) for /: 'int' and 'str'
"""
try:
	c = divide(5, 'a')
except ZeroDivisionError:
	print('두번째 인수는 0이면 안됩니다.')
except TypeError as e:
	print('모든 인수는 숫자이여야 합니다.', e)
else:  # 예외 발생하지 않는 경우
	print('Result: {0}'.format(c))
finally:  # 예외 발생 유무와 상관없이 수행
	print('항상 finally 블록은 수행합니다.')

# ex) 2
"""
수치 연산 관련 에러입니다.
"""
try:
	c = divide(5, 0)
except (ZeroDivisionError, OverflowError, FloatingPointError):
	print('수치 연산 관련 에러입니다.')
except TypeError as e:
	print('모든 인수는 숫자이여야 합니다.', e)
except Exception:
	print('무슨에러인지')

"""
- Exception 에서 상위클래스를 처리 할 시 하위에 하위클래스 처리가 있어도 상위클래스에서 처리가 된다.

### raise 구문
- 명시적으로 예외발생
	> raise [Exception]
		raise [Exception(data)]
		raise
"""

def RaiseErrorFunc():
	raise NameError('하하하')

#  NameError is Catched : data[하하하]
try:
	RaiseErrorFunc()
except NameError as n:
	print('NameError is Catched : data[{}]'.format(n))

"""
### 사용자 정의 예외
- Exception 클래스나 그 하위 클래스를 상속받아서 구현
- 생성자에 클래스 멤버변수를 이용하여 인자를 에러 처리부로 전달

"""

# ex) 1
class NegativeDivisionError(Exception):  # 사용자 정의 예외 정의
	def __init__(self, value):
		self.value = value

def PositiveDivide(a, b):
	if (b < 0):
		raise NegativeDivisionError(b)
	return a / b

"""
Error - Second argument of PositiveDivide is  -3
Error -  ('division by zero',)
Error -  division by zero
error error:  ("'<' not supported between instances of 'str' and 'int'",)
"""
try:
	ret = PositiveDivide(10, -3)  # 0, 'a'
except NegativeDivisionError as e:  # 사용자 정의 예외인 경우
	print('Error - Second argument of PositiveDivide is ', e.value)
except ZeroDivisionError as e:
	print('Error - ', e.args)
	print('Error - ', e.args[0])
except Exception as ex:  # 그 외 모든 예외
	print('error error: ', ex.args)

"""
### assert 구문
- 표현식 : Assert <조건식>,<관련데이터>
  인자로 받은 조건식이 거짓인 경우, AssertionError가 발생
- 개발과정에서 디버깅, 제약 사항 설정 등으로 사용됨.
- __debug__가 True인 경우만 assert 구문 활성화됨.
	> 명령프롬프트에서 최적화옵션(-O)을 설정화면 __debug__는 False로 설정됨
	> 다음 코드와 동일
		if __debut__:
			if not <조건식>:
				raise AssertionError(<관련데이터>)
"""

# ex) 1
def foo(x):  # 받은 인자가 정수형인지 검사
	assert type(x) == int, "input value must be integer"
	return x * 10

ret = foo('a')
# AssertionError: input value must be integer
print(ret)
