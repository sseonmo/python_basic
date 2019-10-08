# 자료형
### 수치
- int, float, complex, 연산자(+, -, *, /, //, %, **, =) 
###  +, * 연산자
```python
print('py''thon')   # python - 중간에 + 생략되어 있다.
print('py' * 3)     # pypypy
```
### 문자 인덱싱 & 슬라이싱
```python
""" 줄바꿈
적용됨
"""
tempStr = 'python'
print(tempStr[0])  # p
print(tempStr[5])  # n
print(tempStr[1:4])  # yth
print(tempStr[-2:])  # on
```
#### - 유니코드
- 모든문자열(string)이 기본적으로 유니코드이다.
- 유니코드 이외의 인코딩이 있는 문자열은 bytes로 표현된다.

### 리스트
- append, insert, extend, index, count, pop, remove, sort
```python
colors = ['red', 'green', 'gold']
print(colors)  # ['red', 'green', 'gold']

colors.append("blue")
print(colors)  # ['red', 'green', 'gold', 'blue']

colors.insert(1, 'black')
print(colors)  # ['red', 'black', 'green', 'gold', 'blue']

colors.extend(['white', 'gray'])
print(colors)  # ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray']

print(colors.index("black"))  # 1
# 검색범위 안에 값이 없으면 error
# print(colors.index("black", 3, 4))  # ValueError: 'black' is not in list

colors.append('red')
print(colors.count('red'))  # 2

print(colors)           # ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray', 'red']
print(colors.pop())     # red
print(colors)           # ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray']
```

### 세트 
- 집합과 동일
- 순서가 없음
- 제공되는 메서드는 리슽와 유사하면, 추가적으로 교집합과 합집합 메서드 제공
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))           # 합집합 - {1, 2, 3, 4, 5}
print(a.intersection(b))    # 교집합 - {3}
```
### 튜플
- 튜플은 리스트와 유사하나, 읽기전용
- 속도는 빠름, 제공메서드 count, index 정도임
```python
c, d = 1, 2
print(c, d)  # 1 2
c, d = d, c
print(c, d)  # 2 2
```

### 딕셔너리(객체랑 비슷함)
- items(), keys(), values(), del, clear()
```python
color = dict(apple='red', banana='yello')
# color = {'apple': 'red', 'banana': 'yello'}
print(color["apple"])  # red
color["apple"] = 'green'
print(color["apple"])  # green
print(color.keys())  # dict_keys(['apple', 'banana'])
print(color.values())  # dict_values(['green', 'yello'])

for k, v in color.items():
	print(k, v)  # apple green, banana yello
color.__delitem__('apple')
color.clear()
```
### 부울(bool)
- 참, 거짓

### 얕은복사 vs 깊은복사
- 얕은복사 - 주소가 복사되어 객체를 공유하는 경우 ( 일반적인 a = b)
- 깊은복사 - 객채를 복사하는 (b = a[:])

# 함수
- 함수의 선언은 def로 시작하고 콜론(:)로 끝남
- 함수의 시작과 끝은 코드의 들여쓰기로 구분
- 시작과 끝을 명시해 줄 필요가 없음
```python
"""
def <함수명>(인수1, 인수2, ...인수n):
    <구문>
    return <반환값>
"""

def multiply(a, b):
	return a * b

print(multiply(10, 20))  # 200
```

### 인수모드
- 기본인수 : 인수값이 없을때 default 값을 적용
```python
def sum1(a=10, b=20):
    return a * b

print(sum1())  # 100
print(sum1(20))  # 200
```
- 키워드인수
    * 인수의 이름으로 값을 전달하는 방식
    * 인수에 순서에 상관없이 변수의 이름으로 특정인수를 전달 할 수 있다.(가동성 짱)
```python
def connectURL(server, port):
    # strUrl = "http://" + server + ":" + port
    strUrl = "http://{}:{}".format(server, port)
    return strUrl

