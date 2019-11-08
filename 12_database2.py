import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("select * from PhoneBook order by name")
[print(r) for r in cur]

cur.execute("select * from PhoneBook order by name desc ")
[print(r) for r in cur]

# 사용자 임의 정력방식
def orderFnc(str1, str2):
	s1 = str1.upper()
	s2 = str2.upper()
	# print("=============================")
	# print( str1 , str2)
	# print('s1 > s2', s1 > s2)
	# print('s1 < s2', s1 < s2)
	# print((s1 > s2) - (s1 < s2))
	return (s1 > s2)

con.create_collation('myordering', orderFnc)
cur.execute("select * from PhoneBook order by name COLLATE myordering")
[print(r) for r in cur]

# dump
for i in con.iterdump():
	print(i)

"""
- 내장/집계 함수
| 함수 | 설명 |
|:---|:---|
| abs(x) | 절대값을 반환 |
| length(x) | 문자열길이 반환 |
| lower(x) | 소문자로 변환 |
| upper(x) | 대문자로 변환 |
| min(...) | 최소값을 반환 |
| max(...) | 최대값을 반환 |
| random(*) | 임의의 정수 반환 |
| count(x) | NULL이 아닌 튜플의 개수를 반환 |
| count(*) | 투플의 개수를 반환 |
| sum(x) | 합을 반환 |

- 자료형 
	> SQLite3 자료형과 그에 대응되는 파이썬의 자료형  
	
| SQLite3 자료형 | python 자료형 |
|:---|:---|
| NULL | None |	
| INTERGE | int |	
| REAL | float |	
| TEXT | str, float |	
| BLOB | buffer |

# 둘다 사용가능함.
> cur.execute('crate table tbl_1(NAME TEXT, Age INTEGER, Money REAL):')	
> cur.execute('crate table tbl_1(NAME str, Age int, Money float):')	
"""
