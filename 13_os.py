## os 모듈
"""
#### os.getcwd(), os.chdir(path)
- chdir() 함수는 현재 작업 디렉토리 위치를 변경한다.
- getcwd() 함수는 현재 작업 디렉토리의 위치를 반환한다.
"""
from os import *

print(getcwd())
# /Users/guseonmo/Documents/study/python/python_basic
chdir('./lib')
print(getcwd())
# /Users/guseonmo/Documents/study/python/python_basic/lib

"""
#### os.access(path, mode)
- 입력받은 path 에 대해서 mode에 해당하는 작업이 가능한지 여부를 반환한다.
 > F_OK  : 해당 path 존재여부, R_OK : 읽기  
X_OK : 실행, W_OK : 쓰기
"""
print(access('.', F_OK))  # True
print(access('.', W_OK & X_OK & R_OK))  # True
"""
#### os.listdir(path)
- 해당경로에 존재하는 파일과 디렉토리들을 리스트로 반환한다.
"""
print(listdir('.'))  # '05_module.py', '07_io.py', '08_StringControl.py',  ... ]

"""
#### os.mkdir(path[, mode])
- <path>에 해당하는 디렉토리 생
#### os.makedirs(path[, mode])
- 인자로 전달된 디렉토리를 재귀적으로 생성
- 이미 디렉토리가 있는 경우 및 권한이 없으면 예외발
"""
# makedirs('test2/sub1/sub2/leaf')
print(listdir('test2/sub1/sub2'))  # ['leaf']

"""
#### os.remove(path), os.unlink(path)
- 파일을 삭제

#### os.rmdir(path)
- 디렉토리삭제 `단 디렉토리가 비워잇어야 삭제가능`

#### os.removedirs(path)
- 디렉토리를 순차적으로 삭제(역순)

#### os.rename(src, dst)
- src를 dst로 이름을 변경하거나 이동한다. `파일, 디렉토리 모두 적용`

#### os.utime(path, times)
- 경로 해당하는 파일에 대해 액세스 시간(access time)과  
수정시간(modified time)dmf <times>로 수정한다.
- times None 경우 현재시간으로 수정에

#### ow.walk(top [, topdown=True[, onerror=None[, followlinks=False]]])
- top으로 지정된 디렉토리를 순회하며 경로, 디렉토리 명을 순차적으로 반환
- `topdown이 False 입력되면 desc으로 검색`
"""
for path, dirs, files in walk('.'):
	print(path, dirs, files)

"""
#### os.pipe()
- 파이프를 생성
-  (r, w)를 반환하는데, 각각 읽기와 쓰기에 사용할 수 있습니다.

#### os.fdopen(fd[, mode[, bufsize]])
- 파일 디스크립터를 이용해 파일 객체를 생성

#### os.popen(command[, mode[, bufsize]])
- 인자로 전달된 command를 수애하며 파이프를 생
"""
# p = popen('ls -l', 'r')
p = popen('dir', 'r')
print(p.read())
# -rw-r--r--   1 guseonmo  staff   1782 Oct 20 09:36 01_DataType.py
"""
#### os.system(command)
- <command>를 실행하며, 성공한 경우 0을 반환

#### os.startfile(path[, operation])
- <path>를 os에서 지정된 프로그램으로 실행
"""
print(chdir(".."))
print(getcwd())
startfile('test.txt')   # notepad 실행됨. mac에서 지원안함

"""
#### os.excel(path, arg0, arg1, ..)
- 현재 프로세스에서 새로운 프로그램을 수행
> l : 입력인자 수가 정해져 있다.
  v : 튜플로 인자를 받는다.
  e : 환경변수를 인수로 받을 수 있다.
  p : 환경변수의 path를 이용한다.
"""
