"""
def <함수명>(인수1, 인수2, ...인수n):
    <구문>
    return <반환값>
"""

def multiply(a, b):
	return a * b

print(multiply(10, 20))  # 200

# 기본인수
def sum1(a=10, b=20):
	return a * b

print(sum1())  # 100
print(sum1(20))  # 200

# 키워드인수
def connectURL(server, port):
	# strUrl = "http://" + server + ":" + port
	strUrl = "http://{}:{}".format(server, port)
	return strUrl

print(connectURL("test.com", "8080"))  # http://test.com:8080
print(connectURL(port="8080", server="test.com"))  # http://test.com:8080

# 가변인수 리스트
def union2(*ar):
	res = []
	for item in ar:
		for x in item:
			if not x in res:
				res.append(x)
	return res

print(union2("HAM", "EGG", "SPAM"))  # ['H', 'A', 'M', 'E', 'G', 'S', 'P']

# 정의되지 않은 인수 처리하기
def userURLBuilder(server, port, **user):
	strUrl = "http://{}:{}/?".format(server, port)
	for key in user.keys():
		strUrl += "{}={}&".format(key, user[key])
	return strUrl

print(userURLBuilder('test.com', '8080', id='userid', passwd='1234'))  # http://test.com:8080/?id=userid&passwd=1234&
print(userURLBuilder('test.com', '8080', id='userid', passwd='1234',
                     name='mike'))  # http://test.com:8080/?id=userid&passwd=1234&name=mike&

# 람다함수
""" lambda 인수: <구문> """
g = lambda x, y: x * y
print(g(2, 2))  # 4
print((lambda x: x * x)(3))  # 9

# __doc__ 속성과 help 함수
help(print)

def plus(a, b):
	return a + b

"""
Help on function plus in module __main__:
plus(a, b)
"""
help(plus)

# 이터레이터
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

coll = MyCollection(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(coll))

# for x in coll:
# 	print(x)

# 제네레이터
def square_number(nums):
	for i in nums:
		yield i

numbers = square_number([1, 2, 3, 4, 5])

print(type(numbers))  # <class 'generator'>
# print(sum(numbers))     # 15
print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
print(next(numbers))  # 4
print(next(numbers))  # 5
print(next(numbers))  # 예외발생 - print(next(numbers))       # 예외발생