print(connectURL("test.com", "8080"))   # http://test.com:8080
print(connectURL(port="8080", server="test.com"))   # http://test.com:8080
```
- 가변인수 리스트 
    * 인수의 개수가 정해지지 않는 가변 인수를 전달
    * `*`를 사용하며 인수는 튜플형식으로 전달됨 ( a, b, c) => 이딴식
```python
def union2(*ar):
    res = []
    for item in ar:
        for x in item:
            if not x in res:
                res.append(x)
    return res

print(union2("HAM", "EGG", "SPAM")) # ['H', 'A', 'M', 'E', 'G', 'S', 'P']  
```
- 정의되지 않은 인수처리 
    - `**`사용하여 정의되지 않는 인수를 딕셔너리 형식으로 전달.
    - 정의되지 않은 인수는 가장 마지막 인수여야 한다. 
```python
def userURLBuilder(server, port, **user):
    strUrl = "http://{}:{}/?".format(server, port)
    for key in user.keys():
        strUrl += "{}={}&".format(key, user[key])
    return strUrl

# http://test.com:8080/?id=userid&passwd=1234&
print(userURLBuilder('test.com', '8080', id='userid', passwd='1234'))   
# http://test.com:8080/?id=userid&passwd=1234&name=mike&
print(userURLBuilder('test.com', '8080', id='userid', passwd='1234', name='mike')) 
``` 

### 함수종류
- 람다함수
```python
""" lambda 인수: <구문> """
g = lambda x, y: x * y
print(g(2, 2))  # 4
print((lambda x: x * x)(3))  # 9
```
- 재귀적(recursive)함수호출 : 함수내부에서 자기자신을 호출하는 함수

- pass 구문 :pass 문은 아무것도 하지 않습니다. 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 사용할 수 있다.
```python
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...

"""최소한의 클래스를 만들 때 흔히 사용됩니다."""
class MyEmptyClass:
    pass
...

"""
pass가 사용될 수 있는 다른 장소는 새 코드를 작업할 때 
함수나 조건부 바디의 자리를 채우는 것인데, 
여러분이 더 추상적인 수준에서 생각할 수 있게 합니다. 
pass 는 조용히 무시됩니다:
"""
def initlog(*args):
    pass   # Remember to implement this!
```
- __doc__속성과 help함수
    - help 함수를 이용해 함수의 설명을 볼 수 있음(사용자 정의 함수 )
```python
help(print)

def plus(a, b):
	return a + b

"""
Help on function plus in module __main__:
plus(a, b)
"""
help(plus)
```

### 이터레이터(interator)
- 내부반복문을 관리해 주는 개체로 순회 가능한 객체의 요소를 순서대로 접근할 수 있다.
- 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
- next(it) 또는 it.__next__() 로 하나 하나씩 접근가능하다. 
```python
s = 'abc'
print(type(s))  # 'str'
it = iter(s)  # <class 'str'> => iterable => <class 'str_iterator'> 변환
print(type(it))  # <class 'str_iterator'>
print(next(it))  # a
print(it.__next__())  # b
print(next(it))  # c
# print(next(it))     # 예외발생 StopIteration

# class 로 구현한 예제
class MyCollection:
	def __init__(self, count):
		self.size = count
		self.data = list(range(self.size))
	
	def __iter__(self):
		self.index = 0
		return self
	
	def __next__(self):
		if self.index >= self.size:
			raise StopIteration
		
		n = self.data[self.index]
		self.index += 1
		return n

coll = MyCollection(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(coll))
# for x in coll:
# 	print(x)
```

### 제너레이터(Generator)
- return 대신 yield라는 구문을 이용해 함수 객체를 유지한 체 값을 호출자에게 넘겨줌
- 값을 넘겨준 후 함수 객체는 그대로 유지됨
- 함수의 상태를 유지하고 다시 호출할 수 있기 때문에 순회 가능한 객체를 만들 때 매우 편리
```python
def square_number(nums):
	for i in nums:
		yield i

