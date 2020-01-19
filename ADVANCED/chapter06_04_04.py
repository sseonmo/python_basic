# Chapter06-04-01
# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점부터 재실행 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO -> Thread 사용
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결

# aiohttp 사용가능(Asyncio 지원)

import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio
import aiohttp

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://gmarket.co.kr', 'http://www.naver.com']
start = timeit.default_timer()

async def fetch(session, url):
	print('Thread Name', threading.current_thread().getName(), 'Start', url)
	async with session.get(url) as response:
		res = await response.text()
		return res[0:5]
	# print('Thread Name', threading.current_thread().getName(), 'Done', url)
	# return await res.read()[0:5]

async def main():
	html = []
	async with aiohttp.ClientSession() as session:
		for url in urls:
			html.append(await fetch(session, url))

	print()
	# 결과확인
	print('Result : ', html)

if __name__ == '__main__':
	# 루프 생성
	loop = asyncio.get_event_loop()
	# 루프 대기
	loop.run_until_complete(main())

	# 함수 실행
	main()
	# 완료시간 - 사작시간
	duration = timeit.default_timer() - start

	# 총 실행 시간
	print('Total time ', duration)