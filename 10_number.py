"""
# 숫자다루기

### 수학(math) 모듈
#### 내장함수
| 함수명 | 설명 |
|:---|:---|

### 분수(fractions) 모듈
- 유리수와 관련된 연산을 효율적으로 처리할 수 있는 분수(fractions) 모듈
#### 지원메소드


### 십진법(decimal) 모듈


### 랜덤(random) 모듈
제수, 피제수
유리수

"""

l = list(range(0, 10))
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(l))  # 45
print(max(l))  # 9
print(min(l))  # 0
print(abs(-11))  # 11
print(pow(2, 10))  # 1024
print(divmod(11, 2))  # (5, 1)

import math

print(math.ceil(3.14))  # 4
print(math.floor(3.14))  # 3
print(math.trunc(3.14))  # 3
print(math.modf(3.14))  # (0.14000000000000012, 3.0)

# 주의 - 부호가 다른 값의 나머지를 구할때는 math.fmod 사용하는 것이 정확하다.
#  피제수와 제수의 부호가 같은 경우
print(math.fmod(5.5, 3))  # 2.5
print(5.5 % 3)  # 2.5
#  피제수와 제수의 부호가 다른 경우
print(math.fmod(-5.5, 3))  # -2.5
print(-5.5 % 3)  # 0.5