numbers = square_number([1, 2, 3, 4, 5])

print(type(numbers))    # <class 'generator'>
# print(sum(numbers))     # 15
print(next(numbers))       # 1
print(next(numbers))       # 2
print(next(numbers))       # 3
print(next(numbers))       # 4
print(next(numbers))       # 5
print(next(numbers))       # 예외발생 - print(next(numbers))       # 예외발생
```

# 제어문
### if 문  
```python
# if 문
"""
if <조건식>:
	<구문>
"""
value = 10
if value > 5:
	print('value is bigger than 5')     # value is bigger than 5

"""
if <조건식 1>:
	<구문 1>
elif <조건식 2>:
	<구문 2>
else:
	<구문 3>
"""

score = int(input('Input Score: '))     # 사용자로부터 정수값을 입력받음
if 90 <= score <= 100:
		grade = 'A'
elif 80 <= score < 90:
		grade = 'B'
elif 70 <= score < 80:
		grade = 'C'
elif 60 <= score < 70:
		grade = 'D'
else:
		grade = 'F'

# input 80 / Grade is B
print('Grade is {}'.format(grade))
```
> 파이썬 조건식 표현방법 <br>
    - **70<= score < 80** 간단명료함. <br>
    - 70<= score and score < 80

- 단축평가 - 조건식 전체를 판단하지 않고 순척적으로 진행한다. 좌 => 우
    - `and` 와 `or`는 단축평가로 수행되도록 보장
    - x and y : x가 false 인 경우, y 값은 평가하지 않음
    - x or y : x가 True 인 경우, y 값은 평가하지 않음

### 조건식의 참/거짓 판단
- false : 0, 0.0, (), [], {}, '(빈문자열)', None인 경우
- true : false인 경우를 제외한 값

### for문
```python
"""
시퀀스형 객체를 순차적으로 순회
for <아이템 I> in <시퀀스형 객체 S>:
	<구문>
"""
l = ['Apple', 100, 15, 23]
# Apple | 100 | 15 | 23 
for i in l:
	print(i)
	
d = {"apple": 100, "orange": 200, "Banana": 300}
# apple / 100 | orange / 200 | Banana / 300
for k, v in d.items():
	print('{} / {}'.format(k, v))
```
- break - 반목문 내부 클록을 벗어남
```python
# item: 1 | item: 2 | item: 3 | item: 4 | item: 5 
for i in range(1, 10):
	if i > 5:
		break
	print('item: {}'.format(i))
```
- continue : 내부 블록을 수행하지 않고 다음차례를 순회.
```python
# item: 1 | item: 3 | item: 5 | item: 6 | item: 7 
for i in range(1, 10):
	if i % 2 == 0:
		continue
	print('item: {}'.format(i))
```
- else : 반복문 수행도중 break로 인하여 중간에 종료되지 않고 끝까지 수행되었을때, else 블록을 수행
```python
# item: 1 | item: 3 | item: 5 | item: 6 | item: 7 | Exit without break!    
for i in range(1, 10):
	if i % 2 == 0:
		continue
	print('item: {}'.format(i))
else:
	print('Exit without break!')    # 외부루프문장
```
- 리스트 내장
```python
"""
기존 시퀀스 객체를 이용하며 추가적인 연산을 통하여 새로운 리스트 객체 생성
if문을 옵션으로 filter 처럼 사용가능함.
[<표현식> for <아이템> in <시퀀스 객체> (if <조건식>)]
"""
q = [1, 2, 3, 4, 5]
q2 = [i ** 2 for i in q]
print(q2)  # [1, 4, 9, 16, 25]

t = ("orange", "apple", "banana", "kiwi")
t2 = [len(i) for i in t]
print(t2)  # [6, 5, 6]

# if문을 통한 필터링
t3 = [i for i in t if len(i) > 5]
print(t3)  # ['orange', 'banana']

