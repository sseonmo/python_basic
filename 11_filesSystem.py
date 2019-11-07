# File System Control

### os.path
from os.path import *
import os

"""
#### os.path.abspath(path)
- 절대 경로를 반환
"""
print(__file__)  # C:/workspace/python_basic/11_filesSystem.py
print(abspath(__file__))  # C:/workspace/python_basic/11_filesSystem.py

"""
#### os.path.basename(path)
- 입력받은 경로의 기본 이름을 반환
"""
print(basename(__file__))  # 11_filesSystem.py

"""
#### os.path.dirname(path)
- 입력받은 파일/디렉터리의 경로를 반환
"""
print(dirname(__file__))  # C:/workspace/python_basic

"""
#### os.path.exists(path)
- 입력받은 경로가 존해하면 Treu, 아니면 False
"""
print(exists(__file__))  # True
print(exists(__file__ + "\\temp"))  # false

"""
#### os.path.expanduser(path)
- 입력받은 경로안의 "~"를 현재 사용자 디렉터리의 절대 경로로 대체
"""
print(expanduser("~"))  # C:\Users\seonmo
print(expanduser("~""\\temp"))  # C:\Users\seonmo\temp
# ~ 다음 다른사용자로 디렉토리로 접근하고 싶을때 ~ 뒤에 다른사용자명을 넣는다.
print(expanduser('~public\\test'))  # C:\Users\public\test

"""
#### os.path.expandvars(path)
- path 안에 환경변수가 있다면 확장
"""
print(expandvars('$APPDATA\\temp'))  # C:\Users\seonmo\AppData\Roaming\temp
print(expandvars('$LOCALAPPDATA\\temp'))  # C:\Users\seonmo\AppData\Local\temp

# # 환경변수 확인
# print(os.environ)
# for k, v in os.environ.items():
# 	print("key: {} / value: {}".format(k, v))

"""
#### os.path.getatime(path)
- 입력받은 경로에 대한 최근 접근 시간을 반환
"""
import time

lastTime = getatime(__file__)
print(lastTime)  # 1573109609.978888
print(time.gmtime(lastTime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=6, tm_min=57, tm_sec=39, tm_wday=3, tm_yday=311, tm_isdst=0)
print(time.localtime(lastTime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=15, tm_min=57, tm_sec=19, tm_wday=3, tm_yday=311, tm_isdst=0)

"""
#### os.path.getmtime(path)
- 입력받은 경로에 대한 최근 변경시간을 반환
"""
lastTime = getmtime(__file__)
print(lastTime)  # 1573109943.6744547
print(time.gmtime(lastTime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=6, tm_min=59, tm_sec=3, tm_wday=3, tm_yday=311, tm_isdst=0)
print(time.localtime(lastTime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=15, tm_min=59, tm_sec=3, tm_wday=3, tm_yday=311, tm_isdst=0)

"""
#### os.path.getctime(path)
- 입력받은 경로에 대한 생성 시간을 반환
"""
crtTime = getmtime(__file__)
print(crtTime)  # 1573111323.1960843
print(time.gmtime(crtTime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=7, tm_min=22, tm_sec=3, tm_wday=3, tm_yday=311, tm_isdst=0)
print(time.localtime(crtTime))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=7, tm_hour=16, tm_min=22, tm_sec=3, tm_wday=3, tm_yday=311, tm_isdst=0)

"""
#### os.path.getsize(path)
- 입력받은 경로에 대한 바이트 단위의 파일 크기를 반환
"""
print(getsize(__file__))  # 4101

"""
#### os.path.isabs(path)
- 경로가 절대경로이면 True, 아니면 False
"""
"""
#### os.path.isfile(path)
- 경로가 파일인지 아닌지 검사, return boolean
"""
"""
#### os.path.isDir(path)
- 경로가 데렉터리인지 아닌지검사, return boolean
"""
"""
#### os.path.join(path1[, path2[, ...]])
- 해당 OS 형삭에 맞도록 입력받은 경로를 연결
"""
print(join(dirname(__file__), 'temp', 'temp2'))  # C:/workspace/python_basic\temp\temp2

"""
#### os.path.normcase(path)
- 해당 OS에 맞도록 입력받은 경로의 문자열을 정규화함
"""
print(normcase(__file__))  # c:\workspace\python_basic\11_filessystem.py
print(normcase(join(dirname(__file__), 'temp', 'temp2')))  # c:\workspace\python_basic\temp\temp2

"""
#### os.path.normpath(path)
- 입력받은 경로를 정규화함
"""
print(normpath(__file__))  # C:\workspace\python_basic\11_filesSystem.py
print(normpath(join(dirname(__file__), '..', '..')))  # C:\

"""
#### os.path.split(path)
- 입력받은 경로를 디렉터리 부분과 파일부분으로 나눔
"""
print(split(__file__))  # ('C:/workspace/python_basic', '11_filesSystem.py')
"""
#### os.path.splitdrive(path)
- 입력받은 경로를 드라이브 부분과 나머지 부분으로 나눔
"""
print(splitdrive(__file__))  # ('C:', '/workspace/python_basic/11_filesSystem.py')
"""
#### os.path.splittext(path)
- 입력받은 경로를 확장자부분과 그외 부분으로 나눔
"""
print(splitext(__file__))  # ('C:/workspace/python_basic/11_filesSystem', '.py')

#
#
# # join 중 절대경로가 나오면 이전 path는 무시하고 다시 취합한다.
#
#
# # 그 외 자주 사용되어지는...
# #  파일경로
# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# #  현재파일의 디렉토리 경로
# print(os.getcwd())
# print(os.path.dirname(os.path.realpath(__file__)))
# # 현재 디렉토리에 있는 파일 리스트
# print(os.listdir(os.getcwd()))
# # 작업 디렉토리 변경
# print("before: ", os.getcwd())
# os.chdir("C:\\workspace")
# print("after: ", os.getcwd())

### glob

"""
#### glob.glob(path)
# - Path 경로에 대응되는 모든 파일 및 다렉터리의 리스트를 반환
# - 경로를 주는 방식에 따라 절대 경로로 결과가 나오게 할 수도 있음
"""
import glob

files = glob.glob(join(abspath("."), '*.py'))
print(files)  # ['C:\\workspace\\python_basic\\01_DataType.py', 'C:\\workspace\\python_basic\\02_function.py']
[print(basename(file)) for file in files]  # 01_DataType.py, 02_function.py

"""
#### glob.iglob(path)
- glob과 동일한 동작을 수행하지만, 리스트로 결과를 반환하지 않고 이터레이터로 반환
- 이터레이터로 반환 / 결과값이 매우 만을때 유용함
"""

### tree 만들기

import glob, os.path

def traverse(dir, depth):
	for obj in glob.glob(os.path.join(dir, '*')):

		if depth == 0:
			prefix = '|--'
		else:
			prefix = '|' + ' ' * depth + '+--'

		if os.path.isfile(obj):
			print(prefix + os.path.basename(obj), " " + str(depth))
		elif os.path.isdir(obj):
			print(prefix + os.path.basename(obj), " " + str(depth))
			traverse(obj, depth + 1)
		else:
			print(prefix + 'unknown object', obj)

if __name__ == '__main__':
	traverse("..", 0)
