# Chapter_01
# 파이썬 심화
# 객체 지행 프로그래밍 -> 코드의 재사용, 코드 중복방지 등..
# 클래스 상세 설명
# 클래스변수, 인스턴스변수

# 모든 클래스는 object를 상속받는다.
# 클래스 재 선언
class Student():
	"""
	Student Class
	Author : 홍길동
	Date : 2019-12-01
	"""
	#  클래스 변수 - Student object 전체가 사용하는 공용변수이다.
	student_count = 0

	def __init__(self, name, number, grade, details, email=None):
		# 인스턴스 변수 종속 된 변수
		self._name = name
		self._number = number
		self._grade = grade
		self._details = details
		self._email = email

		# 클래스변수 접근은 class name 으로 접근한다.
		Student.student_count += 1

	# self.student_count += 1

	def __str__(self):
		return 'str {}'.format(self._name)

	def __repr__(self):
		return 'repr {}'.format(self._name)

	def detail_info(self):
		print('Current Id : {}'.format(id(self)))
		print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

	def __del__(self):
		Student.student_count -= 1

# Self 의미
student1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
student2 = Student('Chang', 4, 1, {'gender': 'FeMale', 'score1': 85, 'score2': 74}, 'email@email.com')

# ID 확인
print(id(student1))
print(id(student2))

# value를 비교 'a == b'
print(student1._name == student2._name)
# object를 비교 'a is b'
print(student1 is student2)

# 동일한 객체를 바로본다.
a = 'ABC'
b = a
print('{} == {}'.format(id(a), id(b)))
print(a is b)
print(a == b)

# dir & __dict__ 확인 : dir 더 상세 / __dict__ 실무에서 더 자주 사용함
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_details', '_email', '_grade', '_name', '_number', 'detail_info', 'student_count']
print(dir(student1))
print(dir(student2))
print()
print()
# {'_name': 'Cho', '_number': 2, '_grade': 3, '_details': {'gender': 'Male', 'score1': 65, 'score2': 44}, '_email': None}
print(student1.__dict__)
# {'_name': 'Chang', '_number': 4, '_grade': 1, '_details': {'gender': 'FeMale', 'score1': 85, 'score2': 74}, '_email': 'email@email.com'}
print(student2.__dict__)

# Doctring - class 주석확인
print(Student.__doc__)
print()

# 실행
student1.detail_info()
student2.detail_info()
print()

# 에러
# Student.detail_info() - 에러발생 - 인스턴스가 없으니까
Student.detail_info(student1)

# 비교 - __class__ 원형 클래스를 보여준다.
# <class '__main__.Student'> <class '__main__.Student'>
print(student1.__class__, student2.__class__)
print(id(student1.__class__) == id(student2.__class__))
print()

# 인스턴스 변수
# 직접접근(PEP 문법적으로 권장 X)
print(student1._name, student1._email)
print(student2._name, student2._email)

print()
print()

# 클래스 변수 - 모든 인스턴스가 공유하는 변수
print(student1.student_count)   # 2
print(student2.student_count)   # 2
print(Student.student_count)   # 2

print()
print()

# 공유확인
print(Student.__dict__)
# 인스턴스 변수만 나온다.
# {'_name': 'Cho', '_number': 2, '_grade': 3, '_details': {'gender': 'Male', 'score1': 65, 'score2': 44}, '_email': None}
print(student1.__dict__)
# {'_name': 'Chang', '_number': 4, '_grade': 1, '_details': {'gender': 'FeMale', 'score1': 85, 'score2': 74}, '_email': 'email@email.com'}
print(student2.__dict__)

"""
- 중요 -
인스턴스 네임스페이스에 없으면 상위에서 검색
즉, 동일한 이름으로 변수 생성 가능(인스턴스 겸색 후 -> 상위(클래스, 변수, 부모 클래스 변수)
"""
del student2

print(student1.student_count)   # 1
print(Student.student_count)    # 1