# 원본리스트 2개
L_1 = [3, 4, 5]
L_2 = [1.5, -0.5, 4]
L_3 = [x * y for x in L_1 for y in L_2]
print(L_3)  # [4.5, -1.5, 12, 6.0, -2.0, 16, 7.5, -2.5, 20]
```

### 유용한 함수
- filter
    - 함수의 결과값이 참인 시퀀스 객체의 이터레이터를 반환
    - None이 오는 경우 필터링 하지 않음
```python
"""
filter(<function>|None, 시퀀스 객체)
"""
LL = [10, 25, 30]
IterL = filter(None, LL)
# item : 10 / item : 20 / item : 30
for i in IterL:
	print('item : {}'.format(i))

def GetBiggerThan20(i):
	return i > 20

print(list(filter(GetBiggerThan20, LL)))  # [25, 30]

print(list(filter(lambda i: i > 20, LL)))    # [25, 30]
```
- range : 수열을 순회하는 이터레이터 객체를 반환    
```python
"""
range([시작값],종료값[,증가값]
- 시작값과 종료값은 생략가능하면, 이때는 각각 0 과 1이 할당된다.
"""
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10, 20, 2)))  # [10, 12, 14, 16, 18]
```
- map
```python
"""
map(<function>, 시퀀스 객체, ...)
- 시퀀스 객체를 순회하며 function구문의 연산을 수행
- 함수의 인자 수만큼 시퀀스 객체를 전달
"""
M = [1, 2, 3]

def add10(i):
	return i + 10

print(list(map(add10, M)))  # [11, 12, 13]

# item : 11 / item : 12 / item : 13
for i in map(add10, M):
	print('item : {}'.format(i))

X = [1, 2, 3]
Y = [2, 3, 4]
# pow 지수 계산 | 1 ** 2, 2 ** 3, 3 ** 4
print(list(map(pow, X, Y)))  # [1, 8, 81]
```

# class
- 데이터와 데이터를 변형하는 함수를 같은 공간으로 작성
    > 메서드(Method)  
    인스턴스(Instance)  
    정보은닉(Information Hiding)  
    추상화(Abstraction)  
    다형성(Ploymorphism)
```python
class Person:   # 클래스 정의 
	Name = 'Default Name'   # 멤버변수
	
	def print(self):    # 멤버 메소드 
		print('My Name is {}'.format(self.Name))

p1 = Person()   # 인스턴스 객체 생성
p1.print()      # 인스턴스 메소드 호출
```
### 클래스와 인스턴스 관계
```python
"""
isinstance(인스턴스객체, 클래스객체)
"""

class Person:
	pass

class Bird:
	pass

class Student(Person):
	pass

p, s = Person(), Student()
print("p is instance of Person", isinstance(p, Person))  # p is instance of Person True
print("s is instance of Person", isinstance(s, Person))  # s is instance of Person True
print("p is instance of object", isinstance(p, object))  # p is instance of object True
print("p is instance of Bird", isinstance(p, Bird))  # p is instance of Bird False
```
### 생성자와 소멸자
```python
"""
생성자
	- 생성 시 초기화 작업수행
	- 인스턴스 객체가 생성될때 자동으로 호출
	- __init()__
소멸자
	- 소멸 시 죵료작업을 수행
	- 인스턴스 객체의 참조카운터가 '0'이 될때 호출
	-__del()__
"""
class MyClass:
	def __init__(self, value):  # 생성자 메소드
		self.Value = value
		print('Class is create! Value={}'.format(value))
		
	def __del__(self):          # 소멸자 메서드
		print('Class is deleted!!')

def foo():
	d = MyClass(10)

