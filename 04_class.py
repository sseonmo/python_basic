class Person:  # 클래스 정의
	name = 'Default Name'  # 멤버변수
	
	def print(self):  # 멤버 메소드
		print('My Name is {}'.format(self.name))

p1 = Person()  # 인스턴스 객체 생성
p1.print()  # 인스턴스 메소드 호출

# 클래스와 인스턴스 관계
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
print("p is instance of Persion", isinstance(p, Person))  # p is instance of Persion True
print("s is instance of Persion", isinstance(s, Person))  # s is instance of Persion True
print("p is instance of object", isinstance(p, object))  # p is instance of object True
print("p is instance of Bird", isinstance(p, Bird))  # p is instance of Bird False

# 생성자와 소멸자
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
	
	def __del__(self):  # 소멸자 메서드
		print('Class is deleted!!')

def foo():
	d = MyClass(10)

foo()
# Class is create! Value=10
# Class is deleted!!


# 연산자 중복
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
print(gstr.Remove('bef'))  # acdg

# 상속
"""
부모 클래스의 모든 속성(데이터, 메소드)를 자식 믈래스로 물려줌
클래스의 공통된 속성을 부모클래스에 정의
하위 클래스에서는 특화된 메소드와 데이터를 정의
각 개별 클래스에 특화된 기능을 공통된 인터페이스로 접근가능
"""

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

# 다중상속
"""
2개 이상의 클래스를 상속받는 경우
두 클래스의 모든 속성(변수와 메서드)을 전달받음
"""
