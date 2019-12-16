# Chapter02-1
# 파이썬 심화
# 데이터모델(Data Model)
# - Namedtuple
# - Namedtuple attrs
# - Namedtuple method
# - List Comprehension
# 참조 - https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵식 프레임워크 - 시퀀스(Sequence), 반복(Interator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id(주소값), type(데이터자료형 반환) -> value
a = 7
print(id(a), type(a), dir(a))
# 파이썬 -> 일관성

# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.4, 1.5)

# sqrt - 제곱, pow - 루트(제곱근)
from math import sqrt, pow

line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
line_leng2 = sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2))

print('EX-1 - ', line_leng1)
print('EX-1 - ', line_leng2)

# 네임드 튜플 선언 사용

from collections import namedtuple

# 네임트 튜플 선언
Point = namedtuple('Point', 'x y')
# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.4, 1.5)
#  계산
line_leng3 = sqrt(pow(pt2.x - pt1.x, 2) + pow(pt2.y - pt1.y, 2))
# 출력
print('EX-1-2 - ', line_leng3)
print('EX-1-3 - ', line_leng1 == line_leng3)

print()
# 네임드 튜플 선언 방법 - 리스트, 콤마, 빈칸
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# rename = True => 중복되는 키나 예약어가 있을때 속성값을 rename을 해준다.
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default=False

# 출력
print('EX-2-1 - ', Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 640)
p5 = Point3(**temp_dict)

print('EX2-2 -', p1, p2, p3, p4, p5)

print()

# 사용
print('EX-3-1 - ', p1[0] + p2[1])
print('EX-3-2 - ', p1.x + p2.y)  # 클래스 변수 접근 방식 - 권장

# Unpacking
x, y = p3
print('EXΩ-3-3 - ', x + y)

# Rename 테스트
print('EX3-4 -', p4)

print()
print()

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체를 생성한다.
p4 = Point1._make(temp)
print('Ex4-1 -', p4)

# _fields : 필드 네임 확인
print('Ex4-2 -', p1._fields, p2._fields, p3._fields, p4._fields)

# _asdict() : OrderedDict 반환
print('Ex4-3 -', p1._asdict(), p4._asdict())
print(dict(p1._asdict()))  # dict로 반환

# _replace() : 수정된 '새로운' 객체를 반환한다.
print('Ex4-4 -', p2._replace(y=100))

print()
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트선언 - 리스트내장
numbers = [str(n) for n in range(1, 21)]
print(numbers)
ranks = 'A B C D'.split()
print(ranks, numbers)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print('Ex5-1 -', len(students))
print('Ex5-2 -', students)

# 가독성 X
student2 = [Classes(rank, number) for rank in 'A B C D'.split() for number in [str(n) for n in range(1, 21)]]
print('Ex6-1 -', len(student2))
print('Ex6-2 -', student2)
print()
print()

# 출력
for student in students:
    print('EX-7-1 -', student)
