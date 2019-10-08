# 모듈
# - 코드의 재사용성
# - 코드를 이름공간으로 구분하고 관리 할 수 있음
# - 복잡하고 어려운 기능을 포함하는 프로그램을 간단하게 만들 수 있음
"""
현재 파이썬 3.0 번전에는 대략 200개가 넘는 모듈을 지원
- 문자열(String), 날짜(date), 시간(time), 십진법(decimal), 랜덤(random)
- 파일(file), os, sqllite3, sys, xml , email, http 등등
"""

import math

print(math.pow(2, 10))
# dir() - 모듈에 어떤 함수 혹은 데이터가 들어있는지 확인 할 수 있다.
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',...]
print(dir(math))

# 모듈만들기
# 사용자가 직접 모듈을 만들 수 있음
# 모듈은 일반적으로 <모듈이름>.py으로 지정
# 모듈의 경로 : sys.path에 저장되어 있는 디렉토리를 검색
#   모듈의 경로 밖의 모듈은 임포트 할 수 없음
# 모듈 경로 탐색순위
# - 프로그램이 실행된 디렉터리
# - python 환경 변수에 등록된 위치
# - 표준 라이브러리 디렉토리
"""
>임포트 방법
import <모듈>
from <모듈> import <어트리뷰트>
from <모듈> import *
import <모듈> as <별칭>
"""

from lib.simpleset import union

a = {1, 2, 3}
b = {3, 4, 5}
print(union(a, b))  # {1, 2, 3, 4, 5}
print(__name__)  # __main__

# 유용한 팀
# - 모듈의 직접 실행과 임포트 되어 실행되었는지 구분하는 방법
# 	> import 되었을때 __name__은 모듈 자신의 이름
# 	> 모듈이 직접 실행 되었을때는 __name__은 '__main__'

# 모듈 팩키지 - __init__.py 를 이용해서 모듈팩키지를 만든다.
