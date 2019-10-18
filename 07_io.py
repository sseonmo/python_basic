import sys

"""
출력 - print()
	> 구분자(sep), 끝(end), 출력(file)
"""
print('welcome to', 'python', sep='||', end='!\n', file=sys.stderr)

# fomatting
print('{} is {}'.format('apple', 'red'))  # apple is red
print('{item} is {color}'.format(item='apple', color='red'))  # apple is red
dic = {'item': 'apple', 'color': 'red'}
print("{0[item]} is {0[color]}".format(dic))  # apple is red
"""
** 기호를 사용하면 dictionary를 입력으로 받은 것으로 판단하고 인자를 하나만 받게됨
불필요한 index를 생략가능
"""
print("{item} is {color}".format(**dic))

# ! 기호를 사용한 문자열 변환
# !s, !r, !a == str(), repr(), ascii()
print("{item!s} is {color!s}".format(**dic))    # apple is red
print("{item!r} is {color!r}".format(**dic))    # 'apple' is 'red'
print("{item!a} is {color!a}".format(**dic))    # 'apple' is 'red'


