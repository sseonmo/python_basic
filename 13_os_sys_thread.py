"""
## threading 모듈
- Thread.start() - 쓰레드를 시작할 때 사용
- Thread.run() - 쓰레드의 주요 동작을 정의
- Thread.join([timeout]) - 쓰레드가 종료되기를 기다림

#### Lock 객체
- Lock, unlocked의 2가지 상태를 제공
> 제공메서드
acquire(): locked 상태로 바뀜
release(): unlocked 상태로 바뀜

"""

from threading import Thread, Lock
from time import *

cards = list(range(1, 11))
lock = Lock()

class player(Thread):
	def __init__(self, name):
		Thread.__init__(self)
		self.name = name
		self.mycards = []

	def run(self):
		global cards
		while True:
			lock.acquire()

			if len(cards) > 0:
				self.mycards.append(cards.pop())
				lock.release()
				sleep(0.1)
			else:
				lock.release()
				break

players = []
for name in ['player1', 'player2']:
	print("name : ", name)
	print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
	p = player(name)
	players.append(p)
	p.start()
# name :  player1
# 2019-11-11 11:16:53
# name :  player2
# 2019-11-11 11:16:53

for p in players:
	print("wait : ", p.name)
	print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
	p.join()
	print(p.name, p.mycards)
# 2019-11-11 11:16:53
# player1 [10, 8, 6, 4, 2]
# wait :  player2
# 2019-11-11 11:16:54
# player2 [9, 7, 5, 3, 1]
