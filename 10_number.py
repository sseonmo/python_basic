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

import fractions

print(fractions.Fraction(4, 16))  # 1/4
print(fractions.Fraction(3))  # 3
print(fractions.Fraction('3.14'))  # 157/50

import decimal

# 정수
print(decimal.Decimal(3))  # 3
# 문자열
print(decimal.Decimal('1.1'))  # 1.1
# 튜플
print(decimal.Decimal((0, (3, 1, 4), -2)))  # 3.14
# 음의무한대
print(decimal.Decimal("Infinity"))  # Infinity
# NaN(Not a Number)
print(decimal.Decimal('NaN'))  # NaN

# 객체연산
a, b = decimal.Decimal('3.14'), decimal.Decimal('0.04')
print(a + b)  # 3.18
print(a - b)  # 3.10
print(a * b)  # 0.1256
print(a / b)  # 78.5
print(a % b)  # 0.02
print(a ** b)  # 1.046832472577719248090395663

# ramdom module
import random

print(random.random())  # 0.6288877273639506
print(random.random())  # 0.9081072608530669
print(random.uniform(3, 4))  # 3.2779514435433064
print([random.gauss(1, 1.0) for i in range(3)])  # [1.6710547563870566, 2.06818305305946, -0.40913684745979806]

# 임의의 정수 생성예제
print([random.randrange(20) for i in range(10)])  # [13, 4, 9, 11, 0, 13, 12, 4, 1, 6]
# 중복을 피하긴 위해서 sample 를 사용해야함
print(random.sample(range(20), 10))  # [13, 18, 11, 5, 17, 3, 1, 10, 7, 2]

l = list(range(10))
print([random.choice(l) for i in range(5)])  # [6, 2, 6, 3, 1]
print(random.sample(l, 5))  # [6, 2, 5, 7, 0]
random.shuffle(l)
print(l)  # [3, 2, 1, 7, 4, 8, 6, 5, 0, 9]
