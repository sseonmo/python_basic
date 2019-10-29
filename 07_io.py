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

## 파일입출력
## open
## write, close
## read
## readline, readlines, tell, seek
## 	> With ~ as

## pickle
## 주의 - list, dict 는 반드시 바이너리 타입으로 파일에 저장해야 한다.
## pickle - 사용자 정의 클래스 

