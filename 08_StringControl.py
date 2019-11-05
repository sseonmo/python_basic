print(dir(str))
"""
str - 문자열을 다루는 기본 클래스(내장클래스)
> dir(str) - 모듈에 어떤 함수 혹은 데이터가 들어있는지 확인 할 수 있다.

1. capitalize() - 첫문자를 대문자를 변경한다.
1. count(keyword, [start, [end] ]) - keyword count 반환
1. encode([encoding, [errors]]) -
1. endswith(postfix, [start, [end]]
	print("python is powerful".endswith('ful, 5, -1'))  # False
1. expandtabs([tabsize]) - tab를 공백으로 치환 :  디폴트 공백은 8자리
	aa = "python\tis\tpowerful"
	print(aa.expandtabs(10))    #python    is        powerful
1. find(keyword, [start, [end]]) - keyword의 위치를 index로 반환, 못 찾을 경우 -1를반환
1. index(keyword, [start, [end]]) - 기능은 find와 동일, 단 못찾을시 ValueError 발생
1. isalumn() - 알파벳과 숫자로 이루어 졌는지 검사, return boolean
1. isalpha - 알파벳으로 이루어 졌는지 검사, return boolean
1. islower() - 소문자로 이루어 졌는지 검사, return boolean (알파벳만 검사대상)
1. isupper() - 대문자로 이루어졌는지 검사, return boolean  (알파벳만 검사대상)
1. isspace() - 공백문자 이루어 졌는지 검사, ' ','\t', '\n' True, return boolean
1. isTitle() - 모든 문자가 대문자에 이어 소문자로 시작해야 True 반환
	print('python is powerful'.istitle())       # False
	print('Python Is Powerful'.istitle())       # True
1. isdecimal(), isdigit() - 10진수 이루어졌는지 검사, return boolean ( 유니코드도 포함됨)
1. isnumeric() - 숫자여부 체크
1. join(sequence)
	print(".".join("HOT"))      # H.O.T
	print("\t".join(['python','is', 'powerful']))       # python	is	powerful
1. lower() - 모든 영문자를 소문자로 변환
1. lstrip([chars]) - 왼쪽 공백제거 , 왼쪽 특정 char 제거
1. rstrip([chars]) - 오른쪽 공백제거 , 오른쪽 특정 char 제거
	print(">>> python is powerful >>>".rstrip("<> "))       #>>> python is powerful
1. maketrans(x, [y, [z]])
	transmap = str.maketrans({'p': 'P'})
	print('python is powerful'.translate(transmap))     # Python is Powerful
	transmap = str.maketrans('poieu', 'PO129')
	print('python is powerful'.translate(transmap))     # PythOn 1s POw2rf9l
	transmap = str.maketrans('p', 'P', '!')
	print('python is powerful!!!!!!!!!!!'.translate(transmap))     # Python is Powerful
1. partition(separator) - separator기준으로 문자를 자름 - 튜플형태로 반환
	print("python is powerful".partition('is'))     #('python ', 'is', ' powerful')
1. repace(old, new, [count]) - old, new 로 변환, count가 있을경우 횟수만큼만 변환
1. rfind(keyword, [start, [end]]) - keyword를 뒤에서부터 검색 후 index 반환, 값이 없으면 -1
1. rindex(keyword, [start, [end]]) - rfind와 동일한, 값이 없으면 Value Error 를 발생
1. rpartition(separator) - 오른쪽에서 부터 검사 후 separator로 문자를 자른다. - return  튜플
1. rsplit([separator, [maxsplit]) - 디폴트 공백으로 문자를 자르다.
	print("python is powerful".rsplit())  # ['python', 'is', 'powerful']
	print("python is powerful".rsplit(' ', 1))  # ['python is', 'powerful']
1. split([separator, [maxsplit]] - 디폴트 공백
1. splitlines([keep]) - 여러라인으로 된 문자를 자르다. , keep이 true 일경우 구분자를 제거하지 않음
1. startsWith(prefix,[start, [end]]) - endswith 반대, 앞에서부터 검색, return boolean
	print("python is powerful".startswith(('p', 'm')))  # True
1. strip([chars]) - 문자를 양쪽을 공백문자를 잘라낸다.
1. swapcase() - 영문자에 대해서 대소문자를 반대로 변경한다.
1. title() - 첫번째 시작하는 문자를 대문자로 그뒤는 소문자로 변경
1. upper() - 영문자를 대문자로 변경
"""
# aa = "python is powerful"
# print("python is powerful".startswith(('p', 'm')))  # True

"""
## 정규 표현식(regular expression)
- 특정한 규칙을 가진 문자열을 표현하는데 사용되는 형식 언어
- 주어진 패턴으로 문자열을 검색/치환하는데 사용
- vi, grep 등 프로그램에서 널리 사용

"""

import re

# match - string 시작부분부터 patten 검사
print(re.match('[0-9]*th', '35th'))  # <re.Match object; span=(0, 4), match='35th'>
print(bool(re.match('[0-9]*th', '35th')))  # True

match = re.match('[0-9]*th', '35th')
print(match.string)  # 35th

# search - string 전체에 대해 patten 검사
print(re.search('[0-9]*th', '35th'))  # <re.Match object; span=(0, 4), match='35th'>
print(bool(re.search('[0-9]*th', '35th')))  # True

# 비교
print(bool(re.search('ap', 'This is an apple')))  # True
print(bool(re.match('ap', 'This is an apple')))  # False

# findall
print(re.findall("app\w*", "application orange apple banana"))  # ['application', 'apple']
print(re.findall("king\w*", "application orange apple banana"))  # []

# sub
print(re.sub('-', '', '901225-1234567'))  # 9012251234567
print(re.sub('[:,|\s]', ",", "Apple:Orange Banana|Tomato"))  # Apple,Orange,Banana,Tomato