foo()
# Class is create! Value=10
# Class is deleted!!
```
### 메서드 확장
- 정적(static) 메소드
    > 인스턴스 객체를 통하지 않고, 크래스를 통해 호출 할 수 있는 메소드  
    인스턴스 객체를 참조하는 self 인자가 필요하지 않음
- 클래스(class) 메소드
    > 클래스 영역의 데이터에 직접 접글 할 수 있는 메서드   
    암시적으로 첫 인자로 클래스 객체가 전달되어 진다. 

### 연산자 중복
```python
"""
사용자 정의 객체에서 필요한 연산자를 내장 타입의 형태와 동장이 유사하도록 재정의
연산자 중복을 위하여 두 개의 밑줄 문자가 앞뒤로 있는 메소드를 미리 정의함.
"""
class GString:
	def __init__(self, init=None):
		self.content = init
	
	def __sub__(self, str):  # '-' 연산자 중복 정의
		for i in str:
			self.content = self.content.replace(i, '')
	
	def Remove(self, str):
		self.__sub__(str)
		return self.content
		
gstr = GString('abcdefg')
print(gstr.Remove('bef'))       #acdg
```
### 수치연산자 
- 특정연사자에 대해서 이미 지정되어 있는 메소드로 특정 연산자가 사용되면 자동으로 호출되어진다.
![](./image/수치연산자.png)

### 상속
- 부모 클래스의 모든 속성(변수, 메소드)를 자식 클래스로 물려줌
- 클래스의 공통된 속성을 부모클래스에 정의
- 하위 클래스에서는 특화된 메소드와 데이터를 정의
- 각 개별 클래스에 특화된 기능을 공통된 인터페이스로 접근가능
```python
class Person:
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber

class Student(Person):
	def __init_(self, name, phoneNumber, subject, studentID):
		self.Name = name
		self.PhoneNumber = phoneNumber
		self.Subject = subject
		self.StudentID = studentID

#  상속 관계인 두 클래스 간의 관계를 확인
print(issubclass(Student, Person))  # Ture
```
### 다중상속 
- 2개 이상의 클래스를 상속받는 경우
- 두 클래스의 모든 속성(변수와 메서드)을 전달받음

# 모듈
- 코드의 재사용성
- 코드를 이름공간으로 구분하고 관리 할 수 있음
- 복잡하고 어려운 기능을 포함하는 프로그램을 간단하게 만들 수 있음
> 현재 파이썬 3.0 번전에는 대략 200개가 넘는 모듈을 지원
> 1. 문자열(String), 날짜(date), 시간(time), 십진법(decimal), 랜덤(random)  
> 1. 파일(file), os, sqllite3, sys, xml , email, http 등등

```python
import math

print(math.pow(2, 10))
# dir() - 모듈에 어떤 함수 혹은 데이터가 들어있는지 확인 할 수 있다.
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',...]
print(dir(math))
```
#### 모듈만들기
- 사용자가 직접 모듈을 만들 수 있음
- 모듈은 일반적으로 <모듈이름>.py으로 지정
- 모듈의 경로 : sys.path에 저장되어 있는 디렉토리를 검색
- 모듈의 경로 밖의 모듈은 임포트 할 수 없음
- 모듈 경로 탐색순위
    > 프로그램이 실행된 디렉터리  
    python 환경 변수에 등록된 위치  
    표준 라이브러리 디렉토리
####임포트 방법
 > import <모듈>  
 from <모듈> import <어트리뷰트>  
 from <모듈> import \*  
 import <모듈> as <별칭>
```python
from lib.simpleset import union

a = {1, 2, 3}
b = {3, 4, 5}
print(union(a, b))  # {1, 2, 3, 4, 5}
print(__name__)  # __main__
```
#### 유용한 팀
 - 모듈의 직접 실행과 임포트 되어 실행되었는지 구분하는 방법
 	> import 되었을때 __name__은 모듈 자신의 이름  
 	모듈이 직접 실행 되었을때는 __name__은 '\__main\__'

#### 모듈 팩키지 - __init__.py를 이용해서 모듈팩키지를 만든다.
