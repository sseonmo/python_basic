# Chapter_01
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, static method

#  basic instant method

class Student(object):
	"""
	student Class
	Author : Gu
	Date : 2019-12-14
	Description : Class, Static, Instance Method
	"""

	# class variable
	tuition_Persent = 1.0

	def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
		self._id = id
		self._first_name = first_name
		self._last_name = last_name
		self._email = email
		self._grade = grade
		self._tuition = tuition
		self._gpa = gpa

	# Instance Method
	def full_name(self):
		return "{} {}".format(self._first_name, self._last_name)

	# Instance Method
	def detail_info(self):
		return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email,
		                                                             self._grade, self._tuition, self._gpa)

	# Instance Method
	def get_fee(self):
		return 'Before Tuition -> id : {}, fee : {}'.format(self._id, self._tuition)

	# Instance Method
	def get_fee_cule(self):
		return 'After Tuition -> id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_Persent)

	# Instance Method
	def __str__(self):
		return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)

	# Class Method
	@classmethod
	def raise_fee(cls, per):
		if per <= 1:
			print('please Enter i or More ')
			return

		cls.tuition_Persent = per
		print('Succed! tuition increased!')

	# 인스턴스 생성시 권장하는 방
	@classmethod
	def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
		return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_Persent, gpa)

	# Static Method
	@staticmethod
	def is_scholarship_st(inst):
		if inst._gpa >= 4.3:
			return '{} is a scholarship recipient.'.format(inst._last_name)
		return 'Sorry. Not a scholarship recipient'

# 학생인스턴스
student1 = Student(1, 'gu', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student2 = Student(2, 'Lee', 'Myungho', 'student2@daum.com', '2', 500, 4.2)

print(student1)
print(student2)

print()
print()
# 전체정보
print(student1.detail_info())
print(student2.detail_info())

print()
print()

# 학비정보(인상전)
print(student1.get_fee())
print(student2.get_fee())

print()

# 학비인상(클래스 메소드 미사용)
# Student.tuition_Persent = 1.3
# 학비인상(클래스 메소드 사용)
Student.raise_fee(1.3)

# 학비인상 (클래스 메소드 미사용)
print(student1.get_fee_cule())
print(student2.get_fee_cule())

# 클래스 메소드 인스턴스 생성실
# instance method create by class method
student3 = Student.student_const(3, 'park', 'minji', 'Student3@gmai.com', '3', 550, 4.5)
student4 = Student.student_const(3, 'Cho', 'sunghan', 'Student4@gmai.com', '4', 600, 4.5)

# 전체정보
print(student3.detail_info())
print(student4.detail_info())
print()

# 학생학비 변경확인
print(student3._tuition)
print(student4._tuition)
print()

# 장학금 혜택 여부(static 메소드 미사용)
def is_scholarship(inst):
	if inst._gpa >= 4.3:
		return '{} is a scholarship recipient.'.format(inst._last_name)
	return 'Sorry. Not a scholarship recipient'

print(is_scholarship(student1))
print(is_scholarship(student2))
print(is_scholarship(student3))
print(is_scholarship(student4))

print()
# 장학금 혜택여부(static 메스드 사용)
print(Student.is_scholarship_st(student1))
print(Student.is_scholarship_st(student2))
print(Student.is_scholarship_st(student3))
print(Student.is_scholarship_st(student4))

print()

print(student1.is_scholarship_st(student1))
print(student2.is_scholarship_st(student2))
print(student3.is_scholarship_st(student3))
print(student4.is_scholarship_st(student4))