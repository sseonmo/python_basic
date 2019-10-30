import sys

"""
출력 - print()
	> 구분자(sep), 끝(end), 출력(file)
"""
print('welcome to', 'python', sep='||', end='!\n', file=sys.stderr)

# fomatting
print('{} is {}'.format('apple', 'red'))  # apple is red
print('{item} is {color}'.format(item='apple', color='red'))  # apple is red
dic = {'item': 'apple', 'color': 'red'}
print("{0[item]} is {0[color]}".format(dic))  # apple is red
"""
** 기호를 사용하면 dictionary를 입력으로 받은 것으로 판단하고 인자를 하나만 받게됨
불필요한 index를 생략가능
"""
print("{item} is {color}".format(**dic))

# ! 기호를 사용한 문자열 변환
# !s, !r, !a == str(), repr(), ascii()
print("{item!s} is {color!s}".format(**dic))  # apple is red
print("{item!r} is {color!r}".format(**dic))  # 'apple' is 'red'
print("{item!a} is {color!a}".format(**dic))  # 'apple' is 'red'

# 포매팅(formatting)
"""
- ":" 기호 이용 정력, 폭 , 부호, 공백처리, 소수점, 타입등을 지정
- 정렬기준과 부호표현번
	> **">"** : 오른쪽기준  
	**"<"** : 왼쪽기준  
	**"="** : 가운데기준  
	**"="** : 부호와 상관이 있음
		- **"="**가 사용되면 공백문자들 앞에 부호가 표시됨
			사용되지 않으면 공백문자들 뒤, 즉, 숫자 바로 앞에 부호가 표시됨
		- "+" : 플러스 부호를 나타내라는 뜻
		- "-" : 마이너스 값만 마이너스 부호를 나타내라는 뜻
		- " " : 마이너스 값에는 마이너스 부호를 나타내고 플러스일 때는 공백을 표시하라는 뜻
"""
# ex )
print("{0:$>5}".format(10))  # $$$10
print("{0:$<5}".format(10))  # 10$$$
print("{0:$^5}".format(10))  # $10$$
print("{0:$=5}".format(10))  # $$$10
print("{0:$>-5}".format(-10))  # $$-10
print("{0:$>+5}".format(+10))  # $$+10
print("{0:$> 5}".format(-10))  # $$ 10 / $$+10

"""
- 진수표현법
	> "b"는 이진수, "d"는 십진수, "x"는 16진수를, "o"는 8진수, "c"는 문자열을 출력  
	"#"를 사용하면 #x 16진수, #o는 8진수, #b는 2진수를 표시됨 
"""
print("{0:b}".format(10))  # 1010
print("{0:d}".format(10))  # 10
print("{0:x}".format(10))  # a
print("{0:o}".format(10))  # 12
print("{0:c}".format(65))  # A

print("{0:#x},{0:#o},{0:#b}".format(10))  # 0xa,0o12,0b1010
"""
- 실수표현법
	> "e"는 지수표현, "f"는 일반적인 실수표현, "%"는 퍼센트 표현을 의미  
"""
print("{0:e}".format(4 / 3))  # 1.333333e+00
print("{0:f}".format(4 / 3))  # 1.333333
print("{0:%}".format(4 / 3))  # 133.333333%
# 실수에서는 소수전 몇번째 자리까지 표현할 것인지를 지정가능
print("{0:.3f}".format(4 / 3))  # 1.333

# 입력
"""
- 사용자로부터 입력 input()함수를 이용하여 받을 수 있다. 
"""
# a = input('insert and key:')    # input key : test
# print(a)    # test

## 파일입출력
## open
"""
- 파일 입출력 제어를 보다 세밀하게 하기 위해서는 open()  
함수를 이용 파일을 연 후, 파일전용 함수를 이용해 작업하는것이 일반적
> 기본형:파일객체 = open(file, mode)
- mode 속성 - 속성들을 조합해서 사용가능함.
	- r : 일기모드(디폴트)
	- w : 쓰기모드
	- a : 쓰기 + 이어쓰지모드
	- + : 읽기 + 쓰기모드
	- b : 바이너리모드
	- t : 텍스트모드(디폴트)
"""
## write, close
f = open('test.txt', 'w')
print(f.write('plow deep\nwhile sluggard sleep'))  # writer는 글자수를 반환 (int)
f.close()
## read
# - 텍스트 모드에서는 일반 문자열과 같이 encoding이 적요되기때문에,
# 바이너리 데이터(binary data) 를 다룰 때에는 오류가 발생함
# 바이너리 데이터를 다룰 때에는 만드시 바이너리 모드를 사용해야 한다.
f = open('test.txt')
print(f.read())  # plow deep\nwhile sluggard sleep
f.close()
print(f.closed)  # True : boolean값을 리턴
# 파일입출력 관련 함수들
## readline() 함수 : 호출할 대 마다 한 줄씩 읽은 문자열을 반환함
## readlines() 함수 :  파일의 모든 내용을 줄 단위로 잘라서 리스트를 반환함
## tell() 함수 :  현재 파일에서 어디까지 읽고 썼는지 위치를 반환함
## seek() 함수 :  사용자가 원한느 위치로 포인터를 이동함

## 	> With ~ as 구문 : 문장이 끝날때 자동으로 파일을 close() 한다.
with open('test.txt') as f:
	print(f.readlines())  # ['plow deep\n', 'while sluggard sleep']
	print(f.closed)  # False

print(f.closed)  # True

## pickle
"""
# - 리스트나 클래스를 파일로 저장할 때 사용함.
# - 쓰기 : dump, 읽기 : load
## 주의 - list, dict, class 는 반드시 바이너리 타입으로 파일에 저장해야 한다.
"""
# 쓰기
import pickle

colors = ['red', 'green', 'black']
f = open('colors', 'wb')
pickle.dump(colors, f)
f.close()

# 읽기
del colors
f = open('colors', 'rb')
colors = pickle.load(f)
f.close()
print(colors)

## pickle - 사용자 정의 클래스
class test:
	var = None

a = test()
a.var = 'Test'
f = open('test', 'wb')
pickle.dump(a, f)
f.close()
f = open('test', 'rb')
b = pickle.load(f)
f.close()
print(b.var)  # Test
