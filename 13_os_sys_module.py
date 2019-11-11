"""
## sys모듈

#### sys.argv
- 파이썬 스크립트로 넘어온 입력인자(argument)들의 리스트
"""
import sys

print("argv size :", len(sys.argv))  # argv size : 2
for i, arg in enumerate(sys.argv):
	print(i, arg)
# 0 13_os_sys_module.py
# 1 arg1

"""
#### sys.exc_info()
- 현재 발생한 예외정보를 튜플로 반환한다. 예외가 없으면 None를 반환  
- 반환값 : 예외 클래스, 예외값, traceback 객체를 반환한다.

#### sys.exc_info()
- 프로세스 종료( arg가 0 일때 정상종료, 이 외 비정상종료)

#### sys.path
- 모듈을 찾을 때 참조하는 경로를 나타냄
"""
print(sys.path)
