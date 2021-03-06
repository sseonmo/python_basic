# Chapter_01
# 파이썬 심화
# 객체 지행 프로그래밍 -> 코드의 재사용, 코드 중복방지 등..
# 클래스 상세 설명
# 클래스변수, 인스턴스변

# 일반적인 코딩
# 학생 1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
	{'gender': 'Male'},
	{'score1': 95},
	{'score2': 88}
]

# 학생 1
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
	{'gender': 'Female'},
	{'score1': 77},
	{'score2': 92}
]

# 학생 3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
	{'gender': 'Male'},
	{'score1': 99},
	{'score2': 100}
]

# 리스트 구조
# 관리하기 불편
# 테이터의 정확한 위치(인덱스) 매핑해서 사용
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
	{'gender': 'Male', 'score1': 95, 'score2': 88},
	{'gender': 'Female', 'score1': 77, 'score2': 92},
	{'gender': 'Male', 'score1': 99, 'score2': 100},
]

# 학생삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()

# 딕셔너리
# 코드 반복 지속, 중첩 문제
students_dicts = [
	{'student_name': 'Kim', 'student_number': 1, 'student_grade': 1,
	 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
	{'student_name': 'Lee', 'student_number': 2, 'student_grade': 2,
	 'student_detail': {'gender': 'Female', 'score1': 77, 'score2': 92}},
	{'student_name': 'Park', 'student_number': 3, 'student_grade': 4,
	 'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 100}},
]
del students_dicts[1]
print(students_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
# 모든 클래스는 object 를 사용받는다.
# class Student():
class Student(object):
	def __init__(self, name, number, grade, details):
		self._name = name
		self._number = number
		self._grade = grade
		self._details = details

	# __str__ : 인스턴스가 문자열로 어떻게 표현될지 결정을 해주는 역할을 한다.
	# __str__, __repr__ : 우선순위가 __str__ 높다
	def __str__(self):
		return 'str : {} - {}'.format(self._name, self._number)

	def __repr__(self):
		return 'repr : {} - {}'.format(self._name, self._number)


student1 = Student('kim', 1, 2, {'gender': 'Male', 'score1': 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1': 77, 'score2': 92})
student3 = Student('park', 3, 4, {'gender': 'Male', 'score1': 99, 'score2': 100})

# 모든 속성값들이 보인다. __dict__
print(student1.__dict__)    # {'_name': 'kim', '_number': 1, '_grade': 2, '_details': {'gender': 'Male', 'score1': 95, 'score2': 88}}
print(student2.__dict__)
print(student3.__dict__)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()
print(students_list)
print()

# 반복(__str__) : 인스턴스가 문자열로 어떻게 표현될지 결정을 해주는 역할을 합니다.
for student in students_list:
	print(student)
	# print(repr(student))