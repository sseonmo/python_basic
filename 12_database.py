# 데이터베이스
"""
### Sqlite3
- 디스크 기반의 가벼운 데이터베이스 라이브러리
-서버 X , 모바일 디바이스에서 기본적으로 사용
- 파이썬 defualt 로 포함되어있음.
- 모듈 함수
| 함수 | 설명 |
|:---|:---|
| sqlite3.connect(database[timeout, isolation_level, detect_types, factory]| SQLite3 DB에 연결 |
| sqlite3.complete_statement(sql) | sql 문장에 대해서 True를 반환(검증??) |
| sqlite3.register_adapter(type, callable) | 사용자 정의 파이썬 자료형을 SQLite3에서 사용하도록 등록 |
| sqlite3.register_converter(typename, callable) | SQLite3에 저장된 자료를 사용자 정의 자료형으로 변화하는 함수를 등록  |

- Connection 클래스

| 메서드 | 설명 |
|:---|:---|
| Connection.cursor() | Cursor 객체 설정 |
| Connection.commit() | 현재 트랜잭션의 변경내역을 DB에 반영 |
| Connection.rollback() | 가장 최근 commit() 이후 상태로 작업한 내용을 되돌림 |
| Connection.close() | DB 연결 종료 |
| Connection.isolation_level() | 트랜잭션 격리수준(isolation level) 을 확인 및 설정 |
| Connection.execute(sql[, parameters]) | 임시 Cursor객체를 생성하여 해당 execute 계열메서드를 수행 |
| Connection.executemany(sql[, parameters]) |
| Connection.executescript(sql_script) |
| Connection.crate_aggregate(name, num_params
, aggregate_class) | 사용자  정의 집계(aggregate) 함수를 생성 |
| Connection.crate_collation(name, callable) | 문자열 정렬시 SQL 구문에서 사용될 이름(name)과 정렬 함수를 지정 |
| Connection.iterdump() | 연결된 DB의 내용을 SQL 질의로 형태를 출력 |

- Cursor 클래스

| 메서드 | 설명 |
|:---|:---|
| Cursor.execute(sql[, parameters]) | sql 문장을 실행 |
| Cursor.executemany(sql, seq_os_parameters]) | 동일한 SQL 문장을 파라미터만 변경하며 수행 |
| Cursor.executescript(sql_script) | 세미콜론으로 구분된 연속된 sql문장을 수행|
| Cursor.fetchone() | 조회된 결과(Record Set)로부터 데이터 1개를 반환 |
| Cursor.fetchmany([size=curosr.arraysize]) | 조회된 결과로 부터 입력받은 size 만큼의 데이터를 리스트로 반환 |
| Cursor.fetchall() | 조회된 결과 모두를 리스트로 반환 |

"""

import sqlite3

# 파일디비 생성 - test.db 파일이 생성됨
con = sqlite3.connect("test.db")
# 메모리기반 db 생성
# con = sqlite3.connect(":memory:")
cur = con.cursor()
# create table
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")

# #1 row insert
cur.execute("INSERT INTO PhoneBook values ('Someone1', '010-1234-5678');")
# #2 row insert - 인자전달방식
name = 'Someone2'
phoneNum = '010-1234-5678'
cur.execute("INSERT INTO PhoneBook values (?, ?);", (name, phoneNum))
# #3 row insert - dict 이용한 인자전달
name1 = 'Someone3'
phoneNum1 = '010-1234-5678'
cur.execute("INSERT INTO PhoneBook values (:inputName, :inputNum);", {"inputName":name1, "inputNum": phoneNum1})
# #4 row insert - 연속적인 수행
dataList = (('Tom', '010-1234-5678'), ('Mike', '010-1234-5678'))
cur.executemany("INSERT INTO PhoneBook values (?, ?);", dataList)

# 조회 - fetch
cur.execute("select * from PhoneBook;")
for row in cur:
	print(row)

# 조회 - fetchone, fetchmany
cur.execute("select * from PhoneBook;")
print(cur.fetchone())
print(cur.fetchmany(2))

# 조회 - fetchall
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

# 트랜잭션처리
con.commit()



